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
from datetime import datetime, timedelta
import ftplib
import pandas as pd
import autoit as ai

#---------Mis funciones---------------#


from utileria import *
from logueo import *
from rutas import *

from myFunctions import  AlertaSaldoVencido

#########################################################################################################
## NOTA. YA SOLO FALTA PROBAR

def deteccionPantalla(driver, titExtraccion, selectTodos, opcTodos):
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
            driver.find_element(By.XPATH, selectTodos).click()
            driver.find_element(By.XPATH, opcTodos).click()
    
    except Exception:
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
    
    if 'Cuenta' in tExtraccion:
        
        estatus = parametrosExtraccion[0].split('"estado":')
        if '""' in estatus[1] : estatus = ''
        else: estatus = estatus[1]

        tipo = parametrosExtraccion[1].split('"tipo":')
        if '""' in tipo[1] : tipo = ''
        else: tipo = tipo[1]

        subTipo = parametrosExtraccion[2].split('"subtipo":')
        if '""' in subTipo[1] : subTipo = ''
        else: subTipo = subTipo[1]

        canalIngreso = parametrosExtraccion[3].split('"canalIngreso":')
        if '""' in canalIngreso[1] : canalIngreso = ''
        else: canalIngreso = canalIngreso[1]

        parametrosFinales = {
            'estatus':estatus,
            'tipo':tipo,
            'subTipo':subTipo,
            'canalIngreso':canalIngreso
        }

        return parametrosFinales

    elif 'Casos de negocio' in tExtraccion:

        fechaApertura = parametrosExtraccion[0].split('"fechaApertura":')
        if '""' in fechaApertura[1] : fechaApertura = '' 
        else: fechaApertura = fechaApertura[1]
        fechaApertura = fechaApertura.replace('"','')
        print(fechaApertura)

        estado = parametrosExtraccion[1].split('"estado":')
        if '""' in estado[1] : estado = ''
        else: estado = estado[1]
        print(estado)

        cuenta = parametrosExtraccion[2].split('"cuenta":')
        if '""' in cuenta[1] : cuenta = '' 
        else: cuenta = cuenta[1]
        print(cuenta)

        medioContacto = parametrosExtraccion[3].split('"medioContacto":')
        if '""' in medioContacto[1] : medioContacto = '' 
        else: medioContacto = medioContacto[1]
        print(medioContacto)

        numCaso = parametrosExtraccion[4].split('"casoNegocio":')
        if '""' in numCaso[1] : numCaso = '' 
        else: numCaso = numCaso[1]
        print(numCaso)

        categoria = parametrosExtraccion[5].split('"categoria":')
        if '""' in categoria[1] : categoria = '' 
        else: categoria = categoria[1]
        print(categoria)

        motivo = parametrosExtraccion[6].split('"motivo":')
        if '""' in motivo[1] : motivo = '' 
        else: motivo = motivo[1]
        print(motivo)
        
        motivoCliente = parametrosExtraccion[9].split('"motivoCliente":')
        if '""' in motivoCliente[1] : motivoCliente = '' 
        else: motivoCliente = motivoCliente[1]
        print(motivoCliente)

        subMotivo = parametrosExtraccion[7].split('"subMotivo":')
        if '""' in subMotivo[1] : subMotivo = '' 
        else: subMotivo = subMotivo[1]
        print(subMotivo)

        solucion = parametrosExtraccion[8].split('"solucion":')
        if '""' in solucion[1] : solucion = '' 
        else: solucion = solucion[1]
        print(solucion)

        

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
        if '""' in estado[1] : estado = '' 
        else: 
            estado = estado[1]
            estado = estado.replace('"','')
        print(estado)

        areaConocimiento = parametrosExtraccion[1].split('"areaConocimiento":')
        if '""' in areaConocimiento[1] : areaConocimiento = '' 
        else: 
            areaConocimiento = areaConocimiento[1]
            areaConocimiento = areaConocimiento.replace('"','')
        print(areaConocimiento)

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
        if '""' in cuenta[1] : cuenta = '' 
        else: cuenta = cuenta[1]

        compañia = parametrosExtraccion[1].split('"compania":')
        if '""' in compañia[1] : compañia = '' 
        else: compañia = compañia[1]

        telefonos = parametrosExtraccion[2].split('"telefonos":')
        if '""' in telefonos[1] : telefonos = '' 
        else: telefonos = telefonos[1]

        numeroOrden = parametrosExtraccion[3].split('"numOrden":')
        if '""' in numeroOrden[1] : numeroOrden = '' 
        else: numeroOrden = numeroOrden[1]

        tipoOrden = parametrosExtraccion[4].split('"tipoOrden":')
        if '""' in tipoOrden[1] : tipoOrden = '' 
        else: 
            tipoOrden = tipoOrden[1]
            tipoOrden = tipoOrden.replace('"','')
            print(tipoOrden)
        
        fechaOrden = parametrosExtraccion[5].split('"fechaOrden":')
        if '""' in fechaOrden[1] : fechaOrden = '' 
        else: 
            fechaOrden = fechaOrden[1]
            fechaOrden = fechaOrden.replace('"', '')
            print(fechaOrden)

        estado = parametrosExtraccion[6].split('"estado":')
        if '""' in estado[1] : estado = '' 
        else: 
            estado = estado[1]
            estado = estado.replace('"','')
            print(estado)

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

def validacionOrdenServicio(driver):

    print('-> Validacion Tipo')
    tipo = driver.find_element(By.XPATH, ordenes_servicio['tipo'])
    tipo = tipo.get_attribute("value")
    print('Tipo: ', tipo)

    if tipo.upper() not in ['INSTALACION', 'CAMBIO DE DOMICILIO', 'CAMBIO DE SERVICIOS', 'CAMBIO DE UBICACION']:
        error = 'Error Tipo Orden'
        return False, error

    print('-> Validacion Estado')
    estado = driver.find_element(By.XPATH, ordenes_servicio['estado']+'/input')
    estado = estado.get_attribute("value")
    print('Estado: ', estado)


    if estado.upper() not in ['ABIERTA', 'ABIERTO']:
        error = 'Error Estado Orden'
        return False, error
    else:
        print('VALIDACIONES EXITOSAS')

        return True, ''

def lecturaOpciones(driver):
    buscandoCancelar = True
    contador = 0

    while buscandoCancelar == True:
        try:
            contador += 1
            opcionorden = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/ul[5]/li[{str(contador)}]/div')
            opcionorden = opcionorden.text
            if 'Cancelado' in opcionorden or 'Cancelar' in opcionorden:
                driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div/div[8]/ul[5]/li[{str(contador)}]/div').click()
                buscandoCancelar = False
                print('dentro')
        except:
            print('buscando opcion')
            if contador == 20:
                error = 'Error Opcion Cancelar NO Detectada'
                print(error)
                buscandoCancelar = False
                return False, error

def extOrdeneServicio(driver, datos):

    print('Fun Extraccion Ordenes servicio')
    wait = WebDriverWait(driver,120)

    #Espera a que la página tenga el titulo de Home 
    element = wait.until(EC.title_contains('Todos los pedidos'))

    #LUPA DE BUSQUEDA
    status_open = open_item_selenium_wait(driver, xpath=ordenes_servicio['lupa'])
    if status_open == False:
        description_error('03','pantalla_extraccion','No se encontró la lupa de búsqueda')
        return status_open

    #Numero Orden
    sleep(5)
    nOrden = driver.find_element(By.XPATH, ordenes_servicio['nOrden'])
    nOrden.send_keys(datos)
    nOrden.send_keys(Keys.RETURN)

def ordenesServicio(driver, datos):

    
    result = open_item_selenium_wait(driver, xpath = ordenes_servicio['OS'])
    if result == False:
        return False, 'Pendiente', ''

    result = extOrdeneServicio(driver,datos)
    if result == False:
        return False, 'Pendiente', ''
    

    busquedaOS = True
    contador = 0
    while busquedaOS == True:
        try:
            sleep(5)
            fechaSolicitada = driver.find_element(By.XPATH, ordenes_servicio['fechaSolicitada'])
            fechaSolicitada = fechaSolicitada.text
            print('Fecha solicitada')
            sleep(2)
            driver.find_element(By.XPATH, ordenes_servicio['enlaceOrden']).click()
            busquedaOS = False
            print('ORDEN ENCONTRADA')
            sleep(10)
        except Exception:
            contador += 1
            if contador == 5:
                busquedaOS = False
                error = 'Error Orden NO Encontrada'
                return False, error,'Sin Tipo'
            sleep(5)


    status, resultado = validacionOrdenServicio(driver)
    if status == False:
        error = 'No Aplica Orden ya completa o cancelada'
        print(error)
        return False,error, 'Sin Tipo'
    
    print('Validacion Fecha')
    # fechaSolicitada = driver.find_element(By.XPATH, ordenes_servicio['fechaSolicitada'])
    # fechaSolicitada = fechaSolicitada.get_attribute("value")
    
    if len(fechaSolicitada) == 0:
        error = "Error Sin Fecha Solicitada"
        print(error)
        return False,error, 'Sin Tipo'

    fechaSolicitada = datetime.strptime(fechaSolicitada, "%d/%m/%Y %H:%M:%S").date()
    fechaActual = datetime.now().date()

    if fechaSolicitada > fechaActual:
        error = 'No Aplica Orden Reprogramada'
        print(error)
        return False, error,'Sin Tipo'

    else:

        diferenciaFechas = fechaActual - fechaSolicitada
        print('Diferencia de días {} con la fecha ACTUAL'.format(diferenciaFechas))

        if diferenciaFechas <= timedelta(days=6):
            cn = 'Tipo 1'
            print('Caso de Negocio: ', cn)
            return True,'Cerrado', cn
        else:
            if diferenciaFechas >= timedelta(days=7):
                cn = 'Tipo 2'
                print('Caso de Negocio: ', cn) #LP Cancelada por antigüedad

                driver.find_element(By.XPATH, ordenes_servicio['comentario']).click()
                comentario = driver.find_element(By.XPATH, ordenes_servicio['comentario'] + '/textarea')
                comentario.clear()
                comentario.send_keys('CANCELADA POR ANTIGUEDAD')

                driver.find_element(By.XPATH, ordenes_servicio['motivoCancelacion']).click()
                motivoCancelacion = driver.find_element(By.XPATH, ordenes_servicio['motivoCancelacion'] + '/input')
                motivoCancelacionVal = motivoCancelacion.get_attribute("value")
                if 'Cliente no contactado' not in motivoCancelacionVal:
                    motivoCancelacion.clear()
                    motivoCancelacion.send_keys('Cliente no contactado')
                    motivoCancelacion.send_keys(Keys.ENTER)

                try:
                    driver.find_element(By.XPATH, ordenes_servicio['estado']).click()
                    sleep(2)
                    driver.find_element(By.XPATH, ordenes_servicio['listaEstados']).click()
                    sleep(2)
                    # driver.find_element(By.XPATH, ordenes_servicio['canceladoE']).click()
                    # sleep(2)
                    lecturaOpciones(driver)
                    #estado.send_keys(Keys.TAB)
                
                except Exception as e:
                    print(e)
                    error = 'Error Inconsistencia Orden'
                    print(error)
                    return False, error, cn

                    


                sleep(3)
                # driver.find_element(By.XPATH, ordenes_servicio['motivoCancelacion']).click()
                # 

                
                estado = driver.find_element(By.XPATH, ordenes_servicio['estado'] + '/input')
                estado = estado.get_attribute("value")

                if len(estado) == 0 or 'Cancelado' not in estado:
                    estado = driver.find_element(By.XPATH, ordenes_servicio['estado'] + '/input')
                    estado.send_keys(Keys.ALT + Keys.ARROW_LEFT)
                    estado.send_keys(Keys.ALT + Keys.ARROW_LEFT)
                    estado.send_keys(Keys.ALT + Keys.ARROW_LEFT)
                    estado.send_keys(Keys.ALT + Keys.ARROW_LEFT)

                    error = 'Error Inconsistencia Orden'
                    print(error)
                    return False, error, cn

                print('SE CANCELO LA ORDEN')
                return True,  'Orden Cancelada',cn
    
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
            if 'FTTH,' in alert_txt: 
                alert.accept()
                print('alert Cerrado')
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

        except Exception as e: print(str(e)); return False
    

def generacionCasoNegocio(driver, tipoCN, cuenta, motivoCliente):#50485788
    try:

        if 'FAX/CONTESTADORA' in motivoCliente.upper(): motivoCliente = 'BUZON DE VOZ'
        elif 'OCUPADO' in motivoCliente.upper(): motivoCliente = 'OCUPADO'
        elif 'NO CONTESTA' in motivoCliente.upper() or 'ABANDONO' in motivoCliente.upper(): motivoCliente = 'NO CONTESTA'
        elif 'NO PROCESADO' in motivoCliente.upper() or 'ERROR' in motivoCliente.upper(): motivoCliente = 'TEL NO ENLAZA'
        elif 'NUMERO INVALIDO' in motivoCliente.upper(): motivoCliente = 'TEL NO EXISTE'

        print('INGRESAR CUENTA')

        status_pantalla_unica = pantalla_unica_consulta(driver, cuenta)
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '.')
            return False, 'Error Cuenta no valida', '', ''

        print('CREAR CASO NEGOCIO')
        btn_creacion_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Casos de Negocio Applet de lista:Nuevo')
        if btn_creacion_Ajuste == False: return False, 'Error Crear CN', '-', '-'

        elemento_monto_Ajuste, res = cargandoElemento(driver, 'input', 'aria-label', 'Solución')
        if elemento_monto_Ajuste == False: return False, 'Error Crear CN', '-', '-'
        
        #Categoria
        elemento_categoria, res = cargandoElemento(driver, 'input', 'aria-label', 'Categoria')
        if elemento_categoria == False: 
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'
        
        categoriaCN = driver.find_element_by_xpath("//input[@aria-label='Categoria']")
        categoriaCN.clear()
        categoriaCN.send_keys('VALIDACION')
        categoriaCN.send_keys(Keys.RETURN)
        print('<<<<<<<<<<<<<<<< CATEGORIA INGRESADA >>>>>>>>>>>>>>>>>>><')

        #Motivo
        elemento_motivo, res = cargandoElemento(driver, 'input', 'aria-label', 'Motivo')
        if elemento_motivo == False: 
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'

        motivoCN = driver.find_element_by_xpath("//input[@aria-label='Motivo']")
        motivoCN.clear()
        motivoCN.send_keys('SEGUIMIENTO')
        motivoCN.send_keys(Keys.RETURN)
        print('<<<<<<<<<<<<<<<< MOTIVO INGRESADA >>>>>>>>>>>>>>>>>>><')

        #Submotivo
        elemento_subMotivo, res = cargandoElemento(driver, 'input', 'aria-label', 'Submotivo')
        if elemento_subMotivo == False: 
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'
        
        subMotivoCN = driver.find_element_by_xpath("//input[@aria-label='Submotivo']")
        subMotivoCN.clear()
        subMotivoCN.send_keys('CLIENTE NO CONTACTADO')
        subMotivoCN.send_keys(Keys.RETURN)
        print('<<<<<<<<<<<<<<<< SUBMOTIVO INGRESADA >>>>>>>>>>>>>>>>>>><')

        #Solucion
        elemento_solucion, res = cargandoElemento(driver, 'input', 'aria-label', 'Solución')
        if elemento_solucion == False:  
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'

        solucionCN = driver.find_element_by_xpath("//input[@aria-label='Solución']")
        solucionCN.clear()
        solucionCN.send_keys('NO CONTACTADO')
        solucionCN.send_keys(Keys.RETURN)
        print('<<<<<<<<<<<<<<<< SOLUCION INGRESADA >>>>>>>>>>>>>>>>>>><')

        #Motivo Cliente
        elemento_motivoCliente, res = cargandoElemento(driver, 'input', 'aria-label', 'Motivo Cliente')
        if elemento_motivoCliente == False: 
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'

        motivoClienteCN = driver.find_element_by_xpath("//input[@aria-label='Motivo Cliente']")
        motivoClienteCN.clear()
        motivoClienteCN.send_keys(motivoCliente)
        motivoClienteCN.send_keys(Keys.RETURN)
        print('<<<<<<<<<<<<<<<< MOTIVO CLIENTE INGRESADA >>>>>>>>>>>>>>>>>>><')

        #Comentario
        valComentario = ''
        if 'Tipo 1' in tipoCN: valComentario = 'NO CONTESTA'
        else: valComentario = 'CANCELADA POR ANTIGUEDAD'

        elemento_, res = cargandoElemento(driver, 'textarea', 'aria-label', 'Comentarios')
        if elemento_ == False: 
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'
        
        comentarioCN = driver.find_element_by_xpath("//textarea[@aria-label='Comentarios']")
        comentarioCN.clear()
        comentarioCN.send_keys(valComentario)
        print('<<<<<<<<<<<<<<<< COMENTARIO INGRESADA >>>>>>>>>>>>>>>>>>><')

        #Motivo del Cierre
        elemento_, res = cargandoElemento(driver, 'input', 'aria-label', 'Motivo del Cierre')
        if elemento_ == False: 
            if 'No aplica' in res: return False, res, '-', '-'
            return False, 'Error Crear CN', '-', '-'
        
        motivoCierreCN = driver.find_element_by_xpath("//input[@aria-label='Motivo del Cierre']")
        motivoCierreCN.clear()
        motivoCierreCN.send_keys('RAC INFORMA Y SOLUCIONA')
        motivoCierreCN.send_keys(Keys.RETURN)
        print('<<<<<<<<<<<<<<<< MOTIVO CIERRE INGRESADA >>>>>>>>>>>>>>>>>>><')
        sleep(3)

        cnNuevo = driver.find_element(By.XPATH, caso_negocio['cnNuevo'])
        cnNuevo = cnNuevo.get_attribute("value")

        #Estado
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]').click()
        sleep(10)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span').click()
        sleep(5)

        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: return False, 'Error Pantalla NO Carga', '-', '-'
        
        driver.find_element(By.XPATH, pathEstadoCNOpc.replace('{contador}', posicion)).click()
        sleep(5)
        
        driver.find_element(By.XPATH, "//button[@aria-label='Casos de negocio Applet de formulario:Guardar']").click()
        print('CN Guardado')
        sleep(7)

        return True, '', cnNuevo, 'Cerrado'

    except Exception:
        error = 'Error Crear CN'
        print(error)
        alert = Alert(driver)
        alertText = alert.text
        alert.accept()

        driver.find_element(By.XPATH, caso_negocio['cancelar']).click()
        return False, error, '-', '-'

#########################################################################################################
