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

# USER = "rpaajustes.service"
# PASS = 'mpCtP6xnZZS9Cx8/'

USER = "rpaajustes1.service"
PASS = "utBiJslALlIPZ4M/"
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
        apiresponseTiempo = api.get_tiempo_ajuste()
        meses = apiresponseTiempo[0]
        meses = meses['valor']
        meses = meses.replace(' meses', '')

        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        #<button type="button" class="siebui-ctrl-btn appletButton siebui-icon-newquery s_2_1_13_0" id="s_2_1_13_0_Ctrl" name="s_2_1_13_0" data-display="Consulta" tabindex="0" title="Casos de negocio Applet de lista:Consulta" aria-label="Casos de negocio Applet de lista:Consulta"><span>Consulta</span></button>

        if info != 'SIN INFO':
            response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],'Procesando', '0', ip, '', '', '','', info['prioridad'])
            casoNegocio = info['casoNegocio']
            no_cuenta = info['cuenta']

            sleep(5)

            resultadoValidacionCuenta, error,ajuste, promocion = validacion_cuenta_convenio_cobranza(driver,no_cuenta, casoNegocio,meses)
            print('Validacion de cuenta completa')
            if resultadoValidacionCuenta == False:
                if 'Error Pantalla Unica' in error:
                    print(error)
                    status = 'Registro pendiente'
                    response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '0', ip, '', '', '','', info['prioridad'])
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                else:
                    print(error)
                    status = error 
                    response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, '', '', '','', info['prioridad'])
                    print(response)
                    driver.close()
                    driver.quit()
                    return False

            else:
                resultadoAplicacionAjuste, error, numAjuste, estatusAjuste = aplicacionAjuste(driver, ajuste, promocion)
                print('Aplicacion de Ajuste completa')
                if resultadoAplicacionAjuste == False:
                    print(error)
                    status = error
                    response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, '', '', '',estatusAjuste, info['prioridad'])
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                else:
                    resultadoCreacionCN, error, cnGenerado = generacionCN(driver, casoNegocio, ajuste)
                    print('Creacion de nuevo caso de negocio, completa')
                    if resultadoCreacionCN == False:
                        print('Falla al crear el caso de negocio')
                        status = 'Error al Crear CN'
                        response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, numAjuste, '', '',estatusAjuste, info['prioridad'])
                        print(response)
                        driver.close()
                        driver.quit()
                        return False
                    else:
                        print('Ajuste Completado')
                        status = 'Aplicación correcta'
                        response = api.ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],status, '1', ip, numAjuste, cnGenerado, 'Cerrado',estatusAjuste, info['prioridad'])
                        print(response)

        else:
            try:
                # os.system('cls')
                print('Esperando mas Ajustes')
                sleep(15)
                print('Regreso a HOME')
                result = open_item_selenium_wait(driver, xpath = home['home_from_sidebar']['xpath'])
                if result == False:
                    driver.close()
                    driver.quit()
                    return False
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


