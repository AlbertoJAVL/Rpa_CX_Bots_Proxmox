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
    #Inicio de sesion
    response = api.get_data_user2()
    USER = response['procesoUser'] 
    PASS = response['procesoPassword'] 

    driver, status_logueo = login_siebel(USER, PASS)
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

                        tExtraccion = info['tipoExtraccion']

                        datosSR = info['parametrosExtraccion']
                        datos = separacionParametrosExtraccion(datosSR, tExtraccion)

                        '''▬▬▬▬▬▬▬▬▬▬▬▬ OEXTRACCIONES ▬▬▬▬▬▬▬▬▬▬▬▬'''

                        driver2 = pantalla_extracion(driver, datos, tExtraccion)
                        estatus, nArchivo = extracion(driver, tExtraccion)

                        if estatus == True:
                            try:
                                sleep(10)
                                print('Click sobre btn CERRAR')
                                driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[3]/button').click()

                                print('Regreso a HOME')
                                open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                                text_box('FIN DEL CICLO COMPLETO', '▬')

                                status = 'Completado'
                                response = api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], nArchivo, info['cve_usuario'], info['fechaInicial'], info['fechaFinal'], info['fechaCompletado'], status, info['procesando'], ip)
                                print(response)


                            except Exception:
                                return False
                        
                        else:
                            try:
                                print('Regreso a HOME')
                                open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                                text_box('FIN DEL CICLO COMPLETO', '▬')

                                status = nArchivo
                                response = api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaInicial'], info['fechaFinal'], info['fechaCompletado'], status, info['procesando'], ip)
                                print(response)
                                return False

                            except Exception:
                                return False

                    else:
                        try:
                            print('Esperando EXTRACCIONES')
                            sleep(15)
                            print('Regreso a HOME')
                            open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
                            text_box('FIN DEL CICLO COMPLETO', '▬')
                        
                        except Exception:
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

