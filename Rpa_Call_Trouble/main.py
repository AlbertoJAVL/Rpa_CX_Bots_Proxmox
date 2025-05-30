from login import *
from ventanas import *

import os
import shutil
import socket
import Services.ApiCyberHubOrdenes as api

# driver, estatus = loginVISA('rpaajustes4.service','T3le4z21/f3VxFHM')

# val,val2 = busquedaCuenta(driver, '19598814', 'Trouble Call Cablemodem', 'Offline', 'Call Back Gestion sin contact Telefono 5612052420 Recibe Titular')
# # print(val2)
# generacionCN(driver, 'Trouble Call Cablemodem')
# sleep(10000)


def eliminar_archivos_temporales():
# Obtiene la ruta de la carpeta %temp%
    temp_folder = os.environ['TEMP']
    
    try:
        # Listar los archivos en la carpeta %temp%
        temp_files = os.listdir(temp_folder)

        # Eliminar solo los archivos que no están siendo utilizados por otros procesos
        for temp_file in temp_files:
            temp_file_path = os.path.join(temp_folder, temp_file)
            try:
                # Intentar eliminar el archivo
                if os.path.isfile(temp_file_path):
                    os.remove(temp_file_path)
                elif os.path.isdir(temp_file_path):
                    shutil.rmtree(temp_file_path)  # Si es un directorio, elimínalo recursivamente
            except Exception as e:
                print(f"No se pudo eliminar {temp_file}: {str(e)}")

        print("Archivos no utilizados eliminados correctamente en la carpeta %temp%.")

    except Exception as e:
        print(f"Se produjo un error al eliminar archivos en la carpeta %temp%: {str(e)}")



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
        return False
    
    while status_logueo == True:

        apiresponse = api.get_orden_servicio()
        info = apiresponse[0]
        print(info)

        host = socket.gethostname()
        ip = socket.gethostbyname(host)

        if info != 'SIN INFO':

            sleep(5)


            validador, resultado, numeroOrden = busquedaCuenta(driver, info['cuenta'], 'Trouble Call Cablemodem', 'Offline', 'Call Back Gestion sin contact Telefono 5612052420 Recibe Titular')

            if 'Error' in resultado:
                print(resultado)
                
                status = resultado
                if 'Error Pantalla NO Carga' in resultado: status = 'Pendiente' 
                
                response = api.ajusteCerrado(
                                                info['id'], 
                                                numeroOrden, 
                                                info['fechaCaptura'], 
                                                info['fechaCompletado'], 
                                                status, 
                                                info['cve_usuario'], 
                                                '0', 
                                                info['cuenta'], 
                                                info['tipo'], 
                                                info['motivo'], 
                                                info['comentarios'], 
                                                '-')
                
                return False

            else:
                
                validador, resultado, numeroCN = generacionCN(driver, 'Trouble Call Cablemodem')

                print(resultado)
                
                status = resultado                
                response = api.ajusteCerrado(
                                                info['id'], 
                                                numeroOrden, 
                                                info['fechaCaptura'], 
                                                info['fechaCompletado'], 
                                                status, 
                                                info['cve_usuario'], 
                                                '0', 
                                                info['cuenta'], 
                                                info['tipo'], 
                                                info['motivo'], 
                                                info['comentarios'], 
                                                numeroCN)
                
                if 'Error' in resultado: return False
                
        
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


