#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

#-------------System-------------------#
from time import sleep
import os
import win32clipboard as cp
import socket

#---------Mis funciones---------------#
from utileria import *
from logueo import *
from convenio_cobranza import *
import Services.ApiCyberHubOrdenes as api
from rutas import *
from actividades import *
from fallas_servicio import *
from eliminar_archivos_temporales import eliminar_archivos
#---------Variables globales---------------#

USER = "apiliado"
PASS = 'Rosasrojas_2023'
FINALIZADO_ERROR = 'FLUJO FINALIZADO CON ERROR'



def workflow():
    '''
    Funcion encargada de hacer el flujo completo del bot

    '''
    #Inicio de sesion
    response = api.get_user()
    user = response['procesoUser']
    password = response['procesoPassword']
    driver, status_logueo = login_siebel(user, password)
    

    if status_logueo != True:
        print('Logueo Incorrecto')
        text_box(FINALIZADO_ERROR,'♦')
        return False
    
    while status_logueo == True:

        apiresponse = api.get_orden_servicio()
        info = apiresponse[0]
        print(info)
        host = socket.gethostname()
        ip = socket.gethostbyname(host)

        # info = '123'

        if info != 'SIN INFO':

            # Obtencion de cuentaSUCURSAL OFICINA CENTRAL CUAUTLA
            # status_tupla,info['cuenta'], info['casoNegocio'], comentarios = actividades_asigandas(driver)
            # status_actividades_asigandas, tipo_error = status_tupla

            # info['casoNegocio'] = '1151425829725'
            # no_cuenta = '60606545'

            # if tipo_error != '': text_box(tipo_error, '█')

            # if  tipo_error == 'No hay cuentas':
            #     print('No hay cuentas asignadas, espere...')
            #     sleep(10)
            #     break

            # if  tipo_error == 'Cuenta Vencida':
            #     print('La cuenta esta vencida, se procede a cancelar el caso de negocio')
            #     motivo_cancelacion = 'PERIODO INCORRECTO'
            #     pantalla_unica_consulta(driver, no_cuenta)
            #     if  cancelar_caso(driver,info['cuenta'], info['casoNegocio'], motivo_cancelacion ): break

            # if  no_cuenta == None or info['casoNegocio'] == None:
            #     text_box(FINALIZADO_ERROR,'♦')
            #     return False
            
            # #Regreso home
            # if open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] ) != True: return False
        
            # Busqueda de caso de negocio obtenido para validar el MOTIVO CLIENTE
            # cuenta = '37055565'
            # cn = '1161825969364'
            # cuenta_valida, motivo_cliente = pantalla_caso_negocio(driver,cuenta, cn)
            cuenta_valida, motivo_cliente = pantalla_caso_negocio(driver,info['cuenta'], info['casoNegocio'])
            if cuenta_valida == False:
                text_box('Cuenta no valida', '▬')
                break
                
            #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ T I P O   D E   A J U S T E ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
            if motivo_cliente.upper() == 'CARGO EXTEMPORANEO':
                    # status_validacion_cuenta, causa_rechazo, error = validacion_cuenta_cargo_extemporaneo(driver,cuenta, cn)
                    status_validacion_cuenta, causa_rechazo, errorVali = validacion_cuenta_cargo_extemporaneo(driver,info['cuenta'], info['casoNegocio'])
                    #if 'Message' in causa_rechazo or  causa_rechazo == '': return False
                    print('▄▄▄ CUENTA RECHAZADA ▄▄▄ ')
                    print('Causa: ', causa_rechazo)

                    

                    if errorVali == 'Ajuste Reciente':
                        status = 'Cancelado - Error ' + errorVali
                        response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                        print(response)

                        print('Causa: ', causa_rechazo)
                        if status_validacion_cuenta == False: 
                            cancelar = cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )
                    
                    else:
                        if 'Error Pantalla Unica' in errorVali:
                            status = 'Pendiente'
                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,'0',ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                            print(response)
                            return False

                        if causa_rechazo == True and errorVali != 'Ajuste Mes':
                            status = 'Cancelado - Error ' + errorVali
                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                            print(response)

                            print('Causa: ', causa_rechazo)
                            if status_validacion_cuenta == False: 
                                cancelar = cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )
                        
                        else:
                            status_factura, fecha_fatcura, error = busqueda_factura(driver,info['cuenta'], info['casoNegocio'])

                            if errorVali == 'Ajuste Mes':

                                status_cierre_actividad, error = cierre_caso_y_actividad(driver, info['cuenta'], info['casoNegocio'], fecha_fatcura,'Extemporaneo')
                                if status_cierre_actividad == False: 
                                    status = 'Error ' + error
                                    response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                    print(response)
                                    
                                else:
                                    status = 'Cerrado'
                                    response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                    print(response)
                            else:

                                if status_factura == False: 
                                    status = 'Error ' + error
                                    response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                    print(response)
                                    try:
                                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]').click()
                                    except Exception:
                                        print('Pantalla ajustada')
                                        sleep(5)
                                    cancelar = cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )
                                else:
                                    status_ajuste, error =  aplicacion_ajuste_cargo_extemporaneo(driver, fecha_fatcura, info['casoNegocio'] ) 
                                    if status_ajuste == False and 'Error' not in error:
                                        status = 'Error ' + error
                                        response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                        print(response)
                                    elif status_ajuste == False and 'Error' not in error:
                                        print('Home')
                                    else:    
                                        status_cierre_actividad, error = cierre_caso_y_actividad(driver, info['casoNegocio'], info['casoNegocio'], fecha_fatcura,'Extemporaneo')
                                        if status_cierre_actividad == False: 
                                            status = 'Error ' + error
                                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                            print(response)
                                            
                                        else:
                                            status = 'Cerrado'
                                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                            print(response)

            elif  motivo_cliente.upper() == 'CONVENIO COBRANZA':
                status_validacion_cuenta, causa_rechazo, monto, error, rx = validacion_cuenta_convenio_cobranza(driver,info['cuenta'], info['casoNegocio'])
                print('▄▄▄ CUENTA RECHAZADA ▄▄▄ ')
                if 'Error Pantalla Unica' in error:
                    status = 'Pendiente'
                    response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,'0',ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                    print(response)
                    return False

                if error == 'Ajuste Reciente':
                    status_cierre_actividad, error = cierre_caso_y_actividad(driver, info['cuenta'], info['casoNegocio'], '', 'Cobranza')
                    if status_cierre_actividad == False:
                        status = 'Error ' + error
                        response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                        print(response)
                        
                    else:
                        status = 'Cerrado'
                        response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                        print(response)

                elif error == 'Ajuste 6 Meses':
                    status = 'Cancelado - No Aplica ' + error
                    print(status)
                    response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                    print(response)

                    print('Causa: ', causa_rechazo)
                    if status_validacion_cuenta == False: 
                        # cancelar = cancelar_caso(driver,cuenta, cn, 'FALTA SOPORTE' )
                        cancelar = cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )

                
                        
                elif causa_rechazo == True: 
                    status = 'Cancelado - No Aplica ' + error
                    print(status)
                    response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                    print(response)

                    print('Causa: ', causa_rechazo)
                    if status_validacion_cuenta == False: 
                        cancelar = cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )
                else:
                    status_ajuste, error =  aplicacion_ajuste_convenio_cobranza(driver, info['casoNegocio'], monto) 
                    if status_ajuste == False: 
                        status = 'Error ' + error
                        print(status)
                        response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                        print(response)
                    else:
                        status_cierre_actividad, error = cierre_caso_y_actividad(driver, info['cuenta'], info['casoNegocio'], '', 'Cobranza')
                        if status_cierre_actividad == False:
                            status = 'Error ' + error
                            print(status)
                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                            print(response)
                            
                        else:
                            status = 'Cerrado'
                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                            print(response)
            elif  motivo_cliente.upper() == 'FALLAS EN EL SERVICIO':
                    status_validacion_cuenta, causa_rechazo, monto, error = validacion_cuenta_fallas_servicio(driver,info['cuenta'], info['casoNegocio'], 1)
                    print('▄▄▄ CUENTA RECHAZADA ▄▄▄ ')
                    if causa_rechazo == True: 
                        status = 'Cancelado - Error ' + error
                        response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                        print(response)

                        print('Causa: ', causa_rechazo)
                        if status_validacion_cuenta == False: 
                            cancelar = cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )
                    else: 
                        status_ajuste, error =  aplicacion_ajuste_convenio_cobranza(driver, info['casoNegocio'], monto) 
                        if status_ajuste == False: 
                            status = 'Error ' + error
                            response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                            print(response)
                        else:
                            status_cierre_actividad, error = cierre_caso_y_actividad(driver, info['casoNegocio'], info['casoNegocio'], '', 'Cobranza')
                            if status_cierre_actividad == False:
                                status = 'Error ' + error
                                response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                print(response)
                                
                            else:
                                status = 'Confirmado'
                                response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                                print(response)


            elif  motivo_cliente.upper() == 'RETENCION 20% X 5 MESES':
                    # numero_pago = extraccion_numero_pago( comentarios)
                    # if numero_pago == False: return False
                    status_validacion_cuenta, causa_rechazo, monto = validacion_cuenta_ajusteRet5(driver,info['cuenta'], info['casoNegocio'], 1)
                    print('▄▄▄ CUENTA RECHAZADA ▄▄▄ ')
                    if 'Message' in causa_rechazo or  causa_rechazo == '': return False
                    print('Causa: ', causa_rechazo)
                    if status_validacion_cuenta == False: return cancelar_caso(driver,info['cuenta'], info['casoNegocio'], 'FALTA SOPORTE' )
                    status_ajuste =  aplicacion_ajuste_convenio_cobranza(driver, info['casoNegocio'], monto) 
                    if status_ajuste == False: return False    
                    status_cierre_actividad = cierre_caso_y_actividad(driver, info['casoNegocio'], info['casoNegocio'], '')
                    if status_cierre_actividad == False: return False
            else:
                status = 'Error Ajuste Invalido'
                response = api.ajusteCerrado(info['id'],info['cuenta'],info['casoNegocio'],info['cve_usuario'],info['motivo'],info['motivoCliente'],info['estado'],status,info['procesando'],ip,info['fechaCreado'],info['fechaCompletado'],info['fechaCarga'], info['fechaVencimiento'])
                print(response)
                return False
        else:
            try:
                os.system('cls')
                print('Esperando mas Ajustes')
                sleep(15)
                print('Regreso a HOME')
                open_item_selenium_wait(driver, xpath = home['home_from_sidebar']['xpath'])
                text_box('FIN EL CICLO COMPLETO', '-')
            except Exception:
                return False
                


#
while True == True:
    conteo_errores = 0
    # # Buscamos todos los procesos de Google Chrome en ejecución
    try:
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
    except Exception as e:
        pass
    
    eliminar_archivos()

    error_main = workflow()
    if error_main == False:
        conteo_errores = conteo_errores + 1
        print('conteo_errores::: ', conteo_errores)
        if conteo_errores >= 5:
            os.system(f"taskkill /f /im chrome.exe")
            error_main = workflow()
            text_box ('ERROR CRITICO, REVISAR', '¶¶')
            sleep(1)


