#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import autoit as it
#-------------System-------------------#
from time import sleep
import os
import win32clipboard as cp
import  datetime
#---------Mis funciones---------------#
from utileria import *
from logueo import *
import Services.ApiCyberHubOrdenes as api
from rutas import *

#---------Variables globales---------------#

FORMATO_FECHA = "%Y/%m/%d %H:%M"
FORMATO_FECHA_INVERT = "%d/%m/%Y %H:%M"

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
        campo = driver.find_element(By.XPATH, xpath + '/div/textarea')
        campo.clear()                   
        campo.send_keys(input)         
        campo.send_keys(Keys.RETURN)   

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
    
def obtencionColumna(driver, nombreColumna, path):

    buscandoColumna = True
    contador = 1

    while buscandoColumna:

        try:
            pathF = path.replace('{contador}', str(contador))
            nameColumna = driver.find_element(By.XPATH, pathF)
            nameColumna = driver.execute_script("return arguments[0].textContent;", nameColumna)

            if nombreColumna in nameColumna: return str(contador)
            else:
                contador += 1
                if contador == 100: return False

        except: return False

def generacionCN(driver, cn, ajuste):

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

        #Categoria
        textoLabelCategoriaCN = 'Categoria'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelCategoriaCN + "']").click()
        categoriaCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelCategoriaCN + "']")
        categoriaCN.clear()
        categoriaCN.send_keys('SERVICIOS')
        categoriaCN.send_keys(Keys.RETURN)
        print('♦ Categoria Ingresada ♦')
        sleep(3)

        #Motivo
        textoLabelMotivoCN = 'Motivo'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMotivoCN + "']").click()
        motivoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMotivoCN + "']")
        motivoCN.clear()
        motivoCN.send_keys('ACLARACION DE ESTADO DE CUENTA')
        motivoCN.send_keys(Keys.RETURN)
        print('♦ Motivo Ingresado ♦')
        sleep(3)

        #Submotivo
        textoLabelSubMotivoCN = 'Submotivo'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelSubMotivoCN + "']").click()
        subMotivoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelSubMotivoCN + "']")
        subMotivoCN.clear()
        subMotivoCN.send_keys('AJUSTE FACTURACION')
        subMotivoCN.send_keys(Keys.RETURN)
        print('♦ Submotivo Ingresado ♦')
        sleep(3)

        #Solucion
        try:
            textoLabelsolucionCN = 'Solución'
            driver.find_element_by_xpath("//input[@aria-label='" + textoLabelsolucionCN + "']").click()
            solucionCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelsolucionCN + "']")
            solucionCN.clear()
            solucionCN.send_keys('APLICA AJUSTE')
            solucionCN.send_keys(Keys.RETURN)
        except Exception:
            try:
                alerta = Alert(driver)
                textoAlerta = alerta.text

                if 'Ya existe un Caso de Negocio en proceso con esta tipificacion' in textoAlerta:
                    alerta.accept()
                    error = 'No aplica caso de negocio ya tipificado'
                    textoLabelCancelarCN = 'Casos de negocio Applet de formulario:Cancelar'
                    driver.find_element_by_xpath("//button[@aria-label='" + textoLabelCancelarCN + "']").click()
                    return False, 'Error CN Previo','-'
                else: return False, f'Error Warning: {textoAlerta}', '-'
            except: pass


        sleep(3)
        #Comentario
        fechaActual = datetime.date.today()
        horaActual = datetime.datetime.now().time()
        ajuste = ajuste
        cnSeguimiento = cn
        comentario  = 'Fecha: {}\nHora: {}\nMotvio: Seguimiento a convenio de cobranza\nCantidad Ajustada: {}\nCN de Seguimiento: {}\n GNERADO POR BOT'.format(fechaActual,horaActual,ajuste, cnSeguimiento)
        textoLabelcomentarioCN = 'Comentarios'
        driver.find_element_by_xpath("//textarea[@aria-label='" + textoLabelcomentarioCN + "']").click()
        comentarioCN = driver.find_element_by_xpath("//textarea[@aria-label='" + textoLabelcomentarioCN + "']")
        comentarioCN.clear()
        comentarioCN.send_keys(comentario)

        # Obtencion CN
        noCN = driver.find_element(By.XPATH, f'//a[@name="SRNumber"]')
        noCN = noCN.text
        print(f'♦ CN Generado: {noCN} ♦')
        sleep(3)

        #Motivo del Cliente
        textoLabelmotivoCierreCN = 'Motivo del Cierre'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoCierreCN + "']").click()
        motivoCierreCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoCierreCN + "']")
        motivoCierreCN.clear()
        motivoCierreCN.send_keys('RAC INFORMA Y SOLUCIONA')
        motivoCierreCN.send_keys(Keys.RETURN)
        print('♦ Campo Motivo Cierre ♦')
        
        sleep(3)
        textoLabelmotivoClienteCN = 'Motivo Cliente'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoClienteCN + "']").click()
        motivoClienteCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoClienteCN + "']")
        motivoClienteCN.clear()
        motivoClienteCN.send_keys('CONVENIO COBRANZA')
        motivoClienteCN.send_keys(Keys.RETURN)
        print('♦ Campo Motivo Cliente ♦')
        sleep(3)
        
        #Estado
        driver.find_element(By.XPATH, casos_negocio['cnEstado']).click()
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span').click()
        sleep(5)
        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: return False, 'Error Pantalla NO Carga', '-'
        driver.find_element(By.XPATH, pathEstadoCNOpc.replace('{contador}', posicion)).click()
        sleep(5)

        driver.find_element(By.XPATH, "//button[@aria-label='Casos de negocio Applet de formulario:Guardar']").click()
        print('CN Guardado')

        return True, '', noCN


    except Exception as e:

        alert = Alert(driver)
        
        alert.accept()

        print(e)
        return False,'No aplica cn abierto',''

def validacionCN(driver, noCN):

    try:

        wait = WebDriverWait(driver,120)
        
        #Abrir Casos de Negocio
        sleep(10)
        print('Abriendo pantalla de casos de negocio')
        #
        driver.find_element(By.XPATH, casos_negocio['opcCN']).click()

        # elem = wait.until(EC.title_contains('Mis Ordenes Administrativas'))

        #Cambiar a todos CN
        # driver.find_element(By.XPATH, casos_negocio['selectTodos']).click()
        # driver.find_element(By.XPATH, casos_negocio['todosCN']).click()
        sleep(5)

        #Busqueda del CN
        print('BUSCANDO CN')
        # driver.find_element(By.XPATH, casos_negocio['busqueda']).click()
        texto_boton ='Casos de negocio Applet de lista:Consulta'
        driver.find_element_by_xpath("//button[@aria-label='" + texto_boton + "']").click()
            


        # driver.find_element(By.XPATH, casos_negocio['inputCN']).click()
        sleep(2)
        try:
            texto_boton ='s_2_l_SR_Number s_2_l_altLink'
            inputCN = driver.find_element_by_xpath("//input[@aria-labelledby='" + texto_boton + "']")
        except Exception as e:
            print(e)
            error='Error Busqueda CN'

        # inputCN = driver.find_element(By.XPATH, casos_negocio['inputCN'] + '/input')
        inputCN.send_keys(noCN)
        inputCN.send_keys(Keys.RETURN)

        #Acceso y validacion Formulario Dinamico
        try:
            sleep(5)
            print('PROFUNDISAR EN CN')
            # driver.find_element(By.XPATH, casos_negocio['estado']).click()
            # driver.find_element(By.XPATH, casos_negocio['estado']).click()
            # sleep(4)
            inputCN = driver.find_element(By.XPATH, casos_negocio['inputCN'] + '/input')
            inputCN.send_keys(Keys.TAB)
            sleep(2)
            driver.find_element(By.XPATH, casos_negocio['profCasoNegocio']).click()
            sleep(7)
        except Exception:
            error = 'No Aplica CN NO Existe'
            print(error)
            return False, error
        
        print('MAS INFORMACION')
        driver.find_element(By.XPATH, casos_negocio['masInformacion']).click()
        sleep(4)


        datosBusqueda = ['Cual fue el descuento ofrecido', 'Fecha de Pago', 'Monto de Pago', 'Cual fue el Desc Ofrecido', 'Fecha Primer Pago', 'Monto Primer Pago']
        busquedaCampos = True
        posicion = 2
        descuento = ''
        monto = ''
        fechaPromesaPago = ''
        
        print('Se validad elementos de la tabla')
        while busquedaCampos == True:
            try:                              
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[2]'.format(posicion)).click()
                datoBuscado = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[2]/input'.format(posicion))
                datoBuscado = datoBuscado.get_attribute("value")

                for x in datosBusqueda:

                    if x in datoBuscado:
                        datosBusqueda.remove(x)

                        if x in ['Cual fue el descuento ofrecido', 'Cual fue el Desc Ofrecido']:

                            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[6]'.format(posicion)).click()
                            descuento = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[6]/input'.format(posicion))
                            descuento = descuento.get_attribute("value")
                            print('-> Descuento ofrecido: ', descuento)

                        elif x in ['Fecha de Pago', 'Fecha Primer Pago']:
                                                          
                            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[5]'.format(posicion)).click()
                            fechaPromesaPago = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[5]/input'.format(posicion))
                            fechaPromesaPago = fechaPromesaPago.get_attribute("value")
                            print('-> Fecha promesa pago: ', fechaPromesaPago)

                        elif x in ['Monto de Pago', 'Monto Primer Pago']:

                            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[4]'.format(posicion)).click()
                            monto = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{}]/td[4]/input'.format(posicion))
                            monto = monto.get_attribute("value")
                            print('-> Monto: ', monto)

                posicion += 1

                if descuento != '' and fechaPromesaPago != '' and monto != '':

                    print('-> Fin de busqueda formulario dinamico')
                    busquedaCampos = False

            except Exception as e:
                
                print(e)
                print('-> Fin de busqueda formulario dinamico')

                if descuento != '':
                
                    error = 'No Aplica Formulario Dinamico No existe {}'.format(descuento)
                    return False, error
                
                elif fechaPromesaPago != '':
                
                    error = 'No Aplica Formulario Dinamico No existe {}'.format(fechaPromesaPago)
                    return False, error
                
                elif monto != '':
                
                    error = 'No Aplica Formulario Dinamico No existe {}'.format(monto)
                    return False, error

                busquedaCampos = False

        if 'RECONECTA 50%' in descuento: descuento = 'RX 50%'
        elif 'RECONECTA 100' in descuento: descuento = 'RX 100'
        elif 'RECONECTA 200' in descuento: descuento = 'RX 200'
        else:
            error = 'No Aplica Descuento Invalido'
            return False, error

        datos = {
            'descuento' : descuento,
            'fecha' : fechaPromesaPago,
            'monto' : monto
        }

        return True, datos

        
    except Exception as e:
        print('No Aplica DETECTADO: ', e)
        return False, 'No Aplica Validacion CN'

def validacionCuenta(driver, cuenta, datos):

    try:

        wait = WebDriverWait(driver,120)
        
        #Abrir Casos de Negocio
        status_pantalla_unica = pantalla_unica_consulta(driver, cuenta) 
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '▬')
            return False , 'Error Cuenta no valida', '',''

        print('▬ Inician validaciones de cuenta ▬')

        #Subtipo
        subTipo = driver.find_element(By.XPATH, pantalla_consultad['subTipo'])
        subTipo = subTipo.get_attribute("value")
        print('SubTipo: ', subTipo)

        if subTipo.upper() in ['HOTELES','PYME','CERRADA','EMPLEADOS IZZI']:
            error = 'Error SubTipo'
            return False, error
        
        #Saldo Pendiente
        saldoPendiente = driver.find_element(By.XPATH, pantalla_consultad['saldoVencido'])
        saldoPendiente = saldoPendiente.get_attribute("value")
        print('Saldo Pendiente: ', saldoPendiente)

        if float(saldoPendiente) <= 0:
            error = 'Error Sin Saldo Pendiente'
            return False, error

        #Estado
        estado = driver.find_element(By.XPATH, pantalla_consultad['estado'])
        estado = estado.get_attribute("value")
        print('Estado: ',estado)

        if estado.upper() not in ['INACTIVA', 'NO PAGO']:
            error = 'Error Estado'
            return False, error

        #Busqueda de CN ya tipificado
        #NOTA REVISARLO BIEN CON ERICK POR EL CASO DE QUE SEA EXTEMPORANEO
        driver.find_element(By.XPATH, casos_negocio['busquedaCN']).click()
        sleep(3)
        driver.find_element(By.XPATH, casos_negocio['motivoCliente']).click()
        motivoCliente = driver.find_element(By.XPATH, casos_negocio['motivoCliente'])
        motivoCliente.send_keys('CONVENIO COBRANZA')
        motivoCliente.send_keys(Keys.RETURN)
        motivoCliente.send_keys(Keys.RETURN)

        try:
            driver.find_element(By.XPATH, casos_negocio['existente']).click()
            error = 'Error CN Tipificado Existente'
            return False, error
        except Exception:
            print('Sin Tipificacion Existente')

        #Busqueda Ajuste previo
        driver.find_element(By.XPATH, pantalla_consultad['busquedaSolicitudAjuste']).click()
        sleep(3)
        driver.find_element(By.XPATH, pantalla_consultad['inputMotivo']).click()
        motivo = driver.find_element(By.XPATH, pantalla_consultad['inputMotivo'])
        motivo.send_keys('CONVENIO DE COBRANZA')
        motivo.send_keys(Keys.RETURN)
        motivo.send_keys(Keys.RETURN)
        sleep(3)

        try:
            driver.find_element(By.XPATH, pantalla_consultad['elemBuscado']).click()
            driver.find_element(By.XPATH, pantalla_consultad['elemHistorialAjustes']).click()
        except Exception:
            error = 'Sin Ajuste Previo'
            return False, error

        #Busqueda Pago Realizado
        driver.find_element(By.XPATH, pantalla_consultad['engraneHistorialPagos']).click()
        driver.find_element(By.XPATH, pantalla_consultad['opcOrdenar']).click()
        ordenarPor = driver.find_element(By.XPATH, casos_negocio['ordenarPor'])
        ordenarPor.clear()
        ordenarPor.send_keys('Fecha de Pago')

        driver.find_element(By.XPATH, pantalla_consultad['descendiente']).click()
        driver.find_element(By.XPATH, pantalla_consultad['btnAceptar']).click()
        driver.find_element(By.XPATH, pantalla_consultad['engraneHistorialPagos']).click()
        driver.find_element(By.XPATH, pantalla_consultad['opcColumnasMostradas']).click()

        try:
            driver.find_element(By.XPATH, pantalla_consultad['opcImportePago']).click()
            driver.find_element(By.XPATH, pantalla_consultad['agregarOpc']).click()
            driver.find_element(By.XPATH, pantalla_consultad['btnGuardar']).click()
        except Exception:
            driver.find_element(By.XPATH, casos_negocio['btnGuardar']).click()

        fechaPagoAplicado = driver.find_element(By.XPATH, pantalla_consultad['fechaPagoAplicado'])
        fechaPagoAplicado = fechaPagoAplicado.get_attribute("value")
        fechaPagoAplicado = datetime.datetime.strptime(fechaPagoAplicado, '%d/%m/%Y').date()
        fechaPagoAplicado = fechaPagoAplicado.strftime('%Y-%m-%d')

        fechaSolicitada = datetime.datetime.strptime(datos['fecha'], '%d/%m/%Y %H:%M:%S').date()
        fechaSolicitada = fechaSolicitada.date()

        rangoMenorDias = fechaSolicitada - datetime.timedelta(days=2)
        rangoMayorDias = fechaSolicitada + datetime.timedelta(days=2)

        if fechaPagoAplicado <= rangoMenorDias and fechaPagoAplicado < fechaSolicitada:
            print('Pago realizado dentro de la regla de los 5 dias')
        elif fechaPagoAplicado > fechaSolicitada and fechaPagoAplicado <= rangoMayorDias:
            print('Pago realizado dentro de la regla de los 5 dias')
        elif fechaPagoAplicado == fechaSolicitada:
            print('Pago realizado dentro de la regla de los 5 dias')
        else:
            error = 'Pago Fuera de Fecha'
            return False, error

        monto = driver.find_element(By.XPATH, pantalla_consultad['montoPagado'])
        monto = monto.get_attribute("value")

        if 'RX150' in datos['descuento']:
            if '150' in monto: print('Pago Correcto')
            else:
                error = 'Error Pago Incorrecto'
                return False, error
        elif 'RX100' in datos['descuento']:
            if '100' in monto: print('Pago Correcto')
            else:
                error = 'Error Pago Incorrecto'
                return False, error 
        elif 'RX250' in datos['descuento']:
            if '250' in monto: print('Pago Correcto')
            else:
                error = 'Error Pago Incorrecto'
                return False, error
        elif 'RX 50%' in datos['descuento']:
            if datos['monto'] in monto: print('Pago Correcto')
            else:
                error = 'Error Pago Incorrecto'
                return False, error 

        return True, ''

    except Exception as e:
        print(e)
        return False, ''

def aplicacionAjuste(driver, monto, promocion):
    try:
        print('se va a aplicar el ajuste')
        driver.find_element(By.XPATH, pantalla_consultad['crearAjuste']).click()
        sleep(10)
    except Exception as e:
        error = 'Error al crear ajuste'
        return False, error , '' , ''
    
    try:
        sleep(3)
        print('Importe a aplicar: ',monto)
        driver.find_element(By.XPATH, pantalla_consultad['importe']).click()
        sleep(3)
        montoAjuste = driver.find_element(By.XPATH, pantalla_consultad['importe'] + '/span/input')
        montoAjuste.clear()
        montoAjuste.send_keys(str(monto))
    
    except Exception as e:
        print(e)
        error = 'Problema al asignar Monto Ajuste'
        print(error)
        return False, error , '' , ''
    
    try:
        print('Aplicacio a favor')
        driver.find_element(By.XPATH, pantalla_consultad['aplicar']).click()
        aFavor = driver.find_element(By.XPATH, pantalla_consultad['aplicar'] +'/span/input')
        aFavor.send_keys('A favor')
        aFavor.send_keys(Keys.RETURN)
    
    except:
        error = 'Error al Aplicar Ajuste'
        return False, error , '' , ''
    
    try:
        print('Aplicando motivo del ajuste')
        driver.find_element(By.XPATH, pantalla_consultad['motivoAjuste']).click()
        motivoAjuste = driver.find_element(By.XPATH, pantalla_consultad['motivoAjuste'] + '/span/input')
        
        if 'LATE FEE' in promocion.upper(): motivoAjuste.send_keys('CARGO POR PAGO EXTEMPORANEO')
        # elif 'RX100' in promocion: motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        # elif 'RX150' in promocion: motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        # elif 'RX250' in promocion: motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        # elif 'RX1000' in promocion: motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        # elif 'RX50%' in promocion: motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        # elif 'RX30%' in promocion: motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        else:motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        
        motivoAjuste.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
        error = 'Problema en Aplicacion de Motivo'
        print(error)
        return False, error , '' , ''
    
    try:
        print('aplicando comentario')
        monto = str(monto)
        monto = monto.split(".")
        print(monto[0])
        
        if '150' in promocion: comentario = 'Convenio Cobranza RX 150'
        elif '100' in promocion: comentario = 'Convenio Cobranza RX 100'
        elif '250' in promocion: comentario = 'Convenio Cobranza RX 250'
        elif 'Baby' in promocion or 'baby' in promocion : comentario = 'Convenio Cobranza Baby RX50'
        elif '200' in promocion: comentario = 'Convenio Cobranza RX 200'
        elif '1000' in promocion or '1,000' in promocion: comentario = 'Convenio Cobranza RX 1000'
        elif '20%' in promocion or '20%' in promocion or '2 0%' in promocion or '20 %' in promocion:
            if 'M6' in promocion.upper(): comentario = 'Convenio Cobranza Descuento 20 por ciento mes 6'
            elif 'M5' in promocion.upper(): comentario = 'Convenio Cobranza Descuento 20 por ciento mes 5'
            elif 'M4' in promocion.upper(): comentario = 'Convenio Cobranza Descuento 20 por ciento mes 4'
            elif 'M3' in promocion.upper(): comentario = 'Convenio Cobranza Descuento 20 por ciento mes 3'
            elif 'M2' in promocion.upper(): comentario = 'Convenio Cobranza Descuento 20 por ciento mes 2'
            else: comentario = 'Convenio Cobranza Descuento 20 por ciento mes 1'
        elif 'LATE FEE + CAMBIO PAQUETE' in promocion.upper(): comentario = 'Convenio Cobranza LATE FEE'
        elif 'LATE FEE' in promocion.upper(): comentario = 'POR CONVENIO DE COBRANZA'
        else: comentario = 'Convenio Cobranza RX 50'
        print(comentario)
        sleep(3)
        driver.find_element(By.XPATH, pantalla_consultad['comentarios']).click()
        comentarios = driver.find_element(By.XPATH, pantalla_consultad['comentarios'] + '/span/textarea')
        comentarios.send_keys(comentario)
    except Exception as e:
        print(e)
        error = 'Problema en Aplicacion de Comentario'
        return False, error , '' , ''

    try:
        print('Obteniendo fecha dle ajuste ')

        fechaAjuste = driver.find_element(By.XPATH, pantalla_consultad['fechaAjuste'])
        fechaAjuste = fechaAjuste.get_attribute("value")
        print('Fecha del ajuste: ', fechaAjuste)

    except:
        error = 'Problema en Obtencion Fecha Ajuste'
        return False, error , '' , ''

    try:
        print('Obteniendo numero dle ajuste ')

        numAjuste = driver.find_element(By.XPATH, pantalla_consultad['numAjuste'])
        numAjuste = numAjuste.get_attribute("value")
        print('Numero de ajuste: ', numAjuste)
    except:
        error = 'Error Obtencion Numero Ajuste'
        return False, error , '' , ''

    try:
        driver.find_element(By.XPATH, pantalla_consultad['guardarAjuste']).click()
        sleep(6)
        
         #Busqueda Ajuste previo
        print('Buscando ajuste generado')
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[1]/div[2]/button[2]').click()
        except Exception:
            try:
                sleep(3)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[1]/div[2]/button[2]').click()
            except Exception:
                print('sigue fallando busqueda CN ************************')
                
        sleep(5)
        ingresoNumAjuste = driver.find_element(By.XPATH, solicitud_ajuste['inputBusquedaAjuste'])
        ingresoNumAjuste.send_keys(numAjuste)
        ingresoNumAjuste.send_keys(Keys.RETURN)
    except Exception as e:
        error = 'Problema al Guardar Ajuste'
        return False, error , '' , ''

    sleep(15)
    

    try:
        print('enviando ajuste')

        driver.find_element(By.XPATH, "//button[@aria-label='Solicitudes de Ajuste Applet de lista:Enviar']").click()
        sleep(10)
        print('BTN aceptar envio')

        driver.find_element(By.XPATH, "//button[@aria-label='Enviar Ajuste Applet de formulario:Aceptar']").click()
        sleep(10)
    except:
        error = 'Problema al enviar Ajuste'
        return False, error , '' , ''


    cambiandoStatusAjuste = True
    contador = 0

    while cambiandoStatusAjuste == True:

        try:
            estatusAjuste = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]')
            estatusAjuste = estatusAjuste.text
        except:
            estatusAjuste = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]')
            estatusAjuste = estatusAjuste.text

        if 'Aplicado' in estatusAjuste:
            cambiandoStatusAjuste = False
            print('Ajuste Aplicado')
        else:
            sleep(5)
            contador += 1
            if contador == 4:
                cambiandoStatusAjuste = False

    print('Consultado saldo para actualizar el ajuste ')

    contadorActivo = 0
    consulta = False
    while consulta == False:
        try:
            label = 'Pantalla Única de Consulta Applet de formulario:Consulta de Saldos'
            driver.find_element(By.XPATH, "//button[@aria-label='" + label + "']").click()
            consulta = True
        except:
            sleep(5)
            contadorActivo += 1
            if contadorActivo == 6:
                error = 'Error al actualizar saldo'
                consulta = True
                print(error)
                return False, error, '',''
        
        return True, '', numAjuste, estatusAjuste