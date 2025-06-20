#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
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

def agregarDatos(driver, accion, dato, envio, tElemento, bElemento, labelBusqueda):

    try:

        driver.find_element(By.XPATH, f"//{tElemento}[@{bElemento}='" + labelBusqueda + "']").click()

        if accion == 'ingresar':
            elemento = driver.find_element(By.XPATH, f"//{tElemento}[@{bElemento}='" + labelBusqueda + "']")
            elemento.clear()
            elemento.send_keys(dato)
            elemento.send_keys(Keys.RETURN)

            if envio == True:
                elemento.send_keys(Keys.RETURN)
                return True
            else:
                return True
            
    except:
        return False

def generacionCN(driver, beneficio):

    try:
        sleep(30)

        text_box('INICIA CREACION CASO DE NEGOCIO', '▬')

        #Creacion CN
        insersion = agregarDatos(driver, 'click', False, False, 'button', 'aria-label', 'Casos de Negocio Applet de lista:Nuevo')
        if insersion == False:
            error = 'Error Crear CN'
            print(error)
            return False, error, ''
        sleep(3)
        
        #Categoria
        insersion = agregarDatos(driver, 'ingresar', 'SERVICIOS', False, 'input', 'aria-label', 'Categoria')
        if insersion == False:
            error = 'Error Categoria CN'
            print(error)
            return False, error, ''
        
        #Motivo
        insersion = agregarDatos(driver, 'ingresar', 'MOD AL CONTRATO', False, 'input', 'aria-label', 'Motivo')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''

        #Submotivo
        insersion = agregarDatos(driver, 'ingresar', 'RENOVACION PLAZO FORZOSO', False, 'input', 'aria-label', 'Submotivo')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''

        #Solucion
        insersion = agregarDatos(driver, 'ingresar', 'CON BENEFICIOS', False, 'input', 'aria-label', 'Solución')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''

        #Obtencion No CN
        cnGenerado = driver.find_element(By.XPATH, casos_negocio['numroCN'])
        cnGenerado = cnGenerado.text
        print('CN generado: ', cnGenerado)

        #Comentario
        insersion = agregarDatos(driver, 'ingresar', f'CN: {cnGenerado} Ajuste por Retencion BOT', False, 'textarea', 'aria-label', 'Comentarios')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''
        
        #Beneficios
        if 'PROMOCION 110 X 12M 3P' in beneficio:
            insersion = agregarDatos(driver, 'ingresar', 'Promocion 110 x 12 meses 3P', False, 'input', 'aria-label', 'Nombre Beneficio')
            if insersion == False:
                error = 'Error Motivo CN'
                print(error)
                return False, error, ''
        elif 'PROMOCION 50 X 12M 2P' in beneficio:
            insersion = agregarDatos(driver, 'ingresar', 'Promocion 50 x 12 meses 2P', False, 'input', 'aria-label', 'Nombre Beneficio')
            if insersion == False:
                error = 'Error Motivo CN'
                print(error)
                return False, error, ''
        elif 'EXT 50 Y 110 X 12M 3P' in beneficio:
            insersion = agregarDatos(driver, 'ingresar', 'Extension 50 y 110 x 12 meses 3P', False, 'input', 'aria-label', 'Nombre Beneficio')
            if insersion == False:
                error = 'Error Motivo CN'
                print(error)
                return False, error, ''
        elif 'EXT SIN COSTO Y 110 X 12M 3P' in beneficio:
            insersion = agregarDatos(driver, 'ingresar', 'Extension sin costo y 110 x 12 meses 3P', False, 'input', 'aria-label', 'Nombre Beneficio')
            if insersion == False:
                error = 'Error Motivo CN'
                print(error)
                return False, error, ''
        else:
            error = 'Error Sin Beneficio'
            print(error)
            return False, error, ''


        #Estado
        # ingresarDatos(driver, 'Cerrado', casos_negocio['cnEstado'])
        sleep(5)
        insersion = agregarDatos(driver, 'click', False, False, 'input', 'aria-label', 'Estado')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''
        sleep(2)
        insersion = agregarDatos(driver, 'click', False, False, 'span', 'id', 's_30_1_12_0_icon')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''

        # driver.find_element(By.XPATH, casos_negocio['cnCerrado']).click()

        sleep(6)

        # insersion = agregarDatos(driver, 'click', False, False, 'button', 'aria-label', 'Casos de negocio Applet de formulario:Guardar')
        insersion = agregarDatos(driver, 'click', False, False, 'button', 'aria-label', 'Casos de negocio Applet de formulario:Cancelar')
        if insersion == False:
            error = 'Error Motivo CN'
            print(error)
            return False, error, ''

        return True, '', cnGenerado


    except Exception as e:
        print(e)
        return False,'',''

def cierrecN(driver, cn, movimiento):
    try:
        sleep(5)
        insersion = agregarDatos(driver, 'click', False, False, 'button', 'aria-label', 'Casos de Negocio Applet de lista:Consulta')
        if insersion == False:
            error = 'Error Crear CN'
            print(error)
            return False, error, ''
        sleep(5)
        
        insersion = agregarDatos(driver, 'ingresar', cn, False, 'input', 'un', 'Caso de Negocio')
        if insersion == False:
            error = 'Error Categoria CN'
            print(error)
            return False, error, ''

        insersion = agregarDatos(driver, 'click', False, False, 'td', 'id', '1_s_1_l_Status')
        if insersion == False:
            error = 'Error Crear CN'
            print(error)
            return False, error, ''

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a")
        sleep(10)

        insersion = agregarDatos(driver, 'click', cn, False, 'li', 'un', 'Actividades')
        if insersion == False:
            error = 'Error Categoria CN'
            print(error)
            return False, error, ''
        
        sleep(5)
        it.send('{CTRLDOWN}+s+{CTRLUP}')
    except Exception as e:
        print(e)
        return False, 'Error Cierre CN'
    
  

def validacionCN(driver, noCN):

    try:

        wait = WebDriverWait(driver,120)
        
        #Abrir Casos de Negocio
        sleep(5)
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
        driver.find_element(By.XPATH, "//button[@aria-label='" + texto_boton + "']").click()
            


        # driver.find_element(By.XPATH, casos_negocio['inputCN']).click()
        sleep(2)
        try:
            texto_boton ='s_2_l_SR_Number s_2_l_altLink'
            inputCN = driver.find_element(By.XPATH, "//input[@aria-labelledby='" + texto_boton + "']")
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
            error = 'Error CN NO Existe'
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
                
                    error = 'Error Formulario Dinamico No existe {}'.format(descuento)
                    return False, error
                
                elif fechaPromesaPago != '':
                
                    error = 'Error Formulario Dinamico No existe {}'.format(fechaPromesaPago)
                    return False, error
                
                elif monto != '':
                
                    error = 'Error Formulario Dinamico No existe {}'.format(monto)
                    return False, error

                busquedaCampos = False

        if 'RECONECTA 50%' in descuento: descuento = 'RX 50%'
        elif 'RECONECTA 100' in descuento: descuento = 'RX 100'
        elif 'RECONECTA 200' in descuento: descuento = 'RX 200'
        else:
            error = 'Error Descuento Invalido'
            return False, error

        datos = {
            'descuento' : descuento,
            'fecha' : fechaPromesaPago,
            'monto' : monto
        }

        return True, datos

        
    except Exception as e:
        print('ERROR DETECTADO: ', e)
        return False, 'Error Validacion CN'

def validacionCuenta(driver, cuenta, datos):

    try:

        wait = WebDriverWait(driver,120)
        
        #Abrir Casos de Negocio
        status_pantalla_unica = pantalla_unica_consulta(driver, cuenta) 
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '▬')
            return False , 'Cuenta no valida', '',''

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

def aplicacionAjuste(driver, monto, cn):
    try:
        print('se va a aplicar el ajuste')
        driver.find_element(By.XPATH, pantalla_consultad['crearAjuste']).click()
        sleep(5)

        print('Importe a aplicar: ',monto)
        montoAjuste = driver.find_element(By.XPATH, pantalla_consultad['importe'] + '/span/input')
        montoAjuste.clear()
        montoAjuste.send_keys(str(monto))

        print('Aplicacio a favor')
        driver.find_element(By.XPATH, pantalla_consultad['aplicar']).click()
        aFavor = driver.find_element(By.XPATH, pantalla_consultad['aplicar'] +'/span/input')
        aFavor.send_keys('A favor')
        aFavor.send_keys(Keys.RETURN)

        print('Aplicando motivo del ajuste')
        driver.find_element(By.XPATH, pantalla_consultad['motivoAjuste']).click()
        motivoAjuste = driver.find_element(By.XPATH, pantalla_consultad['motivoAjuste'] + '/span/input')
        motivoAjuste.send_keys('CONVENIO DE COBRANZA')
        motivoAjuste.send_keys(Keys.RETURN)

        print('aplicando comentario')
        monto = str(monto)
        monto = monto.split(".")
        print(monto[0])
        

        comentario = 'Solucion\nSeguiminto a convencio de cobranza \nCaso de Negocio {}\nMonto {}'.format(cn,monto[0])
        print(comentario)
        driver.find_element(By.XPATH, pantalla_consultad['comentarios']).click()
        comentarios = driver.find_element(By.XPATH, pantalla_consultad['comentarios'] + '/span/textarea')
        comentarios.send_keys(comentario)

        print('Obteniendo fecha dle ajuste ')

        fechaAjuste = driver.find_element(By.XPATH, pantalla_consultad['fechaAjuste'])
        fechaAjuste = fechaAjuste.get_attribute("value")
        print('Fecha del ajuste: ', fechaAjuste)

        print('Obteniendo numero dle ajuste ')

        numAjuste = driver.find_element(By.XPATH, pantalla_consultad['numAjuste'])
        numAjuste = numAjuste.get_attribute("value")
        print('Numero de ajuste: ', numAjuste)

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

        sleep(8)
    


        print('enviando ajuste')

        driver.find_element(By.XPATH, pantalla_consultad['enviar']).click()
        sleep(10)
        print('BTN aceptar envio')
        # try:
        #     driver.find_element(By.XPATH, solicitud_ajuste['aceptarEnvio']).click()
        # except Exception:
        #     driver.find_element(By.XPATH, solicitud_ajuste['aceptarEnvio']).click()

        it.send('{TAB 5}')
        sleep(2)
        it.send('{ENTER}')
        sleep(10)
        print('Consultado saldo para actualizar el ajuste ')

        contadorActivo = 0
        consulta = False
        while consulta == False:
            try:
                driver.find_element(By.XPATH, casos_negocio['consultaSaldo']).click()
                consulta = True
            except:
                sleep(5)
                contadorActivo += 1
                if contadorActivo == 6:
                    error = 'Error al actualizar saldo'
                    consulta = True
                    print(error)
        
        return True, '', numAjuste


    except Exception as e:
        print(e)
        error = 'Error Aplicacion Ajuste'
        return False, error