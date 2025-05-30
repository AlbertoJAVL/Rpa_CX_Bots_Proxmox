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
from datetime import datetime

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

# USER = "apiliado"
# PASS = 'Cafeconleche.2023'

# USER = "rbernal"
# PASS = 'Proyectos.0523'

# USER = "mgonzalezd"
# PASS = "Gr@ciaaas.D105"
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

    print('Iniciando Sesion')
    driver, status_logueo = login_siebel(USER, PASS)
    global sesion
    sesion = USER

    sleep(10)
    statusHome = verificacionLSiebel(driver)
    print('Verificacion completa')

    if statusHome == True:

        while status_logueo == True:

            apiresponse = api.get_extraccion()
            info = apiresponse[0]
            print(info)
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            status = 'Procesando'

            if info != 'SIN INFO':

                response = api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], status, '', info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 10)
                datosExtraccion = info['parametrosExtraccion']
                tExtraccion = info['tipoExtraccion']
                diasVencidos = info['tipoProgramacion']
                viaExtraccion = info['medioExtraccion']
                correo = info['correo']
                fechaFijaConsecutiva = False

                if '1' in diasVencidos:
                    fechaFijaConsecutiva = True

                datos = separacionParametrosExtraccion(datosExtraccion, tExtraccion)

                '''▬▬▬▬▬▬▬▬▬▬▬▬ OEXTRACCIONES ▬▬▬▬▬▬▬▬▬▬▬▬'''

                contador = 0
                extrayendo = True

                while extrayendo == True:


                    validacionRes, validacion = pantalla_extracion(driver, datos, tExtraccion, fechaFijaConsecutiva, viaExtraccion)
                    if validacion == True:
                        estatus, nArchivo, error = extracion(driver, tExtraccion, viaExtraccion, correo, info, ip)

                        if estatus == True:
                            sleep(10)
                            status = 'Completado'
                            response = api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], nArchivo, info['cve_usuario'], info['fechaCompletado'], status, ip, info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 100)
                            print(response)
                            sleep(1)
                            
                            print('Click sobre btn CERRAR')    

                            driver.find_element(By.XPATH, "//button[@aria-label='Exportar Applet de formulario:Cerrar']").click()
                            sleep(10)

                            os.system(f"taskkill /f /im chrome.exe")
                            os.system(f"taskkill /f /im chrome.exe")
                            os.system(f"taskkill /f /im chrome.exe")

                            print('Regreso a HOME')
                            # casosNegocio = busquedaExtraccion(driver, 'Página inicial')
                            # driver.find_element(By.XPATH, nuvasRutas['exportaciones'].replace('{contador}', casosNegocio)).click()
                            text_box('FIN DEL CICLO COMPLETO', '▬')
                            sleep(10)
                            # sleep(3600)
                            extrayendo = False
                            return True

                        else:

                            contador += 1
                            if contador == 3:

                                try:

                                    status = error
                                    response = api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], status, ip, info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 0)
                                    print(response)

                                    os.system(f"taskkill /f /im chrome.exe")
                                    os.system(f"taskkill /f /im chrome.exe")
                                    os.system(f"taskkill /f /im chrome.exe")

                                    sleep(10)
                                    extrayendo = False
                                    return True

                                except Exception:
                                    return False
                            else:
                                print('Click sobre btn CERRAR')    

                                driver.find_element(By.XPATH, "//button[@aria-label='Exportar Applet de formulario:Cerrar']").click()
                                sleep(10)
                                driver.find_element(By.XPATH, "//a[@title='Página inicial']").click()
                                sleep(10)
                    else:
                        try:
                            if 'true' in viaExtraccion:
                                driver.find_element(By.XPATH, "//div[@ot='Link']").click()
                                sleep(4)
                        except:
                            os.system(f"taskkill /f /im chrome.exe")
                            os.system(f"taskkill /f /im chrome.exe")
                            os.system(f"taskkill /f /im chrome.exe")
                            driver, status_logueo = login_siebel(USER, PASS)

                            sleep(10)
                            statusHome = verificacionLSiebel(driver)
                            print('Verificacion completa')

                        driver.find_element(By.XPATH, "//a[@title='Página inicial']").click()
                        sleep(10)
                        contador += 1
                        if contador == 3:
                            status = validacionRes
                            response = api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], status, ip, info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 0)
                            print(response)
                            extrayendo = False
                            return False
            
            else:
                try:
                    print('Esperando mas Ajuste')
                    sleep(15)
                    print('Regreso a HOME')
                    result = open_item_selenium_wait(driver, xpath= home['home_from_sidebar']['xpath'])
                    if result == False:
                        return False
                    text_box('FIN CICLO COMPLETO', '-')
                    os.system('cls')
                except Exception:
                    return False
    else:
        
        return False



while True == True:
    
    conteo_errores = 0

    try:

        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")
        os.system(f"taskkill /f /im chrome.exe")

    except Exception as e:
        pass
    
    eliminar_archivos()
    
    error_main = __main__()
    if error_main == False:
        conteo_errores = conteo_errores + 1
        print('conteo_errores::: ', conteo_errores)
        if conteo_errores >= 5:
            os.system(f"taskkill /f /im chrome.exe")
            error_main = __main__()
            text_box('ERROR CRITICO, REVISAR', '>>')
            sleep(1)


    # try:
    #     datos = api.get_extraccion()

    #     for x in datos:
    #         datos = x
    #         horario = datos['horaProgramacion']
    #         datosExtraccion = datos['parametrosExtraccion']
    #         tExtraccion = datos['tipoExtraccion']
    #         horario = datetime.datetime.strptime(horario, '%H:%M:%S').time()
    #         timeActual = datetime.datetime.now()


            
    #         hrActual = timeActual.hour
    #         horaEjecucion  = horario.hour
    #         print(horario)
    #         print(timeActual)

    #         minActual = timeActual.minute
    #         minEjecucion = horario.minute

    #         if hrActual == horaEjecucion and minActual == minEjecucion:
    #         # if hrActual == horaEjecucion:
    #             print('Horar coincidencia')
    #             print('hora de extraccion : ', str(horaEjecucion))
    #             print('datosExtraccion: ', str(datosExtraccion))
    #             print('tipo Extraccion: ', str(tExtraccion))
    #             error_main = __main__(str(horario), datosExtraccion, tExtraccion, datos)
                
    #             if error_main == False:
    #                 try:
    #                     os.system(f"taskkill /f /im chrome.exe")
    #                     os.system(f"taskkill /f /im chrome.exe")
    #                     os.system(f"taskkill /f /im chrome.exe")
    #                 except:
    #                     pass
                        
    #                 os.system(f"taskkill /f /im chrome.exe")
    #                 os.system(f"taskkill /f /im chrome.exe")
    #                 os.system(f"taskkill /f /im chrome.exe")

    #                 error_main = __main__(str(horario), datosExtraccion, tExtraccion, datos)
                
    #         else:

    #             print('> HORARIO NO CORRESPONDE <')
    #             sleep(5)
    #             os.system('cls')
    # except Exception as e:
    #     print(e)
    #     __main__(str(horario), datosExtraccion, tExtraccion, datos)
