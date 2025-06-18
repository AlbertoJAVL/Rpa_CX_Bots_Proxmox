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
from ordenesServicio import *
from caso_de_negocio import  *
import Services.ApiCyberHubOrdenes as api

#---------Variables globales---------------#

USER = "rpadepura.service"
PASS = 'H76EUdKg5V7e2rh/'
FINALIZADO_ERROR = 'FLUJO FINALIZADO CON ERROR'


def __main__():
    '''
    Funcion encargada de hacer el flujo completo del bot

    '''
    #Inicio de sesion
    response = api.get_data_user2()
    user = response['procesoUser']
    password = response['procesoPassword']

    driver, status_logueo = login_siebel(user, password)
    global sesion
    sesion = USER

    while status_logueo == True:
        
            # user, password = api.usuario()
            # #user = "p-jlima"
            # #password = 'sobu*8vlDros'
            
            #SI EL LOGEO FUE CORRECTO
            if status_logueo == True:
                text_box('CUENTA DE: ' + sesion,'▬')

                try:
                    apiresponse = api.get_orden_servicio()   
                    host = socket.gethostname()
                    ip = socket.gethostbyname(host)
                    print(apiresponse)
                except Exception as e:
                    print(e)
                    apiresponse = ['SIN INFO']
                    sleep(15)

                if apiresponse != ['SIN INFO']:             
                    info = apiresponse['info']
                    print(info)
                
                    cuenta_api = info[0]['cuenta']
                    numero_orden = info[0]['numOrden']
                    source_api = info[0]['source']      
                    

                    #DATOS ONDEN DE SERVICIO
                    datos_os = apiresponse['datos_os']
                    comentarios = datos_os[0]['comentarios']
                    motivo = datos_os[0]['motivo_de_Cancelacion']
                    estadoC = datos_os[0]['estado']

                    #DATOS CASO DE NEGOCIO
                    datos_cn = apiresponse['datos_cn']
                    medio_contacto_cn = datos_cn[0]['medio_de_contacto']
                    categoria_cn = datos_cn[0]['categoría']
                    motivo_cn = datos_cn[0]['motivos']
                    sub_motivo_cn = datos_cn[0]['submotivo']
                    solucion_cn = datos_cn[0]['solución']
                    comentarios_cn = datos_cn[0]['comentarios']
                    motivo_cierre_cn = datos_cn[0]['motivo_del_cierre']
                    estado_cn = datos_cn[0]['estado']

                    print('* Comentarios CN:',comentarios_cn)


                    '''▬▬▬▬▬▬▬▬▬▬▬▬ ORDENES DE SERVICIO ▬▬▬▬▬▬▬▬▬▬▬▬'''

                    driver, status_ordenesServicio = pantalla_ordenes_Servicio(driver, numero_orden)
                    if status_ordenesServicio == False:
                        text_box(FINALIZADO_ERROR,'♦')
                        status = 'Orden no valida'
                        response = api.cuenta_erronea(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],info[0]['cn_generado'],info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source'])
                        print('Respuesta de API (Cancelada por IZZI)')
                        driver.close()
                        driver.quit()
                        return False
                    
                    status_orden_valida, driver, estado_orden = validacion_orden_servicio(driver)
                    if status_orden_valida == False:
                        status = 'Orden no valida'
                        response = api.orden_cerrada(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],info[0]['cn_generado'],info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source'])
                        print('Respuesta de API (Cancelada por IZZI)')
                        text_box(FINALIZADO_ERROR,'♦')
                        driver.close()
                        driver.quit()
                        return False

                    '''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬CANCELAR ORDEN▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''
                    #Si la orden ya esta cancelada
                    if 'cancelado' in  estado_orden or 'completa'  in  estado_orden:
                        text_box('CUENTA CANCELADA POR IZZI','▄')
                        status = 'Orden Cancelado por un tercero'
                        response = api.orden_cerrada(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],info[0]['cn_generado'],info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source'])
                        print('Respuesta de API (Cancelada por IZZI: )',response)
                        sleep(2)
                        status_home = open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                        open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                        text_box('FIN DEL CICLO POR PREVIA CANCELACION', '▬')
                       
                    
                    else:
                        status_orden_cerrada = cerrar_orden_servicio(driver, cuenta_api, source_api, comentarios, motivo, estadoC)
                        if status_orden_cerrada != True:
                            text_box(FINALIZADO_ERROR,'♦')
                            status = 'Error al cancelar Orden'
                            response = api.orden_cerrada(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],info[0]['cn_generado'],info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source'])
                            print('Respuesta de API (Cancelada por IZZI: )',response)
                            driver.close()
                            driver.quit()
                            return False
                        status = 'Orden Cancelado por RPA'
                        response = api.orden_cerrada(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],info[0]['cn_generado'],info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source'])
                        print('Respuesta de API (Cancelada por IZZI: )',response)
                        
                        '''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬CASO DE NEGOCIO▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''

                        status = True #respuesta['status']
                        if status == True:
                            status_pantalla_unica  = pantalla_unica_consulta(driver, cuenta_api)
                            if status_pantalla_unica != True:
                                text_box(FINALIZADO_ERROR,'♦')
                                driver.close()
                                driver.quit()
                                return False

                            status_nuevo_caso = nuevo_caso_negocio(driver,
                                                                medio_contacto_cn, 
                                                                categoria_cn,
                                                                motivo_cn, 
                                                                sub_motivo_cn,
                                                                solucion_cn,  
                                                                motivo_cierre_cn, 
                                                                comentarios_cn, 
                                                                estado_cn
                                                                )
                            if status_nuevo_caso == 0:
                                print('Caso de negocio existente')
                                status = 'Orden Cancelado por RPA'
                                cn = 'Ya existe un CN Abierto'
                                response = api.orden_cerrada(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],cn,info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source']) 
                                print('Respuesta de API (ERROR SIBEL)',response)
                                #Quiza vaya un return
                            elif status_nuevo_caso == 2:
                                print("Caso de negocio Abierto")
                                #Quiza vaya un return
                            elif status_nuevo_caso == False:
                                text_box('Fallo la creacion del caso de negocio')
                                text_box(FINALIZADO_ERROR,'♦')
                                driver.close()
                                driver.quit()
                                return False
                            else:
                                status = 'Orden Cancelado por RPA'
                                cn = status_nuevo_caso
                                response = api.orden_cerrada(info[0]['id'],info[0]['lead_id'],info[0]['comentarios'],info[0]['compania'],info[0]['estado'],info[0]['hub'],info[0]['motivoOrden'],info[0]['nodo'],info[0]['cuenta'],info[0]['numOrden'],info[0]['tipo'],cn,info[0]['fechaHoraCierre'],info[0]['fechaCompletado'],info[0]['fechaCarga'],info[0]['fechaCreado'],info[0]['cve_usuario'],status,info[0]['procesando'],ip,info[0]['source']) 
                                print('Respuesta de API (CASO CERRADO EXITOSAMENTE)',response)

                            print('Regreso a HOME')
                            open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                            text_box('FIN DEL CICLO COMPLETO', '▬')
                else:
                    print('Esperando Ordenes de Servicio')
                    sleep(15)
                    print('Regreso a HOME')
                    open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                    text_box('FIN DEL CICLO COMPLETO', '▬')



while True == True:
    conteo_errores = 0
    # Buscamos todos los procesos de Google Chrome en ejecución
    try:
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
    except Exception as e:
        pass

    error_main = __main__()
    if error_main == False:
        conteo_errores = conteo_errores + 1
        print('conteo_errores::: ', conteo_errores)
        if conteo_errores >= 5:
            text_box ('ERROR CRITICO, REVISAR', '¶¶')
            sleep(10000)

