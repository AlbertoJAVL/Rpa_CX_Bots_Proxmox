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
        open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
        return True
    
    except Exception:
        return False

def __main__():
    '''
    Funcion encargada de hacer el flujo completo del bot

    '''
    response = api.get_user()
    user = response['procesoUser']
    password = response['procesoPassword']

    #Inicio de sesion
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

                        numeroCuenta = info['cuenta'].strip()
                        categoria = info['categoria'].strip()
                        motivos = info['motivos'].strip()
                        subMotivo = info['submotivos'].strip()
                        solucion = info['solucion'].strip()
                        motivoCliente = info['motivoCliente'].strip()
                        comentarios = info['comentarios'].strip()
                        estado = info['estado'].strip()

                        if len(motivoCliente) == 0:
                            status = 'Error Sin Motivo Cliente'
                            response = api.notDone_cerrado('-', info['id'], info['cuenta'], info['categoria'], info['motivos'], info['submotivos'], info['solucion'], info['motivoCliente'],info['comentarios'],info['estado'],info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '1', ip)
                            print(response)
                        else:

                            obtencion, error, cnObtenido = generacionCasoNegocio(driver, numeroCuenta, categoria, motivos, subMotivo, solucion,comentarios , motivoCliente,estado)
                            if obtencion == False:
                                print('Fallo al generar caso de negocio')
                                status = error                            
                                response = api.notDone_cerrado('-', info['id'], info['cuenta'], info['categoria'], info['motivos'], info['submotivos'], info['solucion'], info['motivoCliente'],info['comentarios'],info['estado'],info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '1', ip)
                                print(response)
                                if 'Warning' in error:
                                    driver.close()
                                    driver.quit()
                                    return False
                            else:
                                print('Caso de Negocio generado con Exito')
                                status = 'Cerrado'
                                nuevoCN = cnObtenido
                                response = api.notDone_cerrado(nuevoCN, info['id'], info['cuenta'], info['categoria'], info['motivos'], info['submotivos'], info['solucion'], info['motivoCliente'],info['comentarios'],info['estado'],info['cve_usuario'], info['fechaCompletado'], info['fechaCaptura'], status, '1', ip)
                                print(response)


                    else:
                        try:
                            print('Esperando Generacion de CN')
                            sleep(15)
                            print('Regreso a HOME')
                            open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                            text_box('FIN DEL CICLO COMPLETO', '▬')
                            os.system('cls')
                        
                        except Exception:
                            driver.close()
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
        pass

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
                pass
            

        else:
            pass

    # if error_main == False:
    #     conteo_errores = conteo_errores + 1
    #     print('conteo_errores::: ', conteo_errores)
    #     if conteo_errores >= 5:
    #         text_box ('ERROR CRITICO, REVISAR', '¶¶')
    #         sleep(10000)

