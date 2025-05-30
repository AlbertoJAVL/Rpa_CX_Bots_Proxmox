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


USER = "rpaajustes.service"
PASS = 'mpCtP6xnZZS9Cx8/'
# USER = "TSTCALLCENTER"
# PASS = 'TSTCALLCENTeR_2023'
FINALIZADO_ERROR = 'FLUJO FINALIZADO CON ERROR'



def workflow():
    '''
    Funcion encargada de hacer el flujo completo del bot

    '''
    try:
        #Inicio de sesion
        response = api.get_user()
        user = response['procesoUser']
        password = response['procesoPassword']
        driver, status_logueo = login_siebel(user, password)
        # driver, status_logueo = login_siebel('rpaajustes2.service', '6yckCF6GjhyxjJSU/')
        

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

            if info != 'SIN INFO':
                response = api.ajusteCerrado(
                    info['id'],
                    info['cuenta'],
                    info['motivoAjuste'],
                    info['comentarioAjuste'],
                    info['cantidadAjustar'],
                    info['tipoAplicacion'],
                    info['cve_usuario'],
                    info['fechaCompletado'],
                    info['fechaCaptura'], 
                    'Procesando', 
                    '0', 
                    ip, 
                    '-', 
                    '-', 
                    '-', 
                    info['subStatus'],
                    info['usuarioReproceso'],
                    info['fechaReproceso'],
                    info['usuarioCambio'],
                    info['fechaCambio']
                    )
                ajuste = info['cantidadAjustar']
                tipoAjuste = info['tipoAplicacion']
                no_cuenta = info['cuenta']
                motivoAjuste = info['motivoAjuste'].upper()
                ComentariosAjuste = info['comentarioAjuste']
                fecha = info['fechaCaptura']

                fechaCompletado = info['fechaCompletado']
                if fechaCompletado == None: pass
                else:
                    fechaCompletado = fechaCompletado[:10]

                if 'CARGO' in motivoAjuste or 'PAGO' in motivoAjuste or 'EXTEMPORANEO' in motivoAjuste: motivoAjuste = 'CARGO POR PAGO EXTEMPORANEO'
                elif 'CONVENIO' in motivoAjuste or 'COBRANZA' in motivoAjuste: motivoAjuste = "CONVENIO DE COBRANZA"
                else: 
                    status = 'Error Base Convenio'
                    response = api.ajusteCerrado(
                        info['id'],
                        info['cuenta'],
                        info['motivoAjuste'],
                        info['comentarioAjuste'],
                        info['cantidadAjustar'],
                        info['tipoAplicacion'],
                        info['cve_usuario'],
                        info['fechaCompletado'],
                        info['fechaCaptura'], 
                        status, 
                        '0', 
                        ip, 
                        '-', 
                        '-', 
                        estatusAjuste, 
                        info['subStatus'],
                        info['usuarioReproceso'],
                        info['fechaReproceso'],
                        info['usuarioCambio'],
                        info['fechaCambio'])
                    print(response)
                    return False

                sleep(5)
                resultadoAplicacionAjuste, error, numAjuste, estatusAjuste = aplicacionAjuste(driver, fechaCompletado, ajuste, no_cuenta, tipoAjuste,motivoAjuste,ComentariosAjuste,fecha, info['subStatus'], info['numeroAjuste'])
                print('Aplicacion de Ajuste completa')
                if resultadoAplicacionAjuste == False:
                    print(error)
                    status = error
                    status2 = '-'
                    response = api.ajusteCerrado(
                        info['id'],
                        info['cuenta'],
                        info['motivoAjuste'],
                        info['comentarioAjuste'],
                        info['cantidadAjustar'],
                        info['tipoAplicacion'],
                        info['cve_usuario'],
                        info['fechaCompletado'],
                        info['fechaCaptura'], 
                        str(status), 
                        '0', 
                        ip, 
                        numAjuste, 
                        '-', 
                        estatusAjuste, 
                        str(status2),
                        info['usuarioReproceso'],
                        info['fechaReproceso'],
                        info['usuarioCambio'],
                        info['fechaCambio'])
                    print(response)
                    return False
                        
                else:
                    resultadoCreacionCN, error, cnGenerado = generacionCN(driver)
                    print('Creacion de nuevo caso de negocio, completa')
                    if resultadoCreacionCN == False:
                        print('Falla al crear el caso de negocio')
                        status = error
                        status2 = '-'
                        response = api.ajusteCerrado(
                            info['id'],
                            info['cuenta'],
                            info['motivoAjuste'],
                            info['comentarioAjuste'],
                            info['cantidadAjustar'],
                            info['tipoAplicacion'],
                            info['cve_usuario'],
                            info['fechaCompletado'],
                            info['fechaCaptura'],
                            status, 
                            '0', 
                            ip, 
                            numAjuste, 
                            '-', 
                            estatusAjuste, 
                            status2,
                            info['usuarioReproceso'],
                            info['fechaReproceso'],
                            info['usuarioCambio'],
                            info['fechaCambio'])
                        print(response)
                        return False
                    else:
                        print('Ajuste Completado')
                        status = 'Aplicación correcta'
                        status2 = '-'
                        response = api.ajusteCerrado(
                            info['id'],
                            info['cuenta'],
                            info['motivoAjuste'],
                            info['comentarioAjuste'],
                            info['cantidadAjustar'],
                            info['tipoAplicacion'],
                            info['cve_usuario'],
                            info['fechaCompletado'],
                            info['fechaCaptura'], 
                            status, 
                            '0', 
                            ip, 
                            numAjuste, 
                            cnGenerado, 
                            estatusAjuste,
                            status2,
                            info['usuarioReproceso'],
                            info['fechaReproceso'],
                            info['usuarioCambio'],
                            info['fechaCambio'])
                        print(response)


                    
            
            else:
                try:
                    # os.system('cls')
                    print('Esperando mas Ajustes')
                    sleep(15)
                    print('Regreso a HOME')
                    result = open_item_selenium_wait(driver, xpath = home['home_from_sidebar']['xpath'])
                    if result == False:
                        return False
                    text_box('FIN EL CICLO COMPLETO', '-')
                    os.system('cls')
                except Exception as e:
                    return False
    except Exception as e: print(e);  return False


#██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
while True == True:
    conteo_errores = 0
    # # Buscamos todos los procesos de Google Chrome en ejecución
    try:
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        
    
    except Exception as e:
        print(e)

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


