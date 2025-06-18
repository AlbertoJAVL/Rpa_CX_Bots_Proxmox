#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import re

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
from eliminar_archivos_temporales import eliminar_archivos_temporales
#---------Variables globales---------------#

# USER = "TSTCALLCENTER"
# PASS = 'TSTCALLCENTeR_2023'

USER = "rpanotdone5.service"
PASS = 'HaJUwkuhpmO5Bjv/'
FINALIZADO_ERROR = 'FLUJO FINALIZADO CON ERROR'



def workflow(user = USER, password = PASS):
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
        # info = 'CON INFO'
        print(info)

        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        # no_cuenta = '34708260'
        # prueba(driver, no_cuenta)
        # sleep(1000)
        



        if info != 'SIN INFO':
            
            # cn = '1161582194381'
            # no_cuenta = '34655713'

            sleep(5)

            resultadoValidacionCuenta, error, promocionCliente = validacion_cuenta_retencion(driver, info['cuenta'], info['casoNegocio'])
            print('Validacion de cuenta completa')
            if resultadoValidacionCuenta == False:

                if error in ['Error Falla Penalizacion', 'Error Regreso Pantalla Unica', 'Error Pantalla Unica', 'Error Validaciones']:
                    resultadoValidacionCuenta, error, promocionCliente = validacion_cuenta_retencion(driver, info['cuenta'], info['casoNegocio'])

                    if error in ['Error Validaciones', 'Error Cuenta no valida']:
                        print(error)
                        status = 'Pendiente' 
                        response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '0', ip, '', '', '', '')
                        print(response)
                        driver.close()
                        driver.quit()
                        return False

                    elif resultadoValidacionCuenta == False:

                        print(error)
                        status = error 
                        response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, '', '', '', '')
                        print(response)
                        cierreActividad(driver, False)
                        driver.close()
                        driver.quit()
                        return False

                    else:
                        resultadoAplicacionAjuste, error, osGenerada, estatusOS  = terminoPromocion(driver, promocionCliente)
                        if resultadoAplicacionAjuste == False:
                            print(error)
                            status = error
                            response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, osGenerada, '', '', estatusOS)
                            print(response)
                            driver.close()
                            driver.quit()
                            return False
                        else:
                            resultadoCreacionCN, error, cnGenerado = cierreActividad(driver, info['cuenta'])
                            print('Creacion de nuevo caso de negocio, completa')
                            if resultadoCreacionCN == False:
                                print('Falla al crear el caso de negocio')
                                status = 'Error Crear CN'
                                response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, osGenerada, cnGenerado, 'Open', estatusOS)
                                print(response)
                                driver.close()
                                driver.quit()
                                return False
                            else:
                                print('Ajuste Completado')
                                status = 'CN Cerrado'
                                response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, osGenerada, cnGenerado, 'Cerrado', estatusOS)
                                print(response)

                elif error in ['Error Validaciones', 'Error Cuenta no valida']:
                    print(error)
                    status = 'Pendiente' 
                    response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '0', ip, '', '', '', '')
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                else:
                    print(error)
                    status = error 
                    response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, '', '', '', '')
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                    # cierreActividad(driver, False)
            else:
                resultadoAplicacionAjuste, error, osGenerada, estatusOS = terminoPromocion(driver, promocionCliente)
                if resultadoAplicacionAjuste == False:
                    print(error)
                    status = error           
                    response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, osGenerada, '', '', estatusOS)
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                else:
                    resultadoCreacionCN, error, cnGenerado = cierreActividad(driver, info['cuenta'])
                    print('Creacion de nuevo caso de negocio, completa')
                    if resultadoCreacionCN == False:
                        print('Falla al crear el caso de negocio')
                        status = 'Error Crear CN'
                        response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, osGenerada, cnGenerado, 'Open', estatusOS)
                        print(response)
                        driver.close()
                        driver.quit()
                        return False
                        
                    else:
                        print('Ajuste Completado')
                        status = 'CN Cerrado'
                        response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, osGenerada, cnGenerado, 'Cerrado', estatusOS)
                        print(response)


                
        
        else:
            try:
                # os.system('cls')
                print('Esperando mas Ajustes')
                sleep(15)
                print('Regreso a HOME')
                open_item_selenium_wait(driver, xpath = home['home_from_sidebar']['xpath'])
                text_box('FIN EL CICLO COMPLETO', '-')
                os.system('cls')
                
            except Exception:
                driver.close()
                driver.quit()
                return False
                


#██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
while True == True:
    conteo_errores = 0
    # # Buscamos todos los procesos de Google Chrome en ejecución
    try:
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
    except Exception as e:
        pass

    eliminar_archivos_temporales()

    error_main = workflow()
    if error_main == False:
        conteo_errores = conteo_errores + 1
        print('conteo_errores::: ', conteo_errores)
        if conteo_errores >= 5:
            os.system(f"taskkill /f /im chrome.exe")
            error_main = workflow()
            text_box ('ERROR CRITICO, REVISAR', '¶¶')
            sleep(1)


