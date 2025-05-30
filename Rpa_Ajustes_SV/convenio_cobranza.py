#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import autoit as it
import re
#-------------System-------------------#
from time import sleep
import os
import win32clipboard as cp
from datetime import *
from datetime import timedelta
#---------Mis funciones---------------#
from utileria import *
from logueo import *
import Services.ApiCyberHubOrdenes as api
from rutasPreProduccion import *


def ordenar(driver, engrane, opcionOrden, input, elementoOrden, orden, confirmar):

    ########################################################################

                ### FUNCION PARA ORDENAR TABLAS ###

    ########################################################################

    print('Ordenamiento de tabla')

    driver.find_element(By.XPATH, engrane).click() #Click sobre engrane
    sleep(1)
    driver.find_element(By.XPATH, opcionOrden).click() #Click sobre opcion "Ordenar"
    sleep(1)
    driver.find_element(By.XPATH, input).click() #Click sobre input "Ordenar Por"
    
    inputOrdenarPor = driver.find_element(By.XPATH, input) #Obtencion input "Ordenar Por"
    inputOrdenarPor.clear()
    inputOrdenarPor.send_keys(elementoOrden)
    inputOrdenarPor.send_keys(Keys.ESCAPE)

    sleep(1)

    driver.find_element(By.XPATH, orden).click() #Click sobre opcion "Descendiente"
    driver.find_element(By.XPATH, confirmar).click() #Click sobre boton "Aceptar"

def buscar(driver, lupa, campo, busqueda):
    print('Funcion buscar')
    driver.find_element(By.XPATH, lupa).click() #Click sobre lupa de buscar
    sleep(4)

    driver.find_element(By.XPATH, campo).click()

    element = driver.find_element(By.XPATH, campo)
    
    element.clear()                    #Limpia lo que haya en el campo
    element.send_keys(busqueda)         #Introduce el motivo del ajuste
    element.send_keys(Keys.RETURN)     #Enter
    element.send_keys(Keys.RETURN)     #Enter 

def formatoFecha(fecha, time):

    if time == True:
        fechaF = datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S')
        fechaF = fechaF.strftime('%Y-%m-%d %H:%M:%S')
        fechaF = datetime.strptime(fechaF, '%Y-%m-%d %H:%M:%S')
        
    else:
        fechaF = datetime.strptime(fecha, '%d/%m/%Y').date()
        fechaF = fechaF.strftime('%Y-%m-%d')
        fechaF = datetime.strptime(fechaF, '%Y-%m-%d').date()

    print('Fecha formateada')
    return fechaF

def montoPago(driver, engrane, mostrarColumnas, elementoAgregar, agregar, guardar):

    driver.find_element(By.XPATH, engrane).click() #Click sobre engrane
    sleep(1)
    driver.find_element(By.XPATH, mostrarColumnas).click() #Click sobre opcion "Ordenar"
    sleep(4)
    try:
        driver.find_element(By.XPATH, elementoAgregar).click() #Click sobre engrane
        sleep(1)
        driver.find_element(By.XPATH, agregar).click() #Click sobre engrane
        sleep(1)
    except:
        print('...')
        # driver.find_element(By.XPATH, '/html/body/div[20]/div[2]/div/div/div/form/table[2]/tbody/tr/td/span[3]/button').click() #Click sobre engrane
        # sleep(5)
    driver.find_element(By.XPATH, guardar).click() #Click sobre engrane
    sleep(4)

def busquedaCNTipificado(driver, busqueda, meses):
    driver.find_element(By.XPATH, casos_negocio['lupa']).click()
    sleep(3)
    driver.find_element(By.XPATH, casos_negocio['solucion']).click()
    solucion  = driver.find_element(By.XPATH, casos_negocio['solucion'] + '/input')
    solucion.send_keys('APLICA AJUSTE')
    sleep(1)
    driver.find_element(By.XPATH, casos_negocio['subMotivo']).click()
    submotivo  = driver.find_element(By.XPATH, casos_negocio['subMotivo'] + '/input')
    submotivo.send_keys('AJUSTE FACTURACION')
    sleep(1)
    driver.find_element(By.XPATH, casos_negocio['motivo']).click()
    motivo  = driver.find_element(By.XPATH, casos_negocio['motivo'] + '/input')
    motivo.send_keys('ACLARACION DE ESTADO DE CUENTA')
    sleep(1)
    driver.find_element(By.XPATH, casos_negocio['motivoCliente']).click()
    motivoCliente  = driver.find_element(By.XPATH, casos_negocio['motivoCliente'] + '/input')
    motivoCliente.send_keys(busqueda)
    motivoCliente.send_keys(Keys.RETURN)
    motivoCliente.send_keys(Keys.RETURN)
    sleep(8)
    try:
        driver.find_element(By.XPATH, casos_negocio['engrane']).click()
        sleep(2)
        driver.find_element(By.XPATH, casos_negocio['opcOrdenar']).click()
        sleep(7)
        # driver.find_element(By.XPATH, casos_negocio['ordenarPor']).click()
        sleep(3)
        ordenarPor = driver.find_element(By.XPATH, casos_negocio['ordenarPor'] + '/input')
        ordenarPor.send_keys('Fecha de Apertura')
        ordenarPor.send_keys(Keys.RETURN)
        sleep(4)
        driver.find_element(By.XPATH, casos_negocio['descendiente']).click()
        driver.find_element(By.XPATH, casos_negocio['descendiente']).click()
        sleep(4)
        driver.find_element(By.XPATH, casos_negocio['btnAceptar']).click()
        sleep(5)
    except Exception:
        print('Sin CN tipificado con anterioridad')

    try:
        driver.find_element(By.XPATH, casos_negocio['resultadoFecha']).click()
        sleep(2)
        fechaCNObtenido = driver.find_element(By.XPATH, casos_negocio['resultadoFecha'] + '/input')
        fechaCNObtenido = fechaCNObtenido.get_attribute("value")
        print('fecha cn tipificado: ', fechaCNObtenido)
        fechaCNObtenido = formatoFecha(fechaCNObtenido, False)
        fechaActual = date.today()

        diferencia_fechas = fechaActual - fechaCNObtenido
        print('Diferencia entre hoy y la feha de cierre: ', diferencia_fechas)

        tres_meses = timedelta(days=int(meses)*30)

        if diferencia_fechas > tres_meses:
            print('El ultimo ajuste es mayor a 4 meses')
        else:
            print('Ultimo ajuste menor a 4 meses')
            error = 'Error Ajuste reciente'
            print('Error ', error)
            return True, error
            
    except Exception as e:
        print(e)
        return False, ''

def validacion_cuenta_convenio_cobranza(driver, no_cuenta, no_caso, datos, meses):
    '''
    Funcion que hace el ajuste por Cargo Extemporaneo
    args:
        - driver
        - no_cuenta
        - no_caso

    out:
        - Bool: True en caso de que la cuenta cumpla con las validaciones para el ajuste
        - causa_rechazo (str): causa de validacion fallida

    '''
    try:
        wait = WebDriverWait(driver, 120)
        act = webdriver.ActionChains(driver)
        text_box('AJSUTE POR CONVENIO COBRANZA', '▬')
        status_pantalla_unica = pantalla_unica_consulta(driver, no_cuenta) 
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '▬')
            return False ,'Error Cuenta no valida',''
        
        print('▬ Inician validaciones de cuenta ▬')
        
        print('▬ Tipo Cuenta')
        tipo_cuenta = my_copy_by_xpath(driver, pantalla_unica['tipo_cuenta']['xpath'])
        if tipo_cuenta.upper() not in ['RESIDENCIAL', 'NEGOCIO']:
            error = 'tipo cuenta ' + tipo_cuenta
            print('Error ', error)
            return False, error,''
        

        print('▬ Subtipo Cuenta') 
        subtipo_cuenta = my_copy_by_xpath(driver, pantalla_unica['subtipo_cuenta']['xpath'])
        if subtipo_cuenta.upper() not in ['NORMAL']:
            error = 'subtipo cuenta ' + subtipo_cuenta
            print('Error ', error)
            return False, error,''

        print('▬ Saldo pendiente') 
        if open_item_selenium_wait(driver, xpath =  pantalla_unica['saldo_pendiente']['xpath']) != True: return False, True, ''

        saldo_pendiente = my_copy_by_xpath(driver, pantalla_unica['saldo_pendiente']['xpath'])
        if ',' in saldo_pendiente:
            saldo_pendiente = saldo_pendiente.replace(',', '')
        if saldo_pendiente != None:
            try:
                saldo_pendiente = float(saldo_pendiente)
            except Exception as e:
                print(f'No se pudo convertir rl saldo a numero: {e}')
                error = 'saldo invalido'
                print('Error ', error)
                return False,error,''
        if saldo_pendiente <= 0:
            error = 'Sin Saldo Vencido'
            print('Error ', error)
            return False,error,''
        else:
            print(f'El saldo pendiente es de {saldo_pendiente} MXN')

        monto = float(datos['monto'])
        print('monto Pagado: ', datos['monto'])

        if 'RX 100' in datos['descuento']:
            print('Se verifica por un RX100')
            if saldo_pendiente + monto > 300 and saldo_pendiente + monto < 1000:
                if 150 == monto: print('Pago Realizado Correcto de RX 100'); ajuste = saldo_pendiente
                else:
                    error = 'Error Pago Incorrecto'
                    print(error)
                    return False, error,''
            else:
                error = 'Error Saldo Fuera de Rango'
                print(error)
                return False, error,''
        elif 'RX 200' in datos['descuento']:
            print('Se verifica por un RX200')
            if saldo_pendiente  + monto > 251 and saldo_pendiente  + monto < 1000:
                if 250 == monto: print('Pago Realizado Correcto de RX 200'); ajuste = saldo_pendiente
                else:
                    error = 'Error Pago Incorrecto'
                    print(error)
                    return False, error,''
            else:
                error = 'Error Saldo Fuera de Rango'
                print(error)
                return False, error,''
        elif 'RX 50%':
            print('Se verifica por un RX50%')
            # ajuste = (saldo_pendiente * (-1)) - monto
            if saldo_pendiente + monto > 100 and saldo_pendiente + monto < 475 or saldo_pendiente + monto > 1001 and saldo_pendiente + monto < 5000:
                ajuste = saldo_pendiente - monto
            else:
                error = 'Error Saldo Fuera de Rango'
                print(error)
                return False, error,''
        else:
            error = 'Error Descuendo Invalido'
            print(error)
            return False, error, ''
            
        print('-> Monto del ajuste a aplicar: ', ajuste)

        print('▬ Estado de la cuenta')  
        estado_cuenta = my_copy_by_xpath(driver, pantalla_unica['estado_cuenta']['xpath'])
        if estado_cuenta.upper() not  in ['INACTIVA', 'INACTIVO', 'ACTIVO', 'ACTIVA']:
            error = 'Estado Cuenta ' + estado_cuenta
            print('Error ', error)
            return False, error,''

        print('validando fecha de los 5 dias')

        fechaPagoAplicado = datos['fecha']
        fechaPagoAplicado = datetime.strptime(fechaPagoAplicado, '%d/%m/%Y %H:%M:%S').date()
        fechaPagoAplicado = fechaPagoAplicado.strftime('%Y-%m-%d')
        fechaPagoAplicado = datetime.strptime(fechaPagoAplicado, '%Y-%m-%d').date()

        fechaSolicitada = date.today()

        rangoMenorDias = fechaSolicitada - timedelta(days=2)
        rangoMayorDias = fechaSolicitada + timedelta(days=2)

        if fechaPagoAplicado <= rangoMenorDias and fechaPagoAplicado < fechaSolicitada:
            print('Pago realizado dentro de la regla de los 5 dias')
        elif fechaPagoAplicado > fechaSolicitada and fechaPagoAplicado <= rangoMayorDias:
            print('Pago realizado dentro de la regla de los 5 dias')
        elif fechaPagoAplicado == fechaSolicitada:
            print('Pago realizado dentro de la regla de los 5 dias')
        else:
            error = 'Error Pago Fuera de Fecha'
            print(error)
            return False, error,''


        #Busqueda CN Tipificado

        resultadoBusqueda, error = busquedaCNTipificado(driver, 'CONVENIO COBRANZA', meses)
        if resultadoBusqueda == True:
            error = 'Error CN Convenio Cobranza Previo Tipificado'
            print(error)
            return False, error,''
        else:
            print('No hay CN tipificado por convenio cobranza')
            resultadoBusqueda, error = busquedaCNTipificado(driver, 'CARGO EXTEMPORANEO', meses)
            if resultadoBusqueda == True:
                error = 'Error CN Cargo Extemporaneo Previo Tipificado'
                print(error)
                return False, error,''
            else:
                print('Sin CN previo tipificado')

        print('• Monto de ajuste: ', ajuste)

        print('▬ Solicitudes de ajuste')

        # sleep(2)

        # #Busqueda Ajuste previo
        print('Buscando algun ajuste previo')
        driver.find_element(By.XPATH, pantalla_consultad['busquedaSolicitudAjuste']).click()
        sleep(3)
        driver.find_element(By.XPATH, pantalla_consultad['inputMotivo']).click()
        sleep(2)
        motivo = driver.find_element(By.XPATH, pantalla_consultad['inputMotivo'] + '/input')
        motivo.send_keys('CONVENIO DE COBRANZA')
        sleep(2)
        driver.find_element(By.XPATH, pantalla_consultad['inputEstadoAjuste']).click()
        sleep(2)
        motivo = driver.find_element(By.XPATH, pantalla_consultad['inputEstadoAjuste'] + '/input')
        motivo.send_keys('Aplicado')
        motivo.send_keys(Keys.RETURN)
        motivo.send_keys(Keys.RETURN)
        sleep(3)

        try:
            driver.find_element(By.XPATH, solicitud_ajuste['fechaAjusteValidacion']).click()
            sleep(2)
            fechaAjusteObtenido = driver.find_element(By.XPATH, solicitud_ajuste['fechaAjusteValidacion'] + '/input')
            fechaAjusteObtenido = fechaAjusteObtenido.get_attribute("value")
            print('fecha Ajuste obtenido: ', fechaAjusteObtenido)
            fechaAjusteObtenido = formatoFecha(fechaAjusteObtenido, True)
            fechaActual = datetime.today()

            diferencia_fechas = fechaActual - fechaAjusteObtenido
            print('Diferencia entre hoy y la feha de cierre: ', diferencia_fechas)

            tres_meses = timedelta(days=int(meses)*30)

            if diferencia_fechas > tres_meses:
                print('El ultimo ajuste es mayor a 4 meses')
            else:
                print('Ultimo ajuste menor a 4 meses')
                error = 'Error Ajuste reciente'
                print('Error ', error)
                return True, error
        except Exception:
            print('SIN AJUSTE PREVIO')
        
        sleep(5)
 
        print('Validaciones correctas')
        return True, '', ajuste

    except Exception as e:
        print(f'ERROR ajustando el cargo extemporaneo. Caso NO. {no_caso}. CUENTA: {no_cuenta}')
        description_error('11','validacion_cuenta_cargo_extemporaneo',e)
        print('Error ', e)
        return False, 'Excepcion',''

def extraccion_numero_pago(comentarios):
    '''
    Funcion que extrae el numero de pago de los comentarios ingresados en el ajuste

    arg:
        - comentarios: str

    out:
        - numero_pago: str
    '''
    try:
        print('Extraccion del numero de pago.')
        comentarios = comentarios.upper()
        comentarios_separados = comentarios.split('1-')
        ultimo_match = comentarios_separados[-1]
        patron = r"^[0-9]+$"
        numero_pago = '1-'
        # Verificar si la cadena coincide con la expresión regular

        for i in ultimo_match:
            if re.match(patron, i):
                numero_pago = numero_pago + i
            else:
                break
        print(f'Numero de pago {numero_pago}')
        return numero_pago
    except Exception as e:
        print('No se pudo encontrar el numero de pago.')
        description_error('CC-01','extraccion_numero_pago.',e)
        return False

def validar_ajuste_previo_cobranza(driver):
    wait = WebDriverWait(driver, 120)
    act = webdriver.ActionChains(driver)

    text_box('VALIDANDO AJUSTE CONVENIO DE COBRANZA', '▬')

def aplicacion_ajuste_convenio_cobranza(driver, caso_negocio, monto):
    '''
    Funcion que aplica el ajuste
    arg: 
        - driver
    out:
        - bool: True en caso de que se cree el ajuste, se guarde y se envie
    '''
    try:
        text_box('AJUSTE POR CARGO EXTEMPORANEO', '▬')
        print('Cargando...')
        open_item_selenium_wait(driver ,name = pantalla_unica['saldo_pendiente']['name'], xpath =  pantalla_unica['saldo_pendiente']['xpath'])
        it.send('{DOWN 25}')
        element = driver.find_element(By.XPATH,'//*[@id="a_5"]/div[1]')
        print('Nueva Solicitud de Ajuste')
        print('Copia el ID del ajuste')
        open_item_selenium_wait(driver, xpath =  solicitud_ajuste['nueva_solicitud']['xpath'])
        sleep(5)
        element = driver.find_element(By.XPATH,  solicitud_ajuste['importe']['xpath'])
        element.clear()                    #Limpia lo que haya en el campo
        element.send_keys(monto)           #Introduce el numero de orden
        
        driver.find_element(By.XPATH,  solicitud_ajuste['aFavor']).click()
        favor = driver.find_element(By.XPATH,  solicitud_ajuste['aFavor'])
        favor.clear()                    #Limpia lo que haya en el campo
        favor.send_keys('A favor')           #Introduce el numero de orden

        driver.find_element(By.XPATH,  solicitud_ajuste['mAjuste']).click()
        favor = driver.find_element(By.XPATH,  solicitud_ajuste['mAjuste'])
        favor.clear()                    #Limpia lo que haya en el campo
        favor.send_keys('CONVENIO DE COBRANZA')           #Introduce el numero de orden

        sleep(3)
        driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/span/input').click()
        it.send('{TAB}')
        it.send('{LSHIFT}+{TAB}')
        fechaAjusteGenerado = my_copy(driver)
        sleep(3)
        driver.find_element(By.XPATH,  solicitud_ajuste['mAjuste']).click()
        favor = driver.find_element(By.XPATH,  solicitud_ajuste['mAjuste'])
        favor.clear()                    #Limpia lo que haya en el campo
        comentario = f'''SE APLICA AJUSTE POR CONVENIO DE COBRANZA CN {caso_negocio} ROBOT'''
        favor.send_keys(comentario)           #Introduce el numero de orden
        sleep(3)
        print('Guardar')
        driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[1]/tbody/tr/td[1]/span/div/div[3]/button[1]').click()
        sleep(5)

        print('Enviar')

        open_item_selenium_wait(driver, xpath = '//*[@id="s_5_1_0_0_Ctrl"]')
        sleep(7)
        it.send('{TAB 5}')
        sleep(2)
        it.send('{ENTER}')


        # try:
        #     driver.find_element(By.XPATH, '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr/td/span/span[1]/button').click()
        #                                   '/html/body/div[16]/div[2]/div/div/div/form/table/tbody/tr/td/span/span[1]/button'
        # except Exception:
        #     try:
        #         sleep(5)
        #         driver.find_element(By.XPATH, '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr/td/span/span[1]/button').click()
        #     except Exception:
        #         print('fallo al dar aceptar en ENVIAR')
        sleep(7)

        try:
            ###### CLICK BUSCAR
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[1]/div[2]/button[2]').click()
            ###### INGRESO DEL ESTATUS 
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]').click()
            estadoInput = driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]/input')
            estadoInput.clear()
            estadoInput.send_keys("Aplicado")
            sleep(2)

            ###### INGRESO DE LA FECHA
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]').click()
            estadoInput = driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]/input')
            estadoInput.clear()
            estadoInput.send_keys(fechaAjusteGenerado)
            sleep(2)

            ###### INGRESO DEL MOTIVO
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]').click()
            estadoInput = driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]/input')
            estadoInput.clear()
            estadoInput.send_keys("CONVENIO DE COBRANZA")
            # estadoInput.send_keys(Keys.RETURN)
            estadoInput.send_keys(Keys.ESCAPE)
            sleep(2)
            it.send('{ENTER}')
            sleep(5)
        except Exception as e:
            print('Tercera excepcion encontrada: ', e)
            error = 'Ingresar Ajuste'
            return False, error

        

        try:
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]').click()

        except Exception as e:
            print('Cuarta excepcion encontrada: ', e)
            print('-> Ajuste no aplicado')
            error = 'Ajuste NO Aplicado'
            return False, error

        sleep(2)
        print('Consulta saldos')
        it.send('{UP 35}')
        open_item_selenium_wait(driver, xpath =  solicitud_ajuste['consulta_saldos']['xpath'])
        sleep(3)
        open_item_selenium_wait(driver ,name = pantalla_unica['saldo_pendiente']['name'], xpath =  pantalla_unica['saldo_pendiente']['xpath'])
        print('AJUSTE REALIZADO CON EXITO ☺')
        
        return True, ''
        

    
    except Exception as e:
        print(f'ERROR ajustando el cargo extemporaneo. Caso NO. . CUENTA:')
        description_error('13','aplicacion_ajuste_cargo_extemporaneo',e)
        return False, 'Excepcion'

