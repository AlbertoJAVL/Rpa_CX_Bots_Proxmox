#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException,NoAlertPresentException
import autoit as it
#---------import logging
#-------------System-------------------#
from time import sleep
import os
import win32clipboard as cp
import  datetime
from datetime import datetime, timedelta
#---------Mis funciones---------------#
from utileria import *
from logueo import *
import Services.ApiCyberHubOrdenes as api
from rutasPreProduccion import *

#---------Variables globales---------------#

FORMATO_FECHA = "%Y/%m/%d %H:%M"
FORMATO_FECHA_INVERT = "%d/%m/%Y %H:%M"



################### FUNCION NUEVA

def cargandoElemento(driver, elemento, atributo, valorAtributo, path = False):

    cargando = True
    contador = 0

    while cargando:

        sleep(3)
        try: 
            print('Validando posible warning')
            contador += 1
            alert = Alert(driver)
            alert_txt = alert.text
            print(f'♦ {alert_txt} ♦')
            if 'Cuenta en cobertura FTTH,' in alert_txt: 
                alert.accept()
                print('aqui')
                # return True, ''
            else: return False, f'Inconsistencia Siebel: {alert_txt}'            
        
        except:
            try:
                print('Esperando a que el elemento cargue')
                if path == False: 
                    driver.find_element(By.XPATH, f"//{elemento}[@{atributo}='{valorAtributo}']").click()
                    return True, ''
                else: 
                    print('aqui')
                    driver.find_element(By.XPATH, path).click()
                    return True, ''
            except:
                print('Pantalla Cargando')
                if contador == 70: return False, ''

def obtencionColumna(driver, nombreColumna, path, path2 = False):

    buscandoColumna = True
    contador = 0

    while buscandoColumna:

        try:
            contador += 1
            nameColumna2 = 'False'
            pathF = path.replace('{contador}', str(contador))

            try:
                nameColumna = driver.find_element(By.XPATH, pathF)
                nameColumna = driver.execute_script("return arguments[0].textContent;", nameColumna)
                print(f'path1: {nameColumna}')
            except: nameColumna = 'False'

            if path2 != False: 
                try:
                    pathF2 = path2.replace('{contador}', str(contador))
                    nameColumna2 = driver.find_element(By.XPATH, pathF2)
                    nameColumna2 = driver.execute_script("return arguments[0].textContent;", nameColumna2)
                except: nameColumna2 = 'False'
                print(f'path2: {nameColumna2}')

            if nombreColumna in nameColumna or nombreColumna in nameColumna2: return str(contador)
            else:
                if contador == 100: return False

        except Exception as e: 
            logger = logging.getLogger("rpa")
            logger.exception("Fallo en orden %s: %s", e) 
            print(str(e));return False

def ingresoBusquedaAjuste(driver, campoBusqueda, busqueda, pathColumnasBAjuste, pathColumnasBAjuste2, pathColumnasBAInput, pathColumnasBAInput2, pathColumnasBAInput3):
    posicion = obtencionColumna(driver, campoBusqueda, pathColumnasBAjuste, pathColumnasBAjuste2)
    if posicion == False: return False
    
    try: 
        driver.find_element(By.XPATH, pathColumnasBAInput.replace('{contador}', posicion).replace('/input[2]', '')).click()
        sleep(1)
        numeroInputajuste = driver.find_element(By.XPATH, pathColumnasBAInput.replace('{contador}', posicion))
    except: 
        try:
            driver.find_element(By.XPATH, pathColumnasBAInput2.replace('{contador}', posicion).replace('/input', '')).click()
            sleep(1)
            numeroInputajuste = driver.find_element(By.XPATH, pathColumnasBAInput2.replace('{contador}', posicion))
        except: 
            driver.find_element(By.XPATH, pathColumnasBAInput3.replace('{contador}', posicion).replace('/input', '')).click()
            sleep(1)
            numeroInputajuste = driver.find_element(By.XPATH, pathColumnasBAInput3.replace('{contador}', posicion))
    
    numeroInputajuste.send_keys(busqueda)
    numeroInputajuste.send_keys(Keys.ENTER)
    return posicion



#################################

def ingresarDatos(driver, input, xpath):
    driver.find_element(By.XPATH, xpath).click()
    sleep(3)

    try:

        campo = driver.find_element(By.XPATH, xpath + '/div/input')
        campo.clear()           
        sleep(2)        
        campo.send_keys(input)    
        campo.send_keys(Keys.RETURN)          
    
    except Exception:

        try:
            campo = driver.find_element(By.XPATH, xpath + '/span/input')
            campo.clear()           
            sleep(2)        
            campo.send_keys(input)    
            campo.send_keys(Keys.RETURN)          
        
        except Exception:

            try:
                campo = driver.find_element(By.XPATH, xpath + '/span/textarea')
                campo.clear()           
                sleep(2)        
                campo.send_keys(input)    
                campo.send_keys(Keys.RETURN)  

            except Exception:
                campo = driver.find_element(By.XPATH, xpath + '/div/textarea')
                campo.clear()                   
                campo.send_keys(input)         
                campo.send_keys(Keys.RETURN)    

def generacionCN(driver):

    try:
        sleep(30)

        text_box('INICIA CREACION CASO DE NEGOCIO', '▬')

        #Creacion CN
        btn_creacion_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Casos de Negocio Applet de lista:Nuevo')
        if btn_creacion_Ajuste == False: 
            if 'Inconsistencia' in res: return False, res, ''
            else: return False, 'Registro pendiente', ''

        elemento_monto_Ajuste, res = cargandoElemento(driver, 'input', 'aria-label', 'Solución')
        if elemento_monto_Ajuste == False: 
            if 'Inconsistencia' in res: return False, res, ''
            else: return False, 'Registro pendiente', ''
        ################################
        #Categoria
        textoLabelCategoriaCN = 'Categoria'
        driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelCategoriaCN + "']").click()
        categoriaCN = driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelCategoriaCN + "']")
        categoriaCN.clear()
        categoriaCN.send_keys('SERVICIOS')
        categoriaCN.send_keys(Keys.RETURN)
        sleep(3)

        #Motivo
        textoLabelMotivoCN = 'Motivo'
        driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelMotivoCN + "']").click()
        motivoCN = driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelMotivoCN + "']")
        motivoCN.clear()
        motivoCN.send_keys('ACLARACION DE ESTADO DE CUENTA')
        motivoCN.send_keys(Keys.RETURN)
        sleep(3)

        #Submotivo
        textoLabelSubMotivoCN = 'Submotivo'
        driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelSubMotivoCN + "']").click()
        subMotivoCN = driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelSubMotivoCN + "']")
        subMotivoCN.clear()
        subMotivoCN.send_keys('AJUSTE FACTURACION')
        subMotivoCN.send_keys(Keys.RETURN)
        
        sleep(3)
        #Solucion
        try:
            textoLabelsolucionCN = 'Solución'
            driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelsolucionCN + "']").click()
            solucionCN = driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelsolucionCN + "']")
            solucionCN.clear()
            solucionCN.send_keys('APLICA AJUSTE')
            solucionCN.send_keys(Keys.RETURN)
        except Exception:
            alerta = Alert(driver)
            textoAlerta = alerta.text

            if 'Ya existe un Caso de Negocio en proceso con esta tipificacion' in textoAlerta:
                alerta.accept()
                error = 'No aplica caso de negocio ya tipificado'
                textoLabelCancelarCN = 'Casos de negocio Applet de formulario:Cancelar'
                driver.find_element(By.XPATH,"//button[@aria-label='" + textoLabelCancelarCN + "']").click()
                return False, error,'-'
            else: return False, f'No aplica: {textoAlerta}', '-'
        
        sleep(3)
        #Comentario
        textoLabelcomentarioCN = 'Comentarios'
        driver.find_element(By.XPATH,"//textarea[@aria-label='" + textoLabelcomentarioCN + "']").click()
        comentarioCN = driver.find_element(By.XPATH,"//textarea[@aria-label='" + textoLabelcomentarioCN + "']")
        comentarioCN.clear()
        comentarioCN.send_keys('CN INFORMATIVO APLICACION AJUSTE BOT')
        
        sleep(3)
        #Motivo del Cierre
        textoLabelmotivoCierreCN = 'Motivo del Cierre'
        driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelmotivoCierreCN + "']").click()
        motivoCierreCN = driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelmotivoCierreCN + "']")
        motivoCierreCN.clear()
        motivoCierreCN.send_keys('RAC INFORMA Y SOLUCIONA')
        motivoCierreCN.send_keys(Keys.RETURN)
        
        sleep(3)
        #Motivo Cliente
        textoLabelmotivoClienteCN = 'Motivo Cliente'
        driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelmotivoClienteCN + "']").click()
        motivoClienteCN = driver.find_element(By.XPATH,"//input[@aria-label='" + textoLabelmotivoClienteCN + "']")
        motivoClienteCN.clear()
        motivoClienteCN.send_keys('CONVENIO COBRANZA')
        motivoClienteCN.send_keys(Keys.RETURN)
        

        cnGenerado = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[6]/div/span/div")
        cnGenerado = cnGenerado.text
        print('CN generado: ', cnGenerado)
        
        sleep(3)
        #Estado
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]').click()
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span').click()
        sleep(5)
        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: return 1, 'Error Pantalla NO Carga', '-'
        driver.find_element(By.XPATH, pathEstadoCNOpc.replace('{contador}', posicion)).click()

        sleep(6)


        elemento_monto_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Casos de negocio Applet de formulario:Guardar')
        if elemento_monto_Ajuste == False:
            if 'Inconsistencia' in res: return False, res, ''
            else:  return False, 'Registro pendiente', ''

        elemento_monto_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Casos de Negocio Menú List')
        if elemento_monto_Ajuste == False:
            if 'Inconsistencia' in res: return False, res, ''
            else:  return False, 'Registro pendiente', ''

        return True, '', cnGenerado


    except Exception as e:
        logger = logging.getLogger("rpa")
        logger.exception("Fallo en orden %s: %s", e)  
        print(e)
        error = 'Error al crear cn'
        return False,error, '-'

def busquedaCol(driver, colBusqueda):

    busquedaCol = True
    contador = 2
    while busquedaCol == True:
        nameColum =  driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div")
        nameColum = nameColum.text
        print(nameColum)
        if colBusqueda in nameColum:
            print('Columna encontrada: ', nameColum)
            return contador
        else:
            contador += 1
            sleep(2)

def validacionAjusteUsuario(driver, fechaCompletado):

    try:

        usuariosBots = ['CCINTBOAJUSTES1','CCINTBOAJUSTES2','CCINTBOAJUSTES3','CCINTBOAJUSTES4','CCINTBORPAAJUSTES']
        cargaPantalla, res = cargandoElemento(driver, '', '', '', path= "//*[contains(@aria-label,'Nº de solicitud')]")
        if cargaPantalla == False: 
            if 'Inconsistencia' in res: return False, res
            else: return False, 'Registro pendiente'

        usuarioAjuste  = driver.find_element(By.XPATH, "//input[@aria-label='Creado por']")
        usuarioAjuste = usuarioAjuste.get_attribute("value")
        print(f'Usuario del ajuste: {usuarioAjuste}')


        if usuarioAjuste in usuariosBots: 

            
            fechaAjuste  = driver.find_element(By.XPATH, "//input[@aria-label='Fecha de solicitud']")
            fechaAjuste = fechaAjuste.get_attribute("value")
            fechaAjuste = fechaAjuste[:10]
            fechaAjuste = datetime.strptime(fechaAjuste, '%d/%m/%Y')

            fechaCompletado = datetime.strptime(fechaCompletado, '%Y-%m-%d')
            fechaCompletado -= timedelta(days=1)
            print(fechaCompletado)
            print(fechaAjuste)

            if fechaAjuste >= fechaCompletado: 
                print('fechas iguales')
                driver.find_element(By.XPATH, f'//a[contains(text(), "Pantalla Única de Consulta:")]').click()
                cargaPantalla, res = cargandoElemento(driver, '', '', '', path= "//*[contains(@aria-label,'Perfil de Pago')]")
                if cargaPantalla == False: 
                    if 'Inconsistencia' in res: return False, res
                    else: return False, 'Registro pendiente'
                return True, 'BOT'
            else: return False, 'Externo'
            
        else: return False, 'Externo'

    except Exception as e:
        logger = logging.getLogger("rpa")
        logger.exception("Fallo en orden %s: %s", e)  
        print(e)
        return False, 'Inconsistencia siebel: Falla Lectura Usuario'

def profAjuste(driver, pathColumnasBAInput, posicionNumeroajuste, replaceVal, fechaCompletado):
    try:
        sleep(1.5)
        numeroAjuste = driver.find_element(By.XPATH, pathColumnasBAInput.replace('{contador}', posicionNumeroajuste).replace(replaceVal, ''))
        numeroAjuste = numeroAjuste.get_attribute("title")
        driver.find_element(By.XPATH, f'//a[contains(text(), "{numeroAjuste}")]').click()
        print(f'Profundizando ajuste: {numeroAjuste}')

        resultadoValidacion, estadoValidacion = validacionAjusteUsuario(driver, fechaCompletado)
        if resultadoValidacion == True: return numeroAjuste
        else: 
            if 'No aplica' in estadoValidacion: return estadoValidacion
            else: return ''

    except Exception as e:
        logger = logging.getLogger("rpa")
        logger.exception("Fallo en orden %s: %s", e) 
        return 'Registro pendiente'


def ajusteTipificado(driver, convenio, fecha, fechaCompletado):

    pathColumnasBAjuste = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'
    pathColumnasBAjuste2 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'

    pathColumnasBAInput = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input[2]'
    pathColumnasBAInput2 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input'
    pathColumnasBAInput3 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input'

    fechaN = fecha.replace("T", " ")
    fechaN = datetime.strptime(fechaN, "%Y-%m-%d %H:%M:%S").date()
    fechaN = fechaN.strftime("%d/%m/%Y")
    rangoFechaBusqueda = f">= '{fechaN}'"

    print(f'Validando Ajuste Previo: {convenio}')

    try:

        ajusteCarga, res = cargandoElemento(driver, 'button', 'aria-label', 'Solicitudes de Ajuste Applet de lista:Consulta')
        if ajusteCarga == False: 
            if 'Inconsistencia' in res: return False, res
            else: return False, 'Registro pendiente'
        sleep(10)

        posicionNumeroajuste = obtencionColumna(driver, 'Número de Ajuste', pathColumnasBAjuste, pathColumnasBAjuste2)
        if posicionNumeroajuste == False: return False, 'Registro pendiente'

        resultado = ingresoBusquedaAjuste(driver, 'Estado', 'Aplicado', pathColumnasBAjuste, pathColumnasBAjuste2, pathColumnasBAInput, pathColumnasBAInput2, pathColumnasBAInput3)
        if resultado == False: return False, 'Registro pendiente'
        
        resultado = ingresoBusquedaAjuste(driver, 'Motivo del ajuste', convenio, pathColumnasBAjuste, pathColumnasBAjuste2, pathColumnasBAInput, pathColumnasBAInput2, pathColumnasBAInput3)
        if resultado == False: return False, 'Registro pendiente'
        
        resultado = ingresoBusquedaAjuste(driver, 'Fecha del ajuste', rangoFechaBusqueda, pathColumnasBAjuste, pathColumnasBAjuste2, pathColumnasBAInput, pathColumnasBAInput2, pathColumnasBAInput3)
        if resultado == False: return False, 'Registro pendiente'

        print('♥ Buscando Ajuste ♥')
        sleep(10)

        try: 
            driver.find_element(By.XPATH, pathColumnasBAInput.replace('{contador}', resultado).replace('/input[2]', '')).click()
            print('Ajuste Detectado')

            resultadoProf = profAjuste(driver, pathColumnasBAInput, posicionNumeroajuste, '/input[2]', fechaCompletado)
            return True, resultadoProf

        except: 
            try:
                driver.find_element(By.XPATH, pathColumnasBAInput2.replace('{contador}', resultado).replace('/input', '')).click()
                print('Ajuste Detectado')
                
                resultadoProf = profAjuste(driver, pathColumnasBAInput2, posicionNumeroajuste, '/input', fechaCompletado)
                return True, resultadoProf

            except: 
                try: 
                    driver.find_element(By.XPATH, pathColumnasBAInput3.replace('{contador}', resultado).replace('/input', '')).click()
                    print('Ajuste Detectado')
                    
                    resultadoProf = profAjuste(driver, pathColumnasBAInput3, posicionNumeroajuste, '/input', fechaCompletado)
                    return True, resultadoProf
                except: return False, 'Sin ajustes Previos'
        
    except Exception as e:
        logger = logging.getLogger("rpa")
        logger.exception("Fallo en orden %s: %s", e) 
        print(e)
        return False, 'Registro pendiente'

def aplicacionAjuste(driver, fechaCompletado, monto, no_cuenta, tipoAjuste,motivoAjuste,ComentariosAjuste, fecha, statusPrevio, numeroAjuste):
    try:

        pathColumnasBAjuste = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'
        pathColumnasBAjuste2 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'

        pathColumnasBAInput = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input[2]'
        pathColumnasBAInput2 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input'
        pathColumnasBAInput3 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input'

        wait = WebDriverWait(driver, 120)
        act = webdriver.ActionChains(driver)
        text_box('AJUSTE', '▬')

        lupa_busqueda_cn, res = cargandoElemento(driver, 'a', 'title', 'Pantalla Única de Consulta')
        if lupa_busqueda_cn == False:
            if 'Inconsistencia' in res: return False, res, '', ''
            else:  return False, 'Registro pendiente', '', ''

        # Buscando Elemento
        lupa_busqueda_cn, res = cargandoElemento(driver, 'button', 'aria-label', 'Pantalla Única de Consulta Applet de formulario:Consulta')
        if lupa_busqueda_cn == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', '', ''

        lupa_busqueda_cn, res = cargandoElemento(driver, 'input', 'aria-label', 'Numero Cuenta')
        if lupa_busqueda_cn == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', '', ''

        inputNCta = driver.find_element(By.XPATH, "//input[@aria-label='Numero Cuenta']")
        inputNCta.send_keys(no_cuenta)
        inputNCta.send_keys(Keys.RETURN)

        cargaPantalla, res = cargandoElemento(driver, '', '', '', path= "//*[contains(@aria-label,'Perfil de Pago')]")
        if cargaPantalla == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', '', ''

        print('Validacion de ajuste previo tipificado')

        validacion, res2 = ajusteTipificado(driver, motivoAjuste, fecha, fechaCompletado)
        if res2 != 'Sin ajustes Previos':
            print(f'-> Resultado de ajuste previo: {res2}')
            if res2 == '': return False, 'No aplica ajuste reciente', '', ''
            elif res2 == 'Registro pendiente': return False, 'Registro pendiente', '', ''
            elif 'No aplica' in res2: return False, res2, '',''
            else: 
                sleep(5)
                textoLabelConsultarA = 'Pantalla Única de Consulta Applet de formulario:Consulta de Saldos'
                driver.find_element(By.XPATH,"//button[@aria-label='" + textoLabelConsultarA + "']").click()
                consulta = True
                sleep(30)
                return True, '', res2, 'Aplicado'

        print('se va a aplicar el ajuste')
        
        btn_creacion_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Solicitudes de Ajuste Applet de lista:Nuevo')
        if btn_creacion_Ajuste == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', '', ''

        elemento_monto_Ajuste, res = cargandoElemento(driver, 'input', 'aria-label', 'Importe del ajuste')
        if elemento_monto_Ajuste == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', '', ''
        print('♥ Generando Ajuste ♥')

        # Importe Ajuste
        input_importe = driver.find_element(By.XPATH, "//input[@aria-label='Importe del ajuste']")
        input_importe.click()
        sleep(1)
        input_importe.clear()
        input_importe.send_keys(str(monto))
        print('♦ Importe Ingresado ♦')

        input_aplicar = driver.find_element(By.XPATH, "//input[@aria-label='Aplicar']")
        input_aplicar.click()
        sleep(1)
        input_aplicar.send_keys(tipoAjuste)
        input_aplicar.send_keys(Keys.RETURN)
        print('♦ Aplicacion Ingresada ♦')

        input_motivo_ajuste = driver.find_element(By.XPATH, "//input[@aria-label='Motivo del ajuste']")
        input_motivo_ajuste.click()
        sleep(1)
        input_motivo_ajuste.send_keys(motivoAjuste)
        input_motivo_ajuste.send_keys(Keys.RETURN)
        print('♦ Motivo Ajuste Ingresado ♦')

        input_comentario = driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']")
        input_comentario.click()
        sleep(1)
        input_comentario.send_keys(ComentariosAjuste)
        print('♦ Comentario Ingresado ♦')

        numeroAjuste = driver.find_element(By.XPATH, "//input[@aria-label='Número de Ajuste']")
        numeroAjuste = numeroAjuste.get_attribute("value")
        print(f'Ajuste Generado: {numeroAjuste}')
        sleep(2)

        ajusteCarga, res = cargandoElemento(driver, 'button', 'aria-label', 'Solicitud de Ajuste Applet de formulario:Guardar')
        if ajusteCarga == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', numeroAjuste, ''
        print('♦ Ajuste Guardado ♦')
        sleep(5)

        # Envio Ajuste
        print('♥ Enviando Ajuste ♥')
        ajusteCarga, res = cargandoElemento(driver, 'button', 'aria-label', 'Solicitudes de Ajuste Applet de lista:Consulta')
        if ajusteCarga == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', numeroAjuste, ''

        posicion = obtencionColumna(driver, 'Número de Ajuste', pathColumnasBAjuste, pathColumnasBAjuste2)
        if posicion == False: return False, 'Registro pendiente', numeroAjuste, ''
        
        try: numeroInputajuste = driver.find_element(By.XPATH, pathColumnasBAInput.replace('{contador}', posicion))
        except: 
            try: numeroInputajuste = driver.find_element(By.XPATH, pathColumnasBAInput2.replace('{contador}', posicion))
            except: numeroInputajuste = driver.find_element(By.XPATH, pathColumnasBAInput3.replace('{contador}', posicion))
        
        numeroInputajuste.click()
        numeroInputajuste.send_keys(numeroAjuste)
        numeroInputajuste.send_keys(Keys.ENTER)
        print('♥ Buscando Ajuste ♥')
        sleep(5)
        
        ajusteCarga, res = cargandoElemento(driver, 'button', 'aria-label', 'Solicitudes de Ajuste Applet de lista:Enviar')
        if ajusteCarga == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', numeroAjuste, ''

        ajusteCarga, res = cargandoElemento(driver, 'button', 'aria-label', 'Enviar Ajuste Applet de formulario:Aceptar')
        if ajusteCarga == False: 
            if 'Inconsistencia' in res: return False, res, '', ''
            else: return False, 'Registro pendiente', numeroAjuste, ''

        print('♦ Ajuste Enviado ♦')
        sleep(10)

        contadorActivo = 0
        consulta = False
        while consulta == False:
            try:
                print('Validando posible warning')
                alert = Alert(driver)
                alert_txt = alert.text
                print(f'♦ {alert_txt} ♦')
                if 'Cuenta en cobertura FTTH,' in alert_txt: 
                    alert.accept()
                    print('aqui')
                elif 'NO ES POSIBLE APLICAR EL AJUSTE' in alert_txt: return False, 'Error Obtencion Status Ajuste', numeroAjuste, '-'
                else: return False, f'Inconsistencia Siebel: {alert_txt}', numeroAjuste, '-'
                
            except:
                try:
                    # driver.find_element(By.XPATH, pantalla_consultad['consultaSaldo']).click()
                    textoLabelConsultarA = 'Pantalla Única de Consulta Applet de formulario:Consulta de Saldos'
                    driver.find_element(By.XPATH,"//button[@aria-label='" + textoLabelConsultarA + "']").click()
                    consulta = True
                    sleep(30)
                except:
                    sleep(5)
                    contadorActivo += 1
                    if contadorActivo == 6:
                        print("no se encontro consulta de saldos actualizando a error")
                        error = 'Error al crear cn'
                        consulta = True
                        print(error)
                        return False, error, numeroAjuste, '-'
        
        return True, '',  numeroAjuste, 'Aplicado'


    except Exception as e:
        logger = logging.getLogger("rpa")
        logger.exception("Fallo en orden %s: %s", e) 
