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
import json
import socket
from datetime import datetime, time, date

#---------Mis funciones---------------#
from utileria import *
from logueo import *
from extraccion import *
from caso_de_negocio import  *
import Services.ApiCyberHubOrdenes as api
from rutas import *
from eliminar_archivos_temporales import eliminar_archivos
#---------Variables globales---------------#

# USER = "p-lggarciah"
# PASS = 'sobu*8vlDros'

#USER = "kmromero"
# PASS = 'Slytherin.010913A'

USER = "validacionnd.service"
PASS = 'yuchuf=xe5#ZehEf'

# USER = "rbernal"
# PASS = 'Proyectos.0523'

# USER = "sriveraram"
# PASS = "Sus4n4-1985."
FINALIZADO_ERROR = 'FLUJO FINALIZADO CON ERROR'

def verificacionLSiebel(driver):
    try:

        print('Verificacion SIEBEL')
        result = open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
        if result == False:
            return False
        return True
    
    except Exception:
        return False

def __main__():
    '''
    Funcion encargada de hacer el flujo completo del bot

    '''
    #Inicio de sesion
    response = api.get_data_user()
    user = response['procesoUser']
    password = response['procesoPassword']
    driver, status_logueo = login_siebel(user, password)
    global sesion
    sesion = USER

    statusHome = verificacionLSiebel(driver)

    if statusHome == True:

        while status_logueo == True:
                
                #SI EL LOGEO FUE CORRECTO
                if status_logueo == True:
                    text_box('CUENTA DE: ' + sesion,'▬')


                    apiresponse = api.get_extraccion()
                    info = apiresponse[0]
                    print(info)
                    host = socket.gethostname()
                    ip = socket.gethostbyname(host)
                    if info != 'SIN INFO':
                        numeroOrden = info['numeroOrden']
                        numeroCuenta = info['cuenta']
                        motivoCliente = info['resultadoLlamada']
                        fechaCaptura = info['fechaCaptura']

                        fechaCaptura = fechaCaptura.replace("T", " ")
                        horaActual = datetime.now().time()
                        horaInicial = time(5,0,0)
                        horaFinal = time(6,0,0)

                        if horaActual >= horaInicial and horaActual <= horaFinal:
                            error = 'No Aplica Orden Fuera Horario'
                            print(error)
                            status = error                            
                            response = api.notDone_cerrado(info['id'], info['ciudad'], info['comentarios'], info['creadoPor'], info['cuenta'], info['direccion'], info['estadoOrden'], info['fechaApertura'], info['fechaSolicitada'], info['hub'], info['motivoCancelacion'], info['motivoOrden'], info['motivoReprogramacion'], info['nombreCliente'], info['numeroOrden'], info['numRepro'], info['paquete'], info['perfilPago'], info['plaza'], info['referido'], info['rpt'], info['situacionAnticipo'], info['subtipoCliente'], info['subtipoOrden'], info['tecnico'], info['telefono'], info['tipCliente'], info['tipoOrden'], info['ultimaModificacionPor'], info['vendedor'], info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '1', ip, '-', '-',info['resultadoLlamada'],'-')
                            print(response)
                        else:
                            print('ORden Dentro de horario')
                        
                            obtencion,errorOrden, tipoCN = ordenesServicio(driver, numeroOrden )
                            if obtencion == False:
                                if 'Pendiente' in errorOrden:
                                    status = errorOrden                            
                                    response = api.notDone_cerrado(info['id'], info['ciudad'], info['comentarios'], info['creadoPor'], info['cuenta'], info['direccion'], info['estadoOrden'], info['fechaApertura'], info['fechaSolicitada'], info['hub'], info['motivoCancelacion'], info['motivoOrden'], info['motivoReprogramacion'], info['nombreCliente'], info['numeroOrden'], info['numRepro'], info['paquete'], info['perfilPago'], info['plaza'], info['referido'], info['rpt'], info['situacionAnticipo'], info['subtipoCliente'], info['subtipoOrden'], info['tecnico'], info['telefono'], info['tipCliente'], info['tipoOrden'], info['ultimaModificacionPor'], info['vendedor'], info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '0', ip, '-', '-',info['resultadoLlamada'],tipoCN)
                                    print(response)
                                    driver.quit()
                                    return False
                                else:
                                    status = errorOrden                            
                                    response = api.notDone_cerrado(info['id'], info['ciudad'], info['comentarios'], info['creadoPor'], info['cuenta'], info['direccion'], info['estadoOrden'], info['fechaApertura'], info['fechaSolicitada'], info['hub'], info['motivoCancelacion'], info['motivoOrden'], info['motivoReprogramacion'], info['nombreCliente'], info['numeroOrden'], info['numRepro'], info['paquete'], info['perfilPago'], info['plaza'], info['referido'], info['rpt'], info['situacionAnticipo'], info['subtipoCliente'], info['subtipoOrden'], info['tecnico'], info['telefono'], info['tipCliente'], info['tipoOrden'], info['ultimaModificacionPor'], info['vendedor'], info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '0', ip, '-', '-',info['resultadoLlamada'],tipoCN)
                                    print(response)
                                    driver.quit()
                                    return False

                            else:
                                print('Orden validad')

                                obtencion, error, cnObtenido, statusCNO = generacionCasoNegocio(driver, tipoCN, numeroCuenta, motivoCliente)
                                if error == 'Error Cuenta no valida':
                                    status = 'Pendiente'                            
                                    response = api.notDone_cerrado(info['id'], info['ciudad'], info['comentarios'], info['creadoPor'], info['cuenta'], info['direccion'], info['estadoOrden'], info['fechaApertura'], info['fechaSolicitada'], info['hub'], info['motivoCancelacion'], info['motivoOrden'], info['motivoReprogramacion'], info['nombreCliente'], info['numeroOrden'], info['numRepro'], info['paquete'], info['perfilPago'], info['plaza'], info['referido'], info['rpt'], info['situacionAnticipo'], info['subtipoCliente'], info['subtipoOrden'], info['tecnico'], info['telefono'], info['tipCliente'], info['tipoOrden'], info['ultimaModificacionPor'], info['vendedor'], info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '0', ip, '-', '-',info['resultadoLlamada'],tipoCN)
                                    print(response)
                                    driver.quit()
                                    return False

                                elif obtencion == False:
                                    print('Fallo al generar caso de negocio')
                                    status = error                            
                                    response = api.notDone_cerrado(info['id'], info['ciudad'], info['comentarios'], info['creadoPor'], info['cuenta'], info['direccion'], info['estadoOrden'], info['fechaApertura'], info['fechaSolicitada'], info['hub'], info['motivoCancelacion'], info['motivoOrden'], info['motivoReprogramacion'], info['nombreCliente'], info['numeroOrden'], info['numRepro'], info['paquete'], info['perfilPago'], info['plaza'], info['referido'], info['rpt'], info['situacionAnticipo'], info['subtipoCliente'], info['subtipoOrden'], info['tecnico'], info['telefono'], info['tipCliente'], info['tipoOrden'], info['ultimaModificacionPor'], info['vendedor'], info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '1', ip, '-', '-',info['resultadoLlamada'],tipoCN)
                                    print(response)
                                    driver.quit()
                                    return False
                                else:
                                    print('Caso de Negocio generado con Exito')
                                    status = errorOrden
                                    statusCN = statusCNO
                                    nuevoCN = cnObtenido
                                    
                                    response = api.notDone_cerrado(info['id'], info['ciudad'], info['comentarios'], info['creadoPor'], info['cuenta'], info['direccion'], info['estadoOrden'], info['fechaApertura'], info['fechaSolicitada'], info['hub'], info['motivoCancelacion'], info['motivoOrden'], info['motivoReprogramacion'], info['nombreCliente'], info['numeroOrden'], info['numRepro'], info['paquete'], info['perfilPago'], info['plaza'], info['referido'], info['rpt'], info['situacionAnticipo'], info['subtipoCliente'], info['subtipoOrden'], info['tecnico'], info['telefono'], info['tipCliente'], info['tipoOrden'], info['ultimaModificacionPor'], info['vendedor'], info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '1', ip, nuevoCN, statusCN, info['resultadoLlamada'],tipoCN)
                                    print(response)



                    else:
                        try:
                            print('Esperando EXTRACCIONES')
                            sleep(15)
                            print('Regreso a HOME')
                            result = open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                            if result == False:
                                driver.quit()
                                return False
                            text_box('FIN DEL CICLO COMPLETO', '▬')
                            os.system('cls')
                        
                        except Exception:
                            driver.quit()
                            return False
    else:
        
        return False



while True == True:
    conteo_errores = 0
    # Buscamos todos los procesos de Google Chrome en ejecución
    try:
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
    except Exception as e:
        print(e)

    eliminar_archivos()
    error_main = __main__()
    while True == True:
        if error_main == False:

            try:
                os.system(f"taskkill /f /im chrome.exe")
                os.system(f"taskkill /f /im chrome.exe")
                os.system(f"taskkill /f /im chrome.exe")
                error_main = __main__()
            except Exception as e:
                print(e)