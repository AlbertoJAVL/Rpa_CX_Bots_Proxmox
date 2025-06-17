#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

#-------------System-------------------#
from time import sleep
import os
import win32clipboard as cp
import datetime 
import ftplib
import pandas as pd
import calendar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#---------Mis funciones---------------#


from utileria import *
from logueo import *
from rutas import *

from myFunctions import  AlertaSaldoVencido

#########################################################################################################

def deteccionPantalla(driver, titExtraccion, tExtraccion):
    try:
        contador = 0
        cambio = True
        while contador < 5:
            titulo = driver.title
            print(titulo)
            
            if titExtraccion in titulo:
                contador = 5
                cambio = False
            else:
                sleep(2)
                contador += 1
                if contador == 5:
                    print('fallo')
                    cambio = True

        if cambio == True:
            if 'Actividades' in tExtraccion:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]").click()
                
                sleep(3)
                driver.find_element(By.XPATH, "//option[@un='Todas las actividades']").click()
    
    except Exception as e:
        print(e)
        print('Falla en deteccion de pantall')
        return False

def deteccionPantalla2(driver, titExtraccion, tExtraccion):
    try:
        contador = 0
        cambio = True
        while contador < 5:
            titulo = driver.title
            print(titulo)
            
            if titExtraccion in titulo:
                contador = 5
                cambio = False
            else:
                sleep(2)
                contador += 1
                if contador == 5:
                    print('fallo')
                    cambio = True

        if cambio == True:
            if 'Actividades' in tExtraccion:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]").click()
                
                sleep(3)
                driver.find_element(By.XPATH, "//option[@un='Todas las actividades']").click()
    
    except Exception as e:
        print(e)
        print('Falla en deteccion de pantall')
        return False

def separacionParametrosExtraccion(datos, tExtraccion):

    datosF = datos.replace('[{', '')
    datosF = datosF.replace('}]', '')

    # print(datosF)
    
    parametrosExtraccion = datosF.split(',')
    # print(parametrosExtraccion)

    # for x in parametrosExtraccion:
    #     print(x)

    if 'Casos de negocio' in tExtraccion:

        fechaApertura = parametrosExtraccion[0].split('"fechaApertura":')
        fechaApertura = fechaApertura[1]
        fechaApertura = fechaApertura[1:-1]
        # fechaApertura = fechaApertura.replace('"','')
        print('Fecha de apertura: ',fechaApertura)

        estado = parametrosExtraccion[1].split('"estado":')
        estado = estado[1]
        estado = estado[1:-1]
        print('Estado: ',estado)

        cuenta = parametrosExtraccion[2].split('"cuenta":')
        
        cuenta = cuenta[1]
        cuenta = cuenta[1:-1]
        print('No cuenta: ',cuenta)

        medioContacto = parametrosExtraccion[3].split('"medioContacto":')
        
        medioContacto = medioContacto[1]
        medioContacto = medioContacto[1:-1]
        print('Medio de contacto: ',medioContacto)

        numCaso = parametrosExtraccion[4].split('"casoNegocio":')
        
        numCaso = numCaso[1]
        numCaso = numCaso[1:-1]
        print('Numero de caso: ', numCaso)

        categoria = parametrosExtraccion[5].split('"categoria":')
        
        categoria = categoria[1]
        categoria = categoria[1:-1]
        print('Categoria: ',categoria)

        motivo = parametrosExtraccion[6].split('"motivo":')
        motivo = motivo[1]
        motivo = motivo[1:-1]
        print('Motivo: ',motivo)
        
        motivoCliente = parametrosExtraccion[9].split('"motivoCliente":')
        motivoCliente = motivoCliente[1]
        motivoCliente = motivoCliente[1:-1]
        print('Motivo del cliente: ',motivoCliente)

        subMotivo = parametrosExtraccion[7].split('"subMotivo":')
        subMotivo = subMotivo[1]
        subMotivo = subMotivo[1:-1]
        print('SubMotivos: ',subMotivo)

        solucion = parametrosExtraccion[8].split('"solucion":')
        solucion = solucion[1]
        solucion = solucion[1:-1]
        print('Solucion: ',solucion)

        

        parametrosFinales = {
            'fechaApertura':fechaApertura,
            'estado':estado,
            'cuenta':cuenta,
            'medioContacto':medioContacto,
            'numCaso':numCaso,
            'categoria':categoria,
            'motivo':motivo,
            'motivoCliente':motivoCliente,
            'subMotivo':subMotivo,
            'solucion':solucion
        }

        return parametrosFinales

    elif 'Actividades' in tExtraccion:

        estado = parametrosExtraccion[0].split('"estado":')
        # if '""' in estado[1] : estado = '' 
        # else: 
        estado = estado[1]
        estado = estado[1:-1]
        print('Estado: ',estado)

        areaConocimiento = parametrosExtraccion[1].split('"areaConocimiento":')
        if '""' in areaConocimiento[1] : areaConocimiento = '' 
        else: 
            areaConocimiento = areaConocimiento[1]
            areaConocimiento = areaConocimiento.replace('"','')
        print('Area de conocimiento: ',areaConocimiento)

        fechaAsignacion = parametrosExtraccion[2].split('"fechaAsignacion":')
        if '""' in fechaAsignacion[1] : fechaAsignacion = '' 
        else: fechaAsignacion = fechaAsignacion[1]
        fechaAsignacion = fechaAsignacion.replace('"','')
        fechaAsignacion = fechaAsignacion.replace('"','')
        print(fechaAsignacion)
        
        tipo = parametrosExtraccion[3].split('"tipo":')
        if '""' in tipo[1] : tipo = '' 
        else: 
            tipo = tipo[1]
            tipo = tipo.replace('"','')
        print(tipo)

        vencimiento = parametrosExtraccion[4].split('"vencimientoActividad":')
        if '""' in vencimiento[1] : vencimiento = '' 
        else: vencimiento = vencimiento[1]
        vencimiento = vencimiento.replace('"','')
        print(vencimiento)

        fechaCreacion = parametrosExtraccion[5].split('"fechaCreacion":')
        if '""' in fechaCreacion[1] : fechaCreacion = '' 
        else: fechaCreacion = fechaCreacion[1]
        fechaCreacion = fechaCreacion.replace('"','')
        print(fechaCreacion)

        parametrosFinales = {
            'estado':estado,
            'areaConocimiento':areaConocimiento,
            'fechaCreacion':fechaCreacion,
            'tipo':tipo,
            'vencimiento':vencimiento,
            'fechaAsignacion':fechaAsignacion
        }

        return parametrosFinales

    elif 'Ordenes de servicio' in tExtraccion:

        cuenta = parametrosExtraccion[0].split('"cuenta":')
        # if '""' in cuenta[1] : cuenta = '' 
        # else: 
        cuenta = cuenta[1]
        cuenta = cuenta[1:-1]
        print('-----------------------------')
        print(cuenta)
        print('-----------------------------')

        compañia = parametrosExtraccion[1].split('"compania":')
        # if '""' in compañia[1] : compañia = '' 
        # else: 
        compañia = compañia[1]
        compañia = compañia[1:-1]
        print('-----------------------------')
        print(compañia)
        print('-----------------------------')

        telefonos = parametrosExtraccion[2].split('"telefonos":')
        # if '""' in telefonos[1] : telefonos = '' 
        # else: 
        telefonos = telefonos[1]
        telefonos = telefonos[1:-1]
        print('-----------------------------')
        print(telefonos)
        print('-----------------------------')

        numeroOrden = parametrosExtraccion[3].split('"numOrden":')
        # if '""' in numeroOrden[1] : numeroOrden = '' 
        # else: 
        numeroOrden = numeroOrden[1]
        numeroOrden = numeroOrden[1:-1]
        print('-----------------------------')
        print(numeroOrden)
        print('-----------------------------')


        tipoOrden = parametrosExtraccion[4].split('"tipoOrden":')
        print(tipoOrden)
        # if '""' in tipoOrden[1] : tipoOrden = '' 
        # else:
        tipoOrden = tipoOrden[1]
        tipoOrden = tipoOrden[1:-1]
        # tipoOrden = tipoOrden.replace('"','')
        print('-----------------------------')
        print(tipoOrden)
        print('-----------------------------')
        
        fechaOrden = parametrosExtraccion[5].split('"fechaOrden":')
        print(fechaOrden)
        # if '""' in fechaOrden[1] : fechaOrden = '' 
        # else: 
        fechaOrden = fechaOrden[1]
        fechaOrden = fechaOrden[1:-1]        
        print('-----------------------------')
        print(fechaOrden)
        print('-----------------------------')

        estado = parametrosExtraccion[6].split('"estado":')
        # if '""' in estado[1] : estado = '' 
        # else: 
        estado = estado[1]
        estado = estado[1:-1]
        print('-----------------------------')
        print(estado)
        print('-----------------------------')

        parametrosFinales = {
            'cuenta':cuenta,
            'compañia':compañia,
            'telefonos':telefonos,
            'numeroOrden':numeroOrden,
            'tipoOrden':tipoOrden,
            'fechaOrden':fechaOrden,
            'estado':estado
        }
        # print(parametrosFinales)

        return parametrosFinales


def busquedaColDatos(driver, extraccion, xpathIn):
    buscandoExtraccion = True
    contador = 1

    while buscandoExtraccion == True:
        xpath = xpathIn.replace('{contador}', str(contador))
        elemExtraccion = driver.find_element(By.XPATH, xpath)
        elemExtraccion = driver.execute_script("return arguments[0].textContent;", elemExtraccion)
        # elemExtraccion = elemExtraccion.text
        print(elemExtraccion)
        if extraccion in elemExtraccion:
            buscandoExtraccion = False
            return str(contador)
        else:
            contador += 1

def busquedaColDatos2(driver, extraccion, xpathIn):
    buscandoExtraccion = True
    contador = 1

    while buscandoExtraccion == True:
        try:
            xpath = xpathIn.replace('{contador}', str(contador))
            elemExtraccion = driver.find_element(By.XPATH, xpath)
            elemExtraccion = elemExtraccion.get_attribute('un')
            print(elemExtraccion)
            
            if extraccion in elemExtraccion:
                buscandoExtraccion = False
                return str(contador)
            else:
                contador += 1
                if contador == 50:
                    buscandoExtraccion = False
                    return False
        except:
            contador += 1
            if contador == 50:
                buscandoExtraccion = False
                return False


def busquedaAtributos(driver, extraccion, xpathIn):
    buscandoExtraccion = True
    contador = 1

    while buscandoExtraccion == True:
        try:
            xpath = xpathIn.replace('{contador}', str(contador))
            elemExtraccion = driver.find_element(By.XPATH, xpath)
            elemExtraccion = elemExtraccion.get_attribute('data-caption')
            print(elemExtraccion)
            if extraccion in elemExtraccion:
                buscandoExtraccion = False
                return str(contador)
            else:
                contador += 1
        except:
            contador += 1


def llenadoExtraccionCuentas(driver, preFinal, tabulacion ,final, datos, tExtraccion, cambio, tipoElemento):

    
    if 'Casos Negocio' in tExtraccion:
        driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]').click()
        if datos != False:
            if 'input' in tipoElemento:
                ingreso = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]/input')
                ingreso.send_keys(datos)
    
    elif 'Actividades' in tExtraccion:
        driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]').click()
        if datos != False:
            if 'input' in tipoElemento:
                ingreso = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]/input')
                ingreso.send_keys(datos)
    
    elif 'Ordenes Servicio' in tExtraccion:
        driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]').click()
        if datos != False:
            if 'input' in tipoElemento:
                ingreso = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]/input')
                ingreso.send_keys(datos)

    if preFinal == True:
        ingreso.send_keys(Keys.RETURN)

    if tabulacion == True:
        ingreso.send_keys(Keys.TAB)

    if final == True:
        ingreso.send_keys(Keys.RETURN)

def llenadoExtraccionCuentas2(driver, preFinal, tabulacion ,final, datos, tExtraccion, cambio, tipoElemento):

    
    if 'Casos Negocio' in tExtraccion:
        driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]').click()
        if datos != False:
            if 'input' in tipoElemento:
                ingreso = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]/input')
                ingreso.send_keys(datos)
    
    elif 'Actividades' in tExtraccion:
        driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]').click()
        if datos != False:
            if 'input' in tipoElemento:
                ingreso = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]/input')
                ingreso.send_keys(datos)
    
    elif 'Ordenes Servicio' in tExtraccion:
        driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]').click()
        if datos != False:
            if 'input' in tipoElemento:
                ingreso = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{cambio}]/input')
                ingreso.send_keys(datos)

    if preFinal == True:
        ingreso.send_keys(Keys.RETURN)

    if tabulacion == True:
        ingreso.send_keys(Keys.TAB)

    if final == True:
        ingreso.send_keys(Keys.RETURN)



def extCasosNegocio(driver, datos, diasVencidos):

    sleep(5)
    
    print('Fun Extraccion Casos de Negocio')
    wait = WebDriverWait(driver,120)

    validacion = deteccionPantalla(driver, 'Todas las Ordenes', 'Casos de Negocio')
    if validacion == False: return 'Error Bot Extraccion'

    #LUPA DE BUSQUEDA
    labelBusqueda = 'Casos de negocio Applet de lista:Consulta'
    driver.find_element(By.XPATH, f"//button[@aria-label='{labelBusqueda}']").click()

    #Caso de Negocio
    numCol = busquedaColDatos(driver, 'Caso de negocio', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, False, False, datos['numCaso'], 'Casos Negocio', numCol, 'input')
    
    #Estado
    numCol = busquedaColDatos(driver, 'Estado', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, False, False, datos['estado'], 'Casos Negocio', numCol, 'input')

    #Categoria
    numCol = busquedaColDatos(driver, 'Categoría', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, False, False, datos['categoria'], 'Casos Negocio', numCol, 'input')

    #Motivos
    numCol = busquedaColDatos(driver, 'Motivos', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, False, False, datos['motivo'], 'Casos Negocio', numCol, 'input')

    #SubMotivos
    numCol = busquedaColDatos(driver, 'Submotivo', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, False, False, datos['subMotivo'], 'Casos Negocio', numCol, 'input')

    #Solucion
    numCol = busquedaColDatos(driver, 'Solución', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, False, False, datos['solucion'], 'Casos Negocio', numCol, 'input')

    #Cuenta
    numCol = busquedaColDatos(driver, 'Tipo de Contribuyente', nuvasRutas['columnasCasosNegocio'])
    llenadoExtraccionCuentas(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')

    numCol = busquedaColDatos(driver, 'Nº de cuenta', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, True, False, datos['cuenta'], 'Casos Negocio', numCol, 'input')

    #fechaApertura


    numCol = busquedaColDatos(driver, 'Fecha de apertura', nuvasRutas['columnasCasosNegocio'])
    if diasVencidos == False:
        if numCol == False:
            return 'Error Bot Extraccion' 
        if 'null' in datos['fechaApertura']:
            llenadoExtraccionCuentas(driver, False, False, False, "", 'Casos Negocio', numCol, 'input')
        else:
            infoFecha = datos['fechaApertura'].replace("\\", "")
            if "AND <= ''" in infoFecha:
                infoFecha = infoFecha.replace("AND <= ''", "")
            llenadoExtraccionCuentas(driver, False, False, False, infoFecha, 'Casos Negocio', numCol, 'input')
    else:

        fecha = datetime.date.today()
        año = fecha.year
        mes = fecha.month
        fechaUltimaMes = calendar.monthrange(int(año), int(mes))[1]
        fecha = datetime.datetime.strftime(fecha, '%d/%m/%Y')

        fechaExtraccionF = f">= '{fecha}' AND <= '{str(fechaUltimaMes)}/{str(mes)}/{str(año)}'"
        llenadoExtraccionCuentas(driver, False, False, False, fechaExtraccionF, 'Casos Negocio', numCol, 'input')
    
    #Motivo del cliente
    numCol = busquedaColDatos(driver, 'Subestado de la cuenta', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')

    numCol = busquedaColDatos(driver, 'Folio Id Portabilidad', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')

    numCol = busquedaColDatos(driver, 'Motivo Cliente', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, True, False, datos['motivoCliente'], 'Casos Negocio', numCol, 'input')

    #Medio de contacto

    numCol = busquedaColDatos(driver, 'Nodo', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')

    numCol = busquedaColDatos(driver, 'Hub', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')

    numCol = busquedaColDatos(driver, 'Medio de contacto', nuvasRutas['columnasCasosNegocio'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas(driver, True, False, False, datos['medioContacto'], 'Casos Negocio', numCol, 'input')

    esperandoResultados = True
    contador = 0
    while esperandoResultados == True:
        try:
            sleep(10)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[35]').click()
            esperandoResultados = False
            sleep(2)
            return True
        except:
            contador += 1
            if contador == 20:
                esperandoResultados = False
                errro = 'Error Sin Datos'
                print(errro)
                return errro

def extCasosNegocio2(driver, datos, diasVencidos):

    sleep(5)
    
    print('Fun Extraccion Casos de Negocio')
    wait = WebDriverWait(driver,120)

    validacion = deteccionPantalla(driver, 'Todos los Casos de Negocio', 'Casos de Negocio')
    if validacion == False: return 'Error Bot Extraccion'

    #LUPA DE BUSQUEDA
    labelBusqueda = 'Todos los Casos de Negocio Applet de lista:Consulta'
    driver.find_element(By.XPATH, f"//button[@aria-label='{labelBusqueda}']").click()

    #Caso de Negocio
    numCol = busquedaColDatos(driver, 'Caso de negocio', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['numCaso'], 'Casos Negocio', numCol, 'input')

    #Cuenta
    numCol = busquedaColDatos(driver, 'Nº de cuenta', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['cuenta'], 'Casos Negocio', numCol, 'input')

    #Categoria
    numCol = busquedaColDatos(driver, 'Categoría', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['categoria'], 'Casos Negocio', numCol, 'input')

    #Motivos
    numCol = busquedaColDatos(driver, 'Motivos', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['motivo'], 'Casos Negocio', numCol, 'input')

    #SubMotivos
    numCol = busquedaColDatos(driver, 'Submotivo', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['subMotivo'], 'Casos Negocio', numCol, 'input')

    #Solucion
    numCol = busquedaColDatos(driver, 'Solución', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['solucion'], 'Casos Negocio', numCol, 'input')
    
    #Estado
    numCol = busquedaColDatos(driver, 'Estado', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['estado'], 'Casos Negocio', numCol, 'input')


    #Medio de contacto

    numCol = busquedaColDatos(driver, 'Medio de contacto', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, False, False, datos['medioContacto'], 'Casos Negocio', numCol, 'input')

    #fechaApertura
    # numCol = busquedaColDatos(driver, 'Tipo de Contribuyente', nuvasRutas['columnasCasosNegocio'])
    # llenadoExtraccionCuentas(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')


    numCol = busquedaColDatos(driver, 'Fecha de apertura', nuvasRutas['columnasCasosNegocio2'])
    if diasVencidos == False:
        if numCol == False:
            return 'Error Bot Extraccion' 
        if 'null' in datos['fechaApertura']:
            llenadoExtraccionCuentas2(driver, False, False, False, "", 'Casos Negocio', numCol, 'input')
        else:
            infoFecha = datos['fechaApertura'].replace("\\", "")
            if "AND <= ''" in infoFecha:
                infoFecha = infoFecha.replace("AND <= ''", "")
            llenadoExtraccionCuentas2(driver, False, False, False, infoFecha, 'Casos Negocio', numCol, 'input')
    else:

        fecha = datetime.date.today()
        año = fecha.year
        mes = fecha.month
        fechaUltimaMes = calendar.monthrange(int(año), int(mes))[1]
        fecha = datetime.datetime.strftime(fecha, '%d/%m/%Y')

        fechaExtraccionF = f">= '{fecha}' AND <= '{str(fechaUltimaMes)}/{str(mes)}/{str(año)}'"
        llenadoExtraccionCuentas2(driver, False, False, False, fechaExtraccionF, 'Casos Negocio', numCol, 'input')
    
    #Motivo del cliente
    numCol = busquedaColDatos(driver, 'Motivo del cierre', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')

    numCol = busquedaColDatos(driver, 'Fecha de última actualización', nuvasRutas['columnasCasosNegocio2'])
    if numCol == False:
        return 'Error Bot Extraccion' 
    llenadoExtraccionCuentas2(driver, False, True, False, "", 'Casos Negocio', numCol, 'input')
    try:
        numCol = busquedaColDatos(driver, 'Motivo Cliente', nuvasRutas['columnasCasosNegocio2'])
        if numCol == False:
            return 'Error Bot Extraccion' 
        llenadoExtraccionCuentas2(driver, False, False, True, datos['motivoCliente'], 'Casos Negocio', numCol, 'input')


        esperandoResultados = True
        contador = 0
        while esperandoResultados == True:
            try:
                sleep(10)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[26]').click()
                esperandoResultados = False
                sleep(2)
                return True
            except:
                contador += 1
                if contador == 20:
                    esperandoResultados = False
                    errro = 'Error Sin Datos'
                    print(errro)
                    return errro
    except Exception as e:
        print(e)
        sleep(1000)


def extActividades(driver, datos, diasVencidos):
    try:
    
        print('Fun Extraccion Actividades')
        wait = WebDriverWait(driver,120)

        validacion = deteccionPantalla(driver, 'Todas las actividades', 'Actividades')
        if validacion == False: return 'Error Bot Extraccion'

        #LUPA DE BUSQUEDA
        sleep(5)
        labelBusqueda = 'Actividades Applet de lista:Consulta'
        driver.find_element(By.XPATH, f"//button[@aria-label='{labelBusqueda}']").click()

        #Estatus

        numCol = busquedaColDatos2(driver, 'Estado de la asignación', nuvasRutas['columnasActividades'])
        if numCol == False:
            return 'Error Bot Extraccion'
        llenadoExtraccionCuentas(driver, False, False, False, datos['estado'], 'Actividades', numCol, 'input')

        #Area de conocimiento
        numCol = busquedaColDatos2(driver, 'Área de conocimiento', nuvasRutas['columnasActividades'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas(driver, False, False, False, datos['areaConocimiento'], 'Actividades', numCol, 'input')

        #Fecha de Asignacion
        numCol = busquedaColDatos2(driver, 'Fecha de asignación', nuvasRutas['columnasActividades'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        if diasVencidos == False:
        
            if 'null' in datos['fechaAsignacion']:
                llenadoExtraccionCuentas(driver, False, False, False, "", 'Actividades', numCol, 'input')
            else:
                infoFecha = datos['fechaAsignacion'].replace("\\", "")
                if "AND <= ''" in infoFecha:
                    infoFecha = infoFecha.replace("AND <= ''", "")
                llenadoExtraccionCuentas(driver, False, False, False, infoFecha, 'Actividades', numCol, 'input')
        else:

            fecha = datetime.date.today()
            año = fecha.year
            mes = fecha.month
            fechaUltimaMes = calendar.monthrange(int(año), int(mes))[1]
            fecha = datetime.datetime.strftime(fecha, '%d/%m/%Y')

            fechaExtraccionF = f">= '{fecha}' AND <= '{str(fechaUltimaMes)}/{str(mes)}/{str(año)}'"
            llenadoExtraccionCuentas(driver, False, False, False, fechaExtraccionF, 'Actividades', numCol, 'input')

        #Fecha de Creacion
        numCol = busquedaColDatos2(driver, 'Inicio', nuvasRutas['columnasActividades'])
        
        if 'null' in datos['fechaCreacion']:
            llenadoExtraccionCuentas(driver, False, False, False, "", 'Actividades', numCol, 'input')
        else:
            infoFecha = datos['fechaCreacion'].replace("\\", "")
            if "AND <= ''" in infoFecha:
                infoFecha = infoFecha.replace("AND <= ''", "")
            llenadoExtraccionCuentas(driver, False, False, False, infoFecha, 'Actividades', numCol, 'input')

        try:

            alert = Alert(driver)
            alert_txt = alert.text
            print(alert_txt)
            alert.accept()
            sleep(1000)
        
        except Exception:
            print('No hay cuadro de error')

        #Vencimiento
        numCol = busquedaColDatos2(driver, 'Vencimiento', nuvasRutas['columnasActividades'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        
        if 'null' in datos['vencimiento']:
            llenadoExtraccionCuentas(driver, False, False, False, "", 'Actividades', numCol, 'input')
        else:
            infoFecha = datos['vencimiento'].replace("\\", "")
            if "AND <= ''" in infoFecha:
                infoFecha = infoFecha.replace("AND <= ''", "")
            llenadoExtraccionCuentas(driver, False, False, False, infoFecha, 'Actividades', numCol, 'input')

        #Tipo
        numCol = busquedaColDatos2(driver, 'Tipo', nuvasRutas['columnasActividades'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        llenadoExtraccionCuentas(driver, True, False, True, datos['tipo'], 'Actividades', numCol, 'input')

        esperandoResultados = True
        contador = 0
        while esperandoResultados == True:
            try:
                sleep(10)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]').click()
                esperandoResultados = False
                sleep(2)
                return True
            except:
                contador += 1
                if contador == 20:
                    esperandoResultados = False
                    errro = 'Error Sin Datos'
                    print(errro)
                    return errro
    except Exception as e:
        print(e)

def extActividades2(driver, datos, diasVencidos):
    try:
    
        print('Fun Extraccion Actividades')
        wait = WebDriverWait(driver,120)

        validacion = deteccionPantalla(driver, 'Todas las Actividades', 'Actividades')
        if validacion == False: return 'Error Bot Extraccion'

        #LUPA DE BUSQUEDA
        sleep(5)
        labelBusqueda = 'Todas las Actividades Applet de lista:Consulta'
        driver.find_element(By.XPATH, f"//button[@aria-label='{labelBusqueda}']").click()

        #Fecha de Creacion
        numCol = busquedaColDatos2(driver, 'Creado', nuvasRutas['columnasActividades2'])
        
        if 'null' in datos['fechaCreacion']:
            llenadoExtraccionCuentas2(driver, False, False, False, "", 'Actividades', numCol, 'input')
        else:
            infoFecha = datos['fechaCreacion'].replace("\\", "")
            if "AND <= ''" in infoFecha:
                infoFecha = infoFecha.replace("AND <= ''", "")
            llenadoExtraccionCuentas2(driver, False, False, False, infoFecha, 'Actividades', numCol, 'input')

        try:

            alert = Alert(driver)
            alert_txt = alert.text
            print(alert_txt)
            alert.accept()
            sleep(1000)
        
        except Exception:
            print('No hay cuadro de error')

        #Tipo
        numCol = busquedaColDatos2(driver, 'Tipo', nuvasRutas['columnasActividades2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        llenadoExtraccionCuentas2(driver, False, False, False, datos['tipo'], 'Actividades', numCol, 'input')

        #Fecha de Asignacion
        numCol = busquedaColDatos2(driver, 'Fecha de asignación', nuvasRutas['columnasActividades2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        if diasVencidos == False:
        
            if 'null' in datos['fechaAsignacion']:
                llenadoExtraccionCuentas2(driver, False, False, False, "", 'Actividades', numCol, 'input')
            else:
                infoFecha = datos['fechaAsignacion'].replace("\\", "")
                if "AND <= ''" in infoFecha:
                    infoFecha = infoFecha.replace("AND <= ''", "")
                llenadoExtraccionCuentas2(driver, False, True, False, infoFecha, 'Actividades', numCol, 'input')
        else:

            fecha = datetime.date.today()
            año = fecha.year
            mes = fecha.month
            fechaUltimaMes = calendar.monthrange(int(año), int(mes))[1]
            fecha = datetime.datetime.strftime(fecha, '%d/%m/%Y')

            fechaExtraccionF = f">= '{fecha}' AND <= '{str(fechaUltimaMes)}/{str(mes)}/{str(año)}'"
            llenadoExtraccionCuentas2(driver, False, True, False, fechaExtraccionF, 'Actividades', numCol, 'input')

        

        #Estatus
        numCol = busquedaColDatos2(driver, 'Estado de la asignación', nuvasRutas['columnasActividades2'])
        if numCol == False:
            return 'Error Bot Extraccion'
        llenadoExtraccionCuentas2(driver, False, False, False, datos['estado'], 'Actividades', numCol, 'input')

        #Area de conocimiento
        numCol = busquedaColDatos2(driver, 'Área de conocimiento', nuvasRutas['columnasActividades2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas2(driver, False, False, False, datos['areaConocimiento'], 'Actividades', numCol, 'input')

        

        #Vencimiento
        numCol = busquedaColDatos2(driver, 'Final', nuvasRutas['columnasActividades2'])
        if numCol == False:
            return 'Error Bot Extraccion'
        llenadoExtraccionCuentas2(driver, False, True, False, "", 'Actividades', numCol, 'input')

        numCol = busquedaColDatos2(driver, 'Vencimiento', nuvasRutas['columnasActividades2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        
        if 'null' in datos['vencimiento']:
            llenadoExtraccionCuentas2(driver, True, False, False, "", 'Actividades', numCol, 'input')
        else:
            infoFecha = datos['vencimiento'].replace("\\", "")
            if "AND <= ''" in infoFecha:
                infoFecha = infoFecha.replace("AND <= ''", "")
            llenadoExtraccionCuentas2(driver, True, False, False, infoFecha, 'Actividades', numCol, 'input')

        

        esperandoResultados = True
        contador = 0
        while esperandoResultados == True:
            try:
                sleep(10)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[20]').click()
                esperandoResultados = False
                sleep(2)
                return True
            except:
                contador += 1
                if contador == 20:
                    esperandoResultados = False
                    errro = 'Error Sin Datos'
                    print(errro)
                    return errro
    except Exception as e:
        print(e)



def extOrdeneServicio(driver, datos, diasVencidos):

    try:

        print('Fun Extraccion Ordenes servicio')
        wait = WebDriverWait(driver,120)

        #Espera a que la página tenga el titulo de Home 
        element = wait.until(EC.title_contains('Todos los pedidos'))

        #LUPA DE BUSQUEDA
        sleep(5)
        labelBusqueda = 'Ordenes de servicio Applet de lista:Consulta'
        driver.find_element(By.XPATH, f"//button[@aria-label='{labelBusqueda}']").click()

        #Compañia
        numCol = busquedaColDatos2(driver, 'Compañía', nuvasRutas['columnasOrdenesServicio'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas(driver, False, False, False, datos['compañia'], 'Ordenes Servicio', numCol, 'input')

        #Estado
        numCol = busquedaColDatos2(driver, 'Estado', nuvasRutas['columnasOrdenesServicio'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas(driver, False, False, False, datos['estado'], 'Ordenes Servicio', numCol, 'input')

        #Telefonos
        numCol = busquedaColDatos2(driver, 'Teléfonos', nuvasRutas['columnasOrdenesServicio'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas(driver, False, False, False, datos['telefonos'], 'Ordenes Servicio', numCol, 'input')

        #Numero de Orden
        numCol = busquedaColDatos2(driver, 'Nº de orden', nuvasRutas['columnasOrdenesServicio'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas(driver, False, False, False, datos['numeroOrden'], 'Ordenes Servicio', numCol, 'input')

        #Tipo de Orden
        numCol = busquedaColDatos2(driver, 'Tipo', nuvasRutas['columnasOrdenesServicio'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas(driver, False, False, False, datos['tipoOrden'], 'Ordenes Servicio', numCol, 'input')

        #Fecha de la fechaOrden
        numCol = busquedaColDatos2(driver, 'Fecha de la orden', nuvasRutas['columnasOrdenesServicio'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        if diasVencidos == False:

            if 'null' in datos['fechaOrden']:
                llenadoExtraccionCuentas(driver, False, False, False, "", 'Ordenes Servicio', numCol, 'input')
            else:
                infoFecha = datos['fechaOrden'].replace("\\", "")
                if "AND <= ''" in infoFecha:
                    infoFecha = infoFecha.replace("AND <= ''", "")
                llenadoExtraccionCuentas(driver, True, False, True, infoFecha, 'Ordenes Servicio', numCol, 'input')

        else:

            fecha = datetime.date.today()
            año = fecha.year
            mes = fecha.month
            fechaUltimaMes = calendar.monthrange(int(año), int(mes))[1]
            fecha = datetime.datetime.strftime(fecha, '%d/%m/%Y')

            fechaExtraccionF = f">= '{fecha}' AND <= '{str(fechaUltimaMes)}/{str(mes)}/{str(año)}'"
            llenadoExtraccionCuentas(driver, True, False, True, fechaExtraccionF, 'Ordenes Servicio', numCol, 'input')
        
        
        esperandoResultados = True
        contador = 0
        while esperandoResultados == True:
            try:
                sleep(10)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]').click()
                esperandoResultados = False
                sleep(2)
                return True
            except:
                contador += 1
                if contador == 35:
                    esperandoResultados = False
                    errro = 'Error Sin Datos'
                    print(errro)
                    return errro
    except Exception as e:
        print(e)
        sleep(1000)

def extOrdeneServicio2(driver, datos, diasVencidos):

    try:

        print('Fun Extraccion Ordenes servicio')
        wait = WebDriverWait(driver,120)

        validacion = deteccionPantalla(driver, 'Todas las Ordenes de Servicio', 'Ordenes de Servicio')
        if validacion == False: return 'Error Bot Extraccion'

        #LUPA DE BUSQUEDA
        sleep(5)
        labelBusqueda = 'Todas las Ordenes de Servicio Applet de lista:Consulta'
        driver.find_element(By.XPATH, f"//button[@aria-label='{labelBusqueda}']").click()

        #Numero de Orden
        numCol = busquedaColDatos2(driver, 'Nº de orden', nuvasRutas['columnasOrdenesServicio2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas2(driver, False, False, False, datos['numeroOrden'], 'Ordenes Servicio', numCol, 'input')

        #Tipo de Orden
        numCol = busquedaColDatos2(driver, 'Tipo', nuvasRutas['columnasOrdenesServicio2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas2(driver, False, False, False, datos['tipoOrden'], 'Ordenes Servicio', numCol, 'input')

        #Estado
        numCol = busquedaColDatos2(driver, 'Estado', nuvasRutas['columnasOrdenesServicio2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        llenadoExtraccionCuentas2(driver, False, False, False, datos['estado'], 'Ordenes Servicio', numCol, 'input')

        #Fecha de la fechaOrden
        numCol = busquedaColDatos2(driver, 'Fecha de la orden', nuvasRutas['columnasOrdenesServicio2'])
        if numCol == False:
            return 'Error Bot Extraccion'   
        
        if diasVencidos == False:

            if 'null' in datos['fechaOrden']:
                llenadoExtraccionCuentas2(driver, True, False, False, "", 'Ordenes Servicio', numCol, 'input')
            else:
                infoFecha = datos['fechaOrden'].replace("\\", "")
                if "AND <= ''" in infoFecha:
                    infoFecha = infoFecha.replace("AND <= ''", "")
                llenadoExtraccionCuentas2(driver, True, False, False, infoFecha, 'Ordenes Servicio', numCol, 'input')

        else:

            fecha = datetime.date.today()
            año = fecha.year
            mes = fecha.month
            fechaUltimaMes = calendar.monthrange(int(año), int(mes))[1]
            fecha = datetime.datetime.strftime(fecha, '%d/%m/%Y')

            fechaExtraccionF = f">= '{fecha}' AND <= '{str(fechaUltimaMes)}/{str(mes)}/{str(año)}'"
            llenadoExtraccionCuentas(driver, True, False, False, fechaExtraccionF, 'Ordenes Servicio', numCol, 'input')
        



        # #Compañia
        # numCol = busquedaColDatos2(driver, 'Compañía', nuvasRutas['columnasOrdenesServicio'])
        # if numCol == False:
        #     return 'Error Bot Extraccion'   
        # llenadoExtraccionCuentas(driver, False, False, False, datos['compañia'], 'Ordenes Servicio', numCol, 'input')


        # #Telefonos
        # numCol = busquedaColDatos2(driver, 'Teléfonos', nuvasRutas['columnasOrdenesServicio'])
        # if numCol == False:
        #     return 'Error Bot Extraccion'   
        # llenadoExtraccionCuentas(driver, False, False, False, datos['telefonos'], 'Ordenes Servicio', numCol, 'input')

        


        
        
        esperandoResultados = True
        contador = 0
        while esperandoResultados == True:
            try:
                sleep(10)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[14]').click()
                esperandoResultados = False
                sleep(2)
                return True
            except:
                contador += 1
                if contador == 35:
                    esperandoResultados = False
                    errro = 'Error Sin Datos'
                    print(errro)
                    return errro
    except Exception as e:
        print(e)
        sleep(1000)



def extracion(driver, tExtraccion, viaExtraccion, correo, info, ip):
    try:

        sleep(30)

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

        text_box('Pantalla:: Extraccion de querys', '☼')

        print('Click exportar')

        if 'Casos de negocio' in tExtraccion:
            labelEngrane = 'Casos de negocio Menú List'
            if 'true' in viaExtraccion:
                labelEngrane = 'Todos los Casos de Negocio Menú List'
            driver.find_element(By.XPATH, f"//button[@aria-label='{labelEngrane}']").click()
            sleep(5)

            numOpc = busquedaAtributos(driver, 'Exportar...', nuvasRutas['opcExportarCN'])
            driver.find_element(By.XPATH, nuvasRutas['opcExportarCN'].replace('{contador}', numOpc)).click()

        elif 'Actividades' in tExtraccion:

            labelEngrane = 'Actividades Menú List'
            if 'true' in viaExtraccion:
                labelEngrane = 'Todas las Actividades Menú List'
            driver.find_element(By.XPATH, f"//button[@aria-label='{labelEngrane}']").click()
            sleep(5)
            
            if 'true' not in viaExtraccion:
                numOpc = busquedaAtributos(driver, 'Exportar...', nuvasRutas['opcExportarAct'])
                driver.find_element(By.XPATH, nuvasRutas['opcExportarAct'].replace('{contador}', numOpc)).click()
            else:
                numOpc = busquedaAtributos(driver, 'Exportar...', nuvasRutas['opcExportarAct2'])
                driver.find_element(By.XPATH, nuvasRutas['opcExportarAct2'].replace('{contador}', numOpc)).click()

        elif 'Ordenes de servicio' in tExtraccion:
            labelEngrane = 'Ordenes de servicio Menú List'
            if 'true' in viaExtraccion:
                labelEngrane = 'Todas las Ordenes de Servicio Menú List'
            driver.find_element(By.XPATH, f"//button[@aria-label='{labelEngrane}']").click()
            sleep(5)
            
            numOpc = busquedaAtributos(driver, 'Exportar...', nuvasRutas['opcExportarOS'])
            driver.find_element(By.XPATH, nuvasRutas['opcExportarOS'].replace('{contador}', numOpc)).click()

        

        sleep(10)
        print('Click sobre casilla TODOS')
        driver.find_element(By.XPATH, "//input[@aria-label='Todo']").click()
        # driver.find_element(By.XPATH, "//input[@aria-label='Archivo de texto separado por comas']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Exportar Applet de formulario:Siguiente']").click()
        

        sleep(3)

        api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], 'Procesando', '', info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 25)

        try:

            alert = Alert(driver)
            alert_txt = alert.text
            print(alert_txt)
            alert.accept()
            error = 'Error Sin Permisos Extraccion'
            return False, '-', error
        
        except Exception:
            print('No hay cuadro de error')

        busquedaExtraccion = True
        intentosExtraccion = 0

        while busquedaExtraccion == True:
            sleep(20)

            try:

                alert = Alert(driver)
                alert_txt = alert.text
                print(alert_txt)
                alert.accept()
                if 'The server you are trying to access is either busy' in alert_txt:
                    error = 'Error Servidor Ocupado'
                    print(error)
                    return False, '-', error
            
            except Exception:
                print('No hay cuadro de error')

            dir = os.listdir('C:\\Users\\vix10\\Downloads')

            if 'output.csv' in dir or 'output.CSV' in dir:

                api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], 'Procesando', '', info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 50)

                print('Extraccion completa')
                print('ARCHIVO DESCARGADO')
                busquedaExtraccion = False

                ################### Conversion CSV a EXCEL

                # with open('C:\\Users\\vix10\\Downloads\\output.CSV', "rb") as f:
                #     df = pd.read_csv(f, encoding="utf_16", sep=',', low_memory=False, skip_blank_lines=True)
                #     excelWrite = pd.ExcelWriter('C:\\Users\\vix10\\Downloads\\output.xlsx', engine='xlsxwriter')
                #     df.to_excel(excelWrite, index=None)
                #     excelWrite.close()
                

                ################### Obtencion de FECHA

                fechaHRA = datetime.datetime.now()
                fechaHRA = str(fechaHRA)
                fechaHRA = fechaHRA.replace(":", "")
                nArchivo = 'Extraccion '+ tExtraccion + ' ' + fechaHRA + '.CSV'

                archivoO = 'C:\\Users\\vix10\\Downloads\\output.CSV'
                archivoNew = 'C:\\Users\\vix10\\Downloads\\' + nArchivo

                os.rename(archivoO, archivoNew)

                ################### CONFIGURACION FTP

                ftp_servidor = '192.168.50.37'
                ftp_usuario  = 'rpaback1'
                ftp_clave    = 'Cyber123'
                ftp_raiz     = '/Extracciones'

                ################## DATOS DEL FICHERO A SUBIR

                ficheroOrigen = archivoNew
                ficheroDestino = nArchivo

                ################# Conexion al FTP

                try:

                    s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
                    try:
                        api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], 'Procesando', '', info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 75)
                        f = open(ficheroOrigen, 'rb')
                        s.cwd(ftp_raiz)
                        s.storbinary('STOR ' + ficheroDestino, f)
                        f.close()
                        s.quit()
                    except:
                        print("No se ha podido encontrar el fichero" + ficheroOrigen)
                
                except Exception as e:
                    print("No se ha podido   con el servidor" + ftp_servidor)
                    
                print('Archivo cargado a la FTP')
                if "null" not in correo:
                    try: 
                        print('Se hara el envio de la extraccion')
                        sleep(10)
                        # Parametros del correo
                        remitente = 'extracciones@wincall.mx'
                        # destinatario = correo
                        destinatario = correo
                        asunto = 'Extraccion: ' + tExtraccion
                        cuerpo = 'Notificacion Extracion Exitosa   Extraccion: ' + tExtraccion
                        path = 'C:\\Users\\vix10\\Downloads\\' + nArchivo
                        nombreAdjunto = nArchivo

                        # Creacion del objeto mensaje
                        mensaje = MIMEMultipart()
                        
                        try:
                            # Atributos del mensajs
                            mensaje['From'] = remitente
                            mensaje['To'] = destinatario
                            mensaje['Subject'] = asunto

                            # Se agrega el cuerpo del mensaje como objeto MIME de tipo texto
                            mensaje.attach(MIMEText(cuerpo, 'plain'))

                            # Manejo del archivo a adjuntar
                            # archivoAdjunto = open(path, 'rb')
                            # adjuntoMIME = MIMEBase('application', 'octet-stream')
                            # adjuntoMIME.set_payload((archivoAdjunto).read())
                            # encoders.encode_base64(adjuntoMIME)
                            # adjuntoMIME.add_header('Content-Disposition', 'attachment; filename= %s' % nombreAdjunto)
                            # mensaje.attach(adjuntoMIME)
                            # archivoAdjunto.close()

                            # Se genera conexion y configuracion del servidor
                            try:
                                sesionSMTP = smtplib.SMTP_SSL('mail.wincall.mx', 465)
                                sesionSMTP.login('extracciones@wincall.mx', 'Fx1rOeoaf3DW')
                                texto = mensaje.as_string()
                                sesionSMTP.sendmail(remitente, destinatario, texto)
                                sesionSMTP.quit()
                            except Exception as e:
                                error = 'Error Envio Correo'
                                print(error)
                                cont = 0
                                dir = os.listdir('C:\\Users\\vix10\\Downloads')
                                for x in dir:
                                    if 'output.CSV' in x or 'output.csv' in x:
                                        print('Archivo a eliminar: ', x)
                                        os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                                        cont += 1
                                    elif 'Extraccion' in x:
                                        print('Archivo a eliminar: ', x)
                                        os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                                        cont += 1
                                    
                                    if cont == 2:
                                        break 
                                print(e)
                                sleep(1000)
                                return False, '-',

                        except Exception as e:
                            print(e)
                            continue
                            
                        cont = 0
                        dir = os.listdir('C:\\Users\\vix10\\Downloads')
                        for x in dir:
                            if 'output.CSV' in x or 'output.csv' in x:
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
                        print('Extraccion finalizada')
                        api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], 'Procesando', '', info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 100)
                        return True, nArchivo,'Completado'
                    except Exception as e:
                        print(e)
                        sleep(1000)

                else:
                    cont = 0
                    dir = os.listdir('C:\\Users\\vix10\\Downloads')
                    for x in dir:
                        if 'output.CSV' in x or 'output.csv' in x:
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
                    print('Extraccion finalizada')
                    api.extraccion_cerrada(info['id'], info['tipoExtraccion'], info['fechaExtraccion'], info['parametrosExtraccion'], '-', info['cve_usuario'], info['fechaCompletado'], 'Procesando', '', info['horaProgramacion'], info['nombreCron'], info['scheduleExpression'], info['tipoProgramacion'], info['correo'], info['medioExtraccion'], 100)
                    return True, nArchivo,'Completado'
                    
            else:
                print('Extraccion en PROCESO: ', str(intentosExtraccion) )
                intentosExtraccion += 1

                if intentosExtraccion == 105:
                    error = 'Error Falla al Extraer'
                    print(error)
                    return False, '-',error
    except:
        error = 'Error Procesando'
        return False, '-', error

def busquedaExtraccion(driver, extraccion):
    buscandoExtraccion = True
    contador = 1
    
    while buscandoExtraccion == True:
        elemExtraccion = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[{str(contador)}]/a")
        elemExtraccion = elemExtraccion.get_attribute('title')
        print('Buscando: <',elemExtraccion)
        sleep(1)
        if extraccion in elemExtraccion:
            buscandoExtraccion = False
            return str(contador)
        else:
            contador += 1

def busquedaTExtraccion(driver, extraccion):

    buscandoExtraccion = True
    contador = 0

    while buscandoExtraccion == True:
        try:
            contador += 1
            nameExtraccion = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[{str(contador)}]/a")
            nameExtraccion = nameExtraccion.text
            sleep(2)
            if extraccion in nameExtraccion:
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[{str(contador)}]/a").click()
                sleep(5)
                buscandoExtraccion = False
                return True, ''
        except:
            contador += 1
            if contador == 10:
                error = 'Error Tipo Extraccion No Encontrada'
                print(error)
                return False, error

            

def pantalla_extracion(driver, datos, tExtraccion, diasVencidos, viaExtraccion):
    try:
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

        #Entra a la ventana del tipo de extraccion

        if 'false' in viaExtraccion:
            if 'Casos de negocio' in tExtraccion:
                print('Extraccion: ' + tExtraccion)
                casosNegocio = busquedaExtraccion(driver, 'Casos de negocio')
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[{casosNegocio}]/a").click()
                resultado = extCasosNegocio(driver,datos, diasVencidos)
                if resultado != True:
                    return resultado, False

            elif 'Actividades' in tExtraccion:
                print('Extraccion: ' + tExtraccion)
                actividades = busquedaExtraccion(driver, 'Actividades')
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[{actividades}]/a").click()
                resultado = extActividades(driver,datos, diasVencidos)
                if resultado != True:
                    return resultado, False

            elif 'Ordenes de servicio' in tExtraccion:
                print('Extraccion: ' + tExtraccion)
                ordenesServicio = busquedaExtraccion(driver, 'Ordenes de Servicio')
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[{ordenesServicio}]/a").click()
                resultado = extOrdeneServicio(driver,datos, diasVencidos)
                if resultado != True:
                    return resultado, False
            
            else:
                error = 'Error Extraccion Invalida'
                print(error)
                return error, False
        
        else:
            
            casosNegocio = busquedaExtraccion(driver, 'Extracción de Datos')
            driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[{casosNegocio}]/a").click()
            sleep(5)
            driver.find_element(By.XPATH, f'//*[@id="s_sctrl_tabView_noop"]').click()

            if 'Casos de negocio' in tExtraccion:
                busquedaTExtraccion(driver, 'Lista de Casos de Negocio')
                print('Extraccion: ' + tExtraccion)
                resultado = extCasosNegocio2(driver,datos, diasVencidos)
                if resultado != True:
                    return resultado, False

            elif 'Actividades' in tExtraccion:
                busquedaTExtraccion(driver, 'Lista de Actividades')
                print('Extraccion: ' + tExtraccion)
                resultado = extActividades2(driver,datos, diasVencidos)
                if resultado != True:
                    return resultado, False

            elif 'Ordenes de servicio' in tExtraccion:
                busquedaTExtraccion(driver, 'Lista de Ordenes de Servicio')
                print('Extraccion: ' + tExtraccion)
                resultado = extOrdeneServicio2(driver,datos, diasVencidos)
                if resultado != True:
                    return resultado, False

        print('Se ingreso la extraccion')

        return driver, True
    except Exception as e:
        print(e)
        return 'Error Procesando', False

#########################################################################################################

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
    
    