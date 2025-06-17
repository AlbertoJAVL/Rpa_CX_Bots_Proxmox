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
import datetime 
import ftplib
import pandas as pd

#---------Mis funciones---------------#


from utileria import *
from logueo import *
from rutas import *

from myFunctions import  AlertaSaldoVencido

def separacionParametrosExtraccion(datos, tExtraccion):

    datosF = datos.replace('[{', '')
    datosF = datosF.replace('}]', '')

    # print(datosF)
    
    parametrosExtraccion = datosF.split(',')
    # print(parametrosExtraccion)

    # for x in parametrosExtraccion:
    #     print(x)
    
    if 'Cuenta' in tExtraccion:
        
        estatus = parametrosExtraccion[0].split('"estado":')
        estatus = estatus[1]
        tipo = parametrosExtraccion[1].split('"tipo":')
        tipo = tipo[1]
        subTipo = parametrosExtraccion[2].split('"subTipo":')
        subTipo = subTipo[1]

        parametrosFinales = {
            'estatus':estatus,
            'tipo':tipo,
            'subTipo':subTipo
        }

        return parametrosFinales

    elif 'Casos de negocio' in tExtraccion:

        estado = parametrosExtraccion[0].split('"estado":')
        estado = estado[1]
        numCaso = parametrosExtraccion[1].split('"numCaso":')
        numCaso = numCaso[1]
        cuenta = parametrosExtraccion[2].split('"cuenta":')
        cuenta = cuenta[1]
        categoria = parametrosExtraccion[3].split('"categoria":')
        categoria = categoria[1]
        motivo = parametrosExtraccion[4].split('"motivo":')
        motivo = motivo[1]
        subMotivo = parametrosExtraccion[5].split('"subMotivo":')
        subMotivo = subMotivo[1]
        solucion = parametrosExtraccion[6].split('"solucion":')
        solucion = solucion[1]

        parametrosFinales = {
            'estado':estado,
            'numCaso':numCaso,
            'cuenta':cuenta,
            'categoria':categoria,
            'motivo':motivo,
            'subMotivo':subMotivo,
            'solucion':solucion
        }

        return parametrosFinales

    elif 'Actividades' in tExtraccion:

        estado = parametrosExtraccion[0].split('"estado":')
        print(estado)
        estado = estado[1]
        areaConocimiento = parametrosExtraccion[1].split('"areaConocimiento":')
        areaConocimiento = areaConocimiento[1]
        fechaAsignacion = parametrosExtraccion[2].split('"fechaAsignacion":')
        fechaAsignacion = fechaAsignacion[1]
        fechaAsignacion = fechaAsignacion.replace('"','')

        parametrosFinales = {
            'estado':estado,
            'areaConocimiento':areaConocimiento,
            'fechaAsignacion':fechaAsignacion
        }

        return parametrosFinales

    elif 'Ordenes de servicio' in tExtraccion:

        estado = parametrosExtraccion[0].split('"estado":')
        estado = estado[1]
        tipoOrden = parametrosExtraccion[1].split('"tipoOrden":')
        tipoOrden = tipoOrden[1]
        tipoOrden = tipoOrden[1:-1]
        # print(tipoOrden)

        motivo = parametrosExtraccion[2].split('"motivo":')
        motivo = motivo[1]
        areaConocimiento = parametrosExtraccion[3].split('"areaConocimiento":')
        areaConocimiento = areaConocimiento[1]
        fechaAsignacion = parametrosExtraccion[4].split('"fechaAsignacion":')
        fechaAsignacion = fechaAsignacion[1]
        fechaAsignacion = fechaAsignacion.replace('"', '')

        parametrosFinales = {
            'estado':estado,
            'tipoOrden':tipoOrden,
            'motivo':motivo,
            'areaConocimiento':areaConocimiento,
            'fechaAsignacion':fechaAsignacion
        }
        # print(parametrosFinales)

        return parametrosFinales


def extCuentas(driver, datos):

    print('Fun Extraccion Cuentas')
    wait = WebDriverWait(driver,120)

    #Extraccion de Datos por cuentas
    open_item_selenium_wait(driver, xpath = extraccionCuentas['cuentas'])

    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('Cuentas'))

    #LUPA DE BUSQUEDA
    status_open = open_item_selenium_wait(driver, id=extraccionCuentas['lupa']['id'],name=extraccionCuentas['lupa']['name'], xpath=extraccionCuentas['lupa']['xpath'])
    if status_open == False:
        description_error('03','pantalla_extraccion','No se encontró la lupa de búsqueda')
        return status_open

    #Elemento Estatus
    open_item_selenium_wait(driver, id = extraccionCuentas['status']['elemento'])

    #Click input Estatus
    open_item_selenium_wait(driver, id = extraccionCuentas['status']['input'])

    estatus = wait.until(EC.element_to_be_clickable((By.ID, extraccionCuentas['status']['input'])))
    estatus.send_keys(datos['estado']) #Ingresa el estatus

    #Elemento Tipo
    open_item_selenium_wait(driver, id = extraccionCuentas['tipo']['elemento'])

    #Click input Tipo
    open_item_selenium_wait(driver, id = extraccionCuentas['tipo']['input'])

    tipo = wait.until(EC.element_to_be_clickable((By.ID, extraccionCuentas['tipo']['input'])))
    tipo.send_keys(datos['tipo']) #Ingresa el tipo

    #Elemento Sub-Tipo
    open_item_selenium_wait(driver, id = extraccionCuentas['subTipo']['elemento'])

    #Click input Sub-Tipo
    open_item_selenium_wait(driver, id = extraccionCuentas['subTipo']['input'])

    subTipo = wait.until(EC.element_to_be_clickable((By.ID, extraccionCuentas['subTipo']['input'])))
    subTipo.send_keys(datos['subtipo']) #Ingresa el sub tipo
    subTipo.send_keys(Keys.RETURN) 
    subTipo.send_keys(Keys.RETURN)     #Enter
    sleep(10)

def extCasosNegocio(driver, datos):
    print('Fun Extraccion Cuentas')
    wait = WebDriverWait(driver,120)

    #Extraccion de Datos por cuentas
    open_item_selenium_wait(driver, xpath = extraccionCN['cn'])

    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('Negocio'))

    #LUPA DE BUSQUEDA
    status_open = open_item_selenium_wait(driver, id=extraccionCN['lupa']['id'],name =extraccionCN['lupa']['name'], xpath=extraccionCN['lupa']['xpath'])
    if status_open == False:
        description_error('03','pantalla_extraccion','No se encontró la lupa de búsqueda')
        return status_open

    #Input Caso de Negocio
    open_item_selenium_wait(driver, id = extraccionCN['inputCN'])

    cN = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['inputCN'])))
    cN.send_keys(datos['numCaso']) #Ingresa el Caso de Negocios

    #Elemento Cuenta
    open_item_selenium_wait(driver, id = extraccionCN['cuenta']['elemento'])

    #Click input Cuenta
    open_item_selenium_wait(driver, id = extraccionCN['cuenta']['input'])

    cuenta = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['cuenta']['input'])))
    cuenta.send_keys(datos['cuenta']) #Ingresa el cuenta

    #Elemento Estado
    open_item_selenium_wait(driver, id = extraccionCN['estado']['elemento'])

    #Click input Estado
    open_item_selenium_wait(driver, id = extraccionCN['estado']['input'])

    estado = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['estado']['input'])))
    estado.send_keys(datos['estado']) #Ingresa el estado

    #Elemento Categoria
    open_item_selenium_wait(driver, id = extraccionCN['categoria']['elemento'])

    #Click input Categoria
    open_item_selenium_wait(driver, id = extraccionCN['categoria']['input'])

    categoria = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['categoria']['input'])))
    categoria.send_keys(datos['categoria']) #Ingresa la categoria

    #Elemento Motivo
    open_item_selenium_wait(driver, id = extraccionCN['motivo']['elemento'])

    #Click input Motivo
    open_item_selenium_wait(driver, id = extraccionCN['motivo']['input'])

    motivo = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['motivo']['input'])))
    motivo.send_keys(datos['motivo']) #Ingresa el motivo

    #Elemento Sub Motivo
    open_item_selenium_wait(driver, id = extraccionCN['subMotivo']['elemento'])

    #Click input Sub Motivo
    open_item_selenium_wait(driver, id = extraccionCN['subMotivo']['input'])

    sMotivo = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['subMotivo']['input'])))
    sMotivo.send_keys(datos['subMotivo']) #Ingresa el sub motivo

    #Elemento Solucion
    open_item_selenium_wait(driver, id = extraccionCN['solucion']['elemento'])

    #Click input Solucion
    open_item_selenium_wait(driver, id = extraccionCN['solucion']['input'])

    solucion = wait.until(EC.element_to_be_clickable((By.ID, extraccionCN['subMsolucionotivo']['input'])))
    solucion.send_keys(datos['solucion']) #Ingresa la solucion
    solucion.send_keys(Keys.RETURN)     #Enter
    solucion.send_keys(Keys.RETURN)     #Enter

def extActividades(driver, datos):
    print('Fun Extraccion Cuentas')
    wait = WebDriverWait(driver,120)

    #Extraccion de Datos por cuentas
    open_item_selenium_wait(driver, xpath = extraccionactividades['actividades'])

    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('Actividades'))

    #LUPA DE BUSQUEDA
    status_open = open_item_selenium_wait(driver, id=extraccionactividades['lupa']['id'],name =extraccionactividades['lupa']['name'], xpath=extraccionactividades['lupa']['xpath'])
    if status_open == False:
        description_error('03','pantalla_extraccion','No se encontró la lupa de búsqueda')
        return status_open

    #Elemento Estatus
    open_item_selenium_wait(driver, id = extraccionactividades['estatus']['elemento'])

    #Click input Estatus
    open_item_selenium_wait(driver, id = extraccionactividades['estatus']['input'])

    estatus = wait.until(EC.element_to_be_clickable((By.ID, extraccionactividades['estatus']['input'])))
    estatus.send_keys(datos['estado']) #Ingresa el estatus

    #Elemento area de conocimiento
    open_item_selenium(driver, id=extraccionactividades['areaCon']['elemento'])

    #Click input area de conocimiento
    open_item_selenium_wait(driver, id = extraccionactividades['areaCon']['input'])

    aConocimiento = wait.until(EC.element_to_be_clickable((By.ID, extraccionactividades['areaCon']['input'])))
    aConocimiento.send_keys(datos['areaConocimiento']) #Ingresa el area de conocimiento

    #Elemento fecha Asignacion
    open_item_selenium_wait(driver, id = extraccionactividades['fAtencion']['elemento'])

    #Click input fecha Asignacion
    open_item_selenium_wait(driver, id = extraccionactividades['fAtencion']['input'])

    fAsignacion = wait.until(EC.element_to_be_clickable((By.ID, extraccionactividades['fAtencion']['input'])))
    fAsignacion.send_keys(datos['fechaAsignacion']) #Ingresa el fecha Asignacion
    fAsignacion.send_keys(Keys.RETURN)     #Enter

def extOrdeneServicio(driver, datos):
    print('Fun Extraccion Ordenes servicio')
    wait = WebDriverWait(driver,120)

    #Extraccion de Datos por cuentas
    open_item_selenium_wait(driver, xpath = extraccionOS['OS'])

    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('Ordenes'))

    #LUPA DE BUSQUEDA
    status_open = open_item_selenium_wait(driver, id=extraccionOS['lupa']['id'],name =extraccionOS['lupa']['name'], xpath=extraccionOS['lupa']['xpath'])
    if status_open == False:
        description_error('03','pantalla_extraccion','No se encontró la lupa de búsqueda')
        return status_open

    #Elemento tipo de orden
    open_item_selenium_wait(driver, id = extraccionOS['tOrden']['elemento'])

    #Click input tipo de orden
    open_item_selenium_wait(driver, id = extraccionOS['tOrden']['input'])

    tOrden = wait.until(EC.element_to_be_clickable((By.ID, extraccionOS['tOrden']['input'])))
    tOrden.send_keys(datos['tipoOrden']) #Ingresa el tipo de orden

    #Elemento Motivo
    open_item_selenium_wait(driver, id = extraccionOS['motivo']['elemento'])

    #Click input Motivo
    open_item_selenium_wait(driver, id = extraccionOS['motivo']['input'])

    motivo = wait.until(EC.element_to_be_clickable((By.ID, extraccionOS['motivo']['input'])))
    motivo.send_keys(datos['motivo']) #Ingresa el Motivo

    #Elemento Estado
    open_item_selenium_wait(driver, id = extraccionOS['estado']['elemento'])

    #Click input Estado
    open_item_selenium_wait(driver, id = extraccionOS['estado']['input'])

    estado = wait.until(EC.element_to_be_clickable((By.ID, extraccionOS['estado']['input'])))
    estado.send_keys(datos['estado']) #Ingresa el Estado

    #Elemento Fecha Orden
    open_item_selenium_wait(driver, id = extraccionOS['fOrden']['elemento'])

    #Click input Fecha Orden
    open_item_selenium_wait(driver, id = extraccionOS['fOrden']['input'])

    fOrden = wait.until(EC.element_to_be_clickable((By.ID, extraccionOS['fOrden']['input'])))

    if 'null' in datos['fechaAsignacion']:
        fOrden.send_keys("") #Ingresa el Estado
    else:
        infoFecha = datos['fechaAsignacion'].replace("\\", "")
        fOrden.send_keys(infoFecha) #Ingresa el Estado

    fOrden.send_keys(Keys.RETURN)  
    sleep(5)

def extracion(driver, tExtraccion):

    sleep(40)

    '''
    Funcion que culmina la extraccion desde el cuadro de dialogos

    args:
        - driver (obj): instancia del navegador
    
    s_at_m_1 - Orde serv
    s_at_m_1 - Cuentas
    s_at_m_1 - Negocios
    s_at_m_1 - Activ

    out:
        - driver (obj): instancia del navegador
        - stutus (bool): True si se pudo ingresar a 'Ordenes de Servicio' e ingreso la orden, False en caso contrario
    '''
    #Se define el maximo de espera para los elementos, si esto se excede, se genera una excepción
    wait = WebDriverWait(driver, 30)

    text_box('Pantalla:: Cuadro emergente', '☼')

    #Entra engrane para extraccion
    print('Click sobre el engrane')
    open_item_selenium_wait(driver, id='s_at_m_1', xpath='//*[@id="s_at_m_1"]')

    sleep(3)

    # Selecciona extraccion
    print('Click sobre opcion EXPORTAR')

    if 'Cuenta' in tExtraccion:
        open_item_selenium_wait(driver, xpath=extraccionCuentas['exportar'])

    elif 'Casos de negocio' in tExtraccion:
        open_item_selenium_wait(driver, xpath=extraccionCN['exportar'])

    elif 'Actividades' in tExtraccion:
        open_item_selenium_wait(driver, xpath=extraccionactividades['exportar'])

    elif 'Ordenes de servicio' in tExtraccion:
        open_item_selenium_wait(driver, xpath=extraccionOS['exportar'])
    
    #//*[@id="s_at_m_1-menu"]/li[22]

    sleep(3)
    #print('Click sobre opcion EXPORTAR')
    #open_item_selenium(driver, xpath='//*[@id="s_at_m_1-menu"]/li[23]')
    
    # sleep(3)
    try:
        print('Click sobre casilla TODOS')
        driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input[1]').click()
        
        sleep(3)
        print('Click sobre casilla delimitador COMAS')
        driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input[2]').click()
        # open_item_selenium(driver, xpath=, name='s_2_1_108_0') 
        sleep(5)
        print('Click sobre btn SIGUIENTE')
        driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[2]/button').click()

        sleep(3)

        busquedaExtraccion = True

        while busquedaExtraccion == True:
            sleep(20)

            dir = os.listdir('C:\\Users\\vix10\\Downloads')

            if 'output.CSV' in dir:

                print('Extraccion completa')
                print('ARCHIVO DESCARGADO')
                busquedaExtraccion = False

                ################### Conversion CSV a EXCEL

                with open('C:\\Users\\vix10\\Downloads\\output.CSV', "rb") as f:
                    df = pd.read_csv(f, encoding="utf_16", sep=',')
                    excelWrite = pd.ExcelWriter('C:\\Users\\vix10\\Downloads\\output.xlsx')
                    df.to_excel(excelWrite, index=None)
                    excelWrite.close()

                ################### Obtencion de FECHA

                fechaHRA = datetime.datetime.now()
                fechaHRA = str(fechaHRA)
                fechaHRA = fechaHRA.replace(":", "")
                nArchivo = 'Extraccion '+ tExtraccion + ' ' + fechaHRA + '.xlsx'

                archivoO = 'C:\\Users\\vix10\\Downloads\\output.xlsx'
                archivoNew = 'C:\\Users\\vix10\\Downloads\\' + nArchivo

                os.rename(archivoO, archivoNew)

                ################### CONFIGURACION FTP

                ftp_servidor = '192.168.50.37'
                ftp_usuario  = 'rpaBack1'
                ftp_clave    = 'Cyber123'
                ftp_raiz     = '/Extracciones'

                ################## DATOS DEL FICHERO A SUBIR

                ficheroOrigen = archivoNew
                ficheroDestino = nArchivo

                ################# Conexion al FTP

                try:

                    s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
                    try:
                        f = open(ficheroOrigen, 'rb')
                        s.cwd(ftp_raiz)
                        s.storbinary('STOR ' + ficheroDestino, f)
                        f.close()
                        s.quit()
                    except:
                        print("No se ha podido encontrar el fichero" + ficheroOrigen)
                
                except Exception as e:
                    print("No se ha podido conectar con el servidor" + ftp_servidor)
                    
                print('Archivo cargado a la FTP')

                cont = 0
                for x in dir:
                    if 'output.CSV' in x:
                        print('Archivo a eliminar: ', x)
                        os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                        cont += 1
                    elif 'Extraccion' in x:
                        print('Archivo a eliminar: ', x)
                        os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                        cont += 1
                    
                    if cont == 2:
                        break 
                sleep(3)
                return True, nArchivo
                
            else:
                print('Extraccion en PROCESO')
    
    except Exception:
        print('SIN DATOS EN LA EXTRACCION BUSCADA')
        return False, 'Error Sin Datos'



def pantalla_extracion(driver, datos, tExtraccion):
    '''
    Funcion que ingresa a la pantalla de Ordenes de Servicio e ingresa una orden

    args:
        - driver (obj): instancia del navegador

    out:
        - driver (obj): instancia del navegador
        - stutus (bool): True si se pudo ingresar a 'Ordenes de Servicio' e ingreso la orden, False en caso contrario
    '''
    #Se define el maximo de espera para los elementos, si esto se excede, se genera una excepción
    wait = WebDriverWait(driver, 30)

    text_box('Pantalla:: Extraccion', '☼')
    
    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('inicial'))

    #Entra a la ventana de Extraccion de Datos
    open_item_selenium_wait(driver, xpath = elementoExtraccion)

    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('Cuentas'))

    #Se abre Menu para seleccion de tipo de Extraccion
    open_item_selenium_wait(driver, id = menuExtracciones)
    print('Tipo extraccion: ' + tExtraccion)

    if 'Cuenta' in tExtraccion:
        print('Extraccion: ' + tExtraccion)
        extCuentas(driver,datos)

    elif 'Casos de negocio' in tExtraccion:
        print('Extraccion: ' + tExtraccion)
        extCasosNegocio(driver,datos)

    elif 'Actividades' in tExtraccion:
        print('Extraccion: ' + tExtraccion)
        extActividades(driver,datos)

    elif 'Ordenes de servicio' in tExtraccion:
        print('Extraccion: ' + tExtraccion)
        extOrdeneServicio(driver,datos)

    print('Se ingreso la extraccion')

    return driver, True


def validacion_orden_servicio(driver):
    '''
    Funcion que valida una orden de servicio al ser ingresada en la pantala 'Ordenes de servicio'
    
    args:
        - driver (obj): instancia del navegador
    
    out:
        - stutus (bool): True si la orden es valida, False en caso contrario
        - driver (obj): instancia del navegador
    '''
    text_box('Validación de Orden de Servicio', '☼')
    try:
        act = webdriver.ActionChains(driver)
        wait = WebDriverWait(driver, 120)

        print('▬Revisa si la orden esta vacia')

        '''------COPIA CON DOBLE CLICK-------'''
        #Localiza número orden en pantalla
        sleep(2)
        n_orden = driver.find_element(By.XPATH,"//*[@id='a_2']/div/table/tbody/tr[3]/td[4]/div/input")
        act.click(n_orden)
        act.double_click(n_orden).perform()
        texto = my_copy(driver)
        if texto:
            print('Orden valida')
        else:
            print('La orden no es valida')
            return False, '', ''
    except Exception as e:
        print('No se pudo copiar en el portapapeles')
        description_error('04-1','validacion_orden_servicio',e)            
        response = 'PRUEBA'
        print('Respuesta de API (Orden erronea):: ',response)
        return False, '', ''
    

    try:
        print('▬Validacion del estado de la orden')
        #Se va al estado inmediato para copiarlo
        sleep(2)
        element_estado =  driver.find_element(By.XPATH, '//*[@id="1_s_1_l_Status"]')
        act.click(element_estado)
        act.double_click(element_estado).perform()
        estado_orden = my_copy(driver)
        print('Obtencion de estado')
        estado_orden = estado_orden.lower().strip()
        text_box('La cuenta está: ' + estado_orden,'◘')
        #response = api.orden_cerrada(id_lead,sourceApi)
        response = 'PRUEBA'
        print ('Respuesta de la API: ',response)
        return True, driver, estado_orden
    
    except Exception as e:
        print(f'No se pudo validar el estado de la orden')
        description_error('04-3','validacion_orden_servicio',e)            
        return False, '', ''


def cerrar_orden_servicio(driver, cuenta_api, source_api, comentarios, motivo, estadoC):
    '''
    Funcion que cierra la orden de servicio 

    args:
        - driver (obj): instancia del navegador
        - cuenta_api (str): numero de cuenta liada a la orden de servicio, viene de la api
        - source_api(str): fuente de los datos
    out:
        - stutus (bool): True si la orden es valida, False en caso contrario
        - driver (obj): instancia del navegador
    '''
    act = webdriver.ActionChains(driver)
    wait = WebDriverWait(driver, 120)

    text_box('Cerrar orden pendiente / abierta', '☼')
    #Hace click en el enlace generado por la misma orden de servicio
    print('Clic en el enlace de la orden')
    element = driver.find_element(By.NAME,'Order Number').click() 
    #Se va a la cuenta para copiarla
    print('Llegue a la orden')
    element_cuenta = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[5]/td[3]/div/input')))
    act.click(element_cuenta)
    act.double_click(element_cuenta).perform()
    cuenta_siebel = my_copy(driver)
    
    if int(cuenta_siebel) != int(cuenta_api) or source_api !="izzi_ext":
        text_box('Las cuentas no coinciden o la fuente no es la correcta', '▒')
        print(f'cuenta_siebel: {cuenta_siebel}')
        print(f'cuenta_api:    {cuenta_api}')
        print(f'source_api:    {source_api}')
        return  False
    

    #Se deben poner los campos que viene de la api de la API
    status_llenado = rellena_campos_orden_servicio(driver, comentarios, motivo, estadoC)
    if status_llenado != True:
        return False
    
    print('Validacion de cancelacion')
    
    #Entra a pantalla HOME
    #Si hay alerta no se canceló bien

    status_home = open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
    if status_home == False:
        #IMPORTANTE:: No se ha localizado la alerta 
        sleep(10)
        text_box('Hay alerta de NO CANCELADO','▒')
        alert = driver.switch_to.alert
        alert.accept()
        #--------
        # cerrada = cerrarOrdenAgain(driver,numero_orden,comentarios, motivo, estado_orden)
        # #--------
        # if cerrada != True:
        #     response = api.cuenta_erronea(id_lead,source_id)
        #     print('Respuesta de API (ERROR DE CUENTA)',response)
    sleep(2)
    print('Se canceló con éxito ☺')
    return True


def rellena_campos_orden_servicio(driver, comentarios, motivo, estado): 
    '''
    Funcion que llena los campos al cerrar la orden de servicio

    args:
        - driver
        - comentarios
        - motivo
        - estado
    
    out: 
        - stutus (bool): True si se ingresaron todos los campos de la orden, False en caso contrario
    '''
    try:
        act = webdriver.ActionChains(driver)
        wait = WebDriverWait(driver, 120)
        
        text_box('Se llenan campos de Orden de Servicio','☼')
        #COMENTARIOS
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[11]/td[7]/div/textarea')))
        element.clear() 
        element.send_keys(comentarios)
        print('OK: comentarios')

        #MOTIVO
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[5]/td[9]/div/input')))
        sleep(0.5)
        element.clear()
        sleep(0.5)
        element.send_keys(motivo) #poner los de la API
        element.send_keys(Keys.ENTER)#if motivo o bie, entrar al drop y seleecionar
        print('OK: motivo')

        #Estado
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[7]/td[9]/div/input')))
        sleep(2)
        act.double_click(element).perform()
        sleep(1)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        sleep(1)
        #-Paste
        element.send_keys(estado) 
        element.send_keys(Keys.ENTER)
        sleep(2)
        print('OK: estado')
        return True
    except Exception as e:
        print(f'No se pudieron ingresar los campos de la orden')
        description_error('05','rellena_campos_orden_servicio',e)
        return False    


def cerrarOrdenAgain(driver,numeroOrdenApi,comentarios, motivo, estado):
    print('▬▬Se volverá a intentar cerrar la orden▬▬')
    act = webdriver.ActionChains(driver)
    wait = WebDriverWait(driver, 120)
    #Pantalla de ORDENES
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[6]')))
    element.click()
    print('█Pantalla de Ordenes de Servicio')
    sleep(10)
    #LUPA
    try:
        lupa = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s_1_1_24_0_Ctrl"]')))
        #lupa.location_once_scrolled_into_view
        lupa.click()
        print('█Busqueda')
    except Exception as e:
        print('La ventana debe estar abierta')
        driver.quit()
        exit()
    #Insertar 
    #Se posiciona para escirbir en el campo de numero de orden
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1_s_1_l_Order_Number"]')))
    element.click()
    print('█Posicion')
    element = driver.find_element(By.XPATH,'//*[@id="1_Order_Number"]')
    element.clear()                    #Limpia lo que haya en el campo
    element.send_keys(numeroOrdenApi)  #Introduce el numero de orden
    element.send_keys(Keys.RETURN)     #Enter
    print('█Ingreso de número de orden')
    sleep(2)

    '''------COPIA CON DOBLE CLICK-------'''
    #Se va al estado inmediato para copiarlo
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1_s_1_l_Status"]'))).click()
    element = driver.find_element(By.XPATH, '//*[@id="1_Status"]')
    print('█Estado (inmediato)')
    #Doble click
    act = webdriver.ActionChains(driver)
    act.double_click(element).perform()
    #Copiar el estado (CRTL + C)
    #act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    '''------FIN COPIA DEOBLE CLICK-------'''
    #Hace click en el enlace generado
    sleep(2)
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[6]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]/a').click() 
    sleep(10)
    print('█Enlace')
    #Casmpos
    rellena_campos_orden_servicio(driver, comentarios, motivo, estado)
    #Mover a HOME
    #Entra a pantalla HOME
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[1]')))
    print('█Home')
    element.click()
    #Si hay alerta no se cancelo bien
    try:
        element = wait.until(EC.element_to_be_clickable((By.ID, 's_4_1_11_0_mb')))
        print('█Se canceló con éxito en el segundo intento')
        return True
    #FALTA RESVISAR LAS CUENTAS QUE DIGAN VIDEO
    except Exception as e:
        sleep(10)
        print('█Hay alerta de NO CANCELADO')
        alert = driver.switch_to.alert
        alert.accept()
        return False
    #Alerta
    #MARCAR COMO ERRONEA
    
    