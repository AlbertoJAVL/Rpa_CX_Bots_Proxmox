from os import environ, path, remove, listdir
import apiCyberHubOrdenes as api
from login import loginSiebel
from shutil import rmtree
from funcionalidad import *
import socket
import os

def delTemporales():

    temp_folder = environ['TEMP']

    try:

        temp_files = listdir(temp_folder)

        for temp_file in temp_files:
            temp_file_path = path.join(temp_folder, temp_file)

            try:
                if path.isfile(temp_file_path): remove(temp_file_path)
                elif path.isdir(temp_file_path): rmtree(temp_file_path)

            except: pass

        print('Eliminacion temporales OK!')

    except Exception as e: print('Se produjo un error al eliminar los temporales')




def main():

    # Eliminación de Temporales
    
    delTemporales()

    # Inicio de Sesion
    driver, status_logueo = loginSiebel('omartinezhu', 'Loquesea17#44')
    if status_logueo == False: 
        print('→ LOGGIN INCORRECTO ←')
        driver.close()
        driver.quit()
        return False

    while True:

        apiResponse = api.get_orden_servicio()
        info = apiResponse[0]
        print(info)
        host = socket.gethostname()
        ip = socket.gethostbyname(host)

        if info != 'SIN INFO':

            nombre = info['nombre']
            telefono = info['telefono']
            comentario = f'Contesta {nombre} Tel {telefono} confirma servicio ok'
            resultado = inicio(driver, info['cuenta'], comentario, info['numeroOrden'])
            
            if 'Error' in resultado or 'No aplica' in resultado:
                status = resultado
                if 'Error FInicio' in resultado: status = 'Registro Pendiente'
                response = api.ajusteCerrado(info['id'],resultado,info['fechaCaptura'],info['fechaCompletado'],status,info['cve_usuario'],ip,info['cuenta'],info['numeroOrden'], info['hub'], info['tipoOferta'], info['fechaEncuesta'], info['nombre'], info['telefono'])
                print(response)
                driver.close()
                driver.quit()
                return False
            else:
                resultado2 = cierreOS(driver, info['numeroOrden'])
                if 'Error' in resultado2:
                    status = resultado2
                    response = api.ajusteCerrado(info['id'],resultado,info['fechaCaptura'],info['fechaCompletado'],status,info['cve_usuario'],ip,info['cuenta'],info['numeroOrden'], info['hub'], info['tipoOferta'], info['fechaEncuesta'], info['nombre'], info['telefono'])
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                else:
                    status = 'Cerrado'
                    response = api.ajusteCerrado(info['id'],resultado,info['fechaCaptura'],info['fechaCompletado'],status,info['cve_usuario'],ip,info['cuenta'],info['numeroOrden'], info['hub'], info['tipoOferta'], info['fechaEncuesta'], info['nombre'], info['telefono'])
                    print(response)

        else:
            try:
                os.system('cls')
                print('Esperando mas CN')
                sleep(15)
                print('Regreso a HOME')
                home2(driver)
                print('##############\n FIN DE CICLO COMPLETO \n##############')

            except Exception: 
                driver.close()
                driver.quit()
                return False


while True == True:
    conteo_errores = 0
    try:
        os.system(f'taskkill /f /im chrome.exe')
        os.system(f'taskkill /f /im chrome.exe')
        os.system(f'taskkill /f /im chrome.exe')

    except Exception as e: pass

    delTemporales()

    error_main = main()
    if error_main == False:
        conteo_errores = conteo_errores + 1
        print(f'conteo_errores::: {str(conteo_errores)}')
        if conteo_errores >= 5:
            # os.system(f'taskkill /f /im chrome.exe')
            error_main = main()
            print('##################\n ERROR CRITICO \n##################')
            sleep(1)
