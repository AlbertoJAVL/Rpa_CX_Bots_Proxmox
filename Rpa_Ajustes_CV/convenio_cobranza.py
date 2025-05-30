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
from unidecode import unidecode
#---------Mis funciones---------------#
from utileria import *
from logueo import *
import Services.ApiCyberHubOrdenes as api
from rutas import *


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

def busquedaCNTipificado(driver, busqueda, meses, promocionMes):
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



    fechaInicioMes = date.today()
    fechaInicioMes = fechaInicioMes.replace(day=1)
    fechaInicioMes = fechaInicioMes.strftime('%d/%m/%Y')

    fechaInicioMes = ">= '{}'".format(fechaInicioMes)


    driver.find_element(By.XPATH, casos_negocio['fechaCierre']).click()
    fechaCierre  = driver.find_element(By.XPATH, casos_negocio['fechaCierre'] + '/input')
    fechaCierre.send_keys(fechaInicioMes)
    sleep(100)
    
    sleep(2)
    driver.find_element(By.XPATH, casos_negocio['motivoCliente']).click()
    motivoCliente  = driver.find_element(By.XPATH, casos_negocio['motivoCliente'] + '/input')
    motivoCliente.send_keys(busqueda)
    motivoCliente.send_keys(Keys.RETURN)
    motivoCliente.send_keys(Keys.RETURN)
    sleep(8)


    try:
        driver.find_element(By.XPATH, casos_negocio['fechaCierre']).click()
        sleep(2)
        fechaCNObtenido = driver.find_element(By.XPATH, casos_negocio['fechaCierre'] + '/input')
        fechaCNObtenido = fechaCNObtenido.get_attribute("value")
        print('fecha cn tipificado: ', fechaCNObtenido)
        fechaCNObtenido = formatoFecha(fechaCNObtenido, True)
        fechaActual = datetime.today()

        diferencia_fechas = fechaActual - fechaCNObtenido
        print('Diferencia entre hoy y la feha de cierre: ', diferencia_fechas)

        if promocionMes == False:

            tres_meses = timedelta(days=int(meses)*30)

            if diferencia_fechas > tres_meses:
                print('Sin CN tipificado recientemente')
            else:
                print('CN tipificado recientemente')
                error = 'Error CN tipificado'
                print('Error ', error)
                return True, error

        else:

            mes = timedelta(days=int(1)*30)

            if diferencia_fechas > mes:
                print('Sin CN tipificado recientemente')
            else:
                print('CN tipificado recientemente')
                error = 'Error CN tipificado'
                print('Error ', error)
                return True, error
            
    except Exception as e:
        print(e)
        return False, ''

def busquedaColuman(driver, colBusqueda):
    buscandoColumna = True
    contador = 2
    while buscandoColumna == True:
        try:
            try:
                columna = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{str(contador)}]/div")
            except:
                columna = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{str(contador)}]/div")
            columna = driver.execute_script("return arguments[0].textContent;", columna)
            print('Name column : <',columna)
            sleep(5)
            if colBusqueda in columna:
                buscandoColumna = False
                return str(contador)
            else:
                contador += 1
        except:
            print('Buscando...')
            contador += 1

def busquedaOpc(driver, opcBusqueda, ruta):

    buscandoOpc = True
    contador = 0

    while buscandoOpc == True:

        try:

            contador += 1
            path = ruta.replace('{contador}', str(contador))
            busquedaObtenida = driver.find_element(By.XPATH, path)
            busquedaObtenida = driver.execute_script("return arguments[0].textContent;", busquedaObtenida)
            print(f'->column: {busquedaObtenida}')

            if opcBusqueda in busquedaObtenida:
                busquedaObtenida = driver.find_element(By.XPATH, path).click()
                buscandoOpc = False
                sleep(15)
                return ''

        except Exception as e:
            if contador == 100:
                error = 'Error historial pago'
                return error


def validacion_cuenta_convenio_cobranza(driver, no_cuenta, no_caso, meses):
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
        status_pantalla_unica,error = pantalla_unica_consulta(driver, no_cuenta) 
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '▬')
            return False ,'Error Pantalla Unica','',''

        sleep(6)
        try:
            driver.find_element(By.XPATH, casos_negocio['consultaSaldo']).click()
        except Exception as e:
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[1]/div[3]/button[8]').click()

        print('▬ Inician Obtencion Promocion, fecha y pago ▬')
        sleep(12)


        driver.find_element(By.XPATH, casos_negocio['lupa']).click()
        sleep(3)
        envioCN  = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/input')
        envioCN.send_keys(no_caso)
        envioCN.send_keys(Keys.RETURN)
        sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]').click()
        sleep(2)
        comentario = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]/textarea')
        comentario = comentario.get_attribute("value")

        print(comentario)

        comentario = comentario.replace("\n", "")
        print('##################')
        print(comentario)                  
        
        comentario = unidecode(comentario)
        comentario = comentario.replace('á', 'a')
        comentario = comentario.replace('é', 'e')
        comentario = comentario.replace('í', 'i')
        comentario = comentario.replace('ó', 'o')
        comentario = comentario.replace('ú', 'u')

        # patterns = {
        #     "Cantidad a pagar" : r"Cantidad a pagar (\d+\.\d+)",
        #     "Fecha pago" : 
        # }
        

        patron_promocion = r"Tipo promocion(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Saldo ajustar|Promocion|Cantidad a pagar|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
        resultado_promocion = re.search(patron_promocion, comentario)
        if resultado_promocion:
            promocion = resultado_promocion.group(1)
            promocion = promocion.replace(":", "")
        else:
            patron_promocion = r"Tipo de promocion(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Saldo ajustar|Promocion|Cantidad a pagar|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
            resultado_promocion = re.search(patron_promocion, comentario)
            if resultado_promocion:
                promocion = resultado_promocion.group(1)
                promocion = promocion.replace(":", "")
            else:
                error = 'Error en formato plantilla'
                print(error)
                return False, error, '',''
        
        patron_cantidad_pagar = r"Cantidad a pagar(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Saldo ajustar|Promocion|Cantidad a pagar|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
        resultado_cantidad = re.search(patron_cantidad_pagar, comentario)
        if resultado_cantidad:
            cantidad_pagar_p = resultado_cantidad.group(1)
            cantidad_pagar_p = cantidad_pagar_p.replace(":", "")
        else:
            patron_cantidad_pagar = r"Cantidad pagar(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Saldo ajustar|Promocion|Cantidad a pagar|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
            resultado_cantidad = re.search(patron_cantidad_pagar, comentario)
            if resultado_cantidad:
                cantidad_pagar_p = resultado_cantidad.group(1)
                cantidad_pagar_p = promocion.replace(":", "")
            else:
                error = 'Error en formato plantilla'
                print(error)
                return False, error, '',''
            

        patron_SaldoAjustar = r"Saldo a ajustar(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Cantidad a pagar|Promocion|Tipo promocion|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
        resultado_saldoAjustar = re.search(patron_SaldoAjustar, comentario)
        if resultado_saldoAjustar:
            saldoAjustar = resultado_saldoAjustar.group(1)
            saldoAjustar = saldoAjustar.replace(":", "")
            saldoAjustar = saldoAjustar.replace(" ", "")
            saldoAjustar = saldoAjustar[0:5]
            saldoAjustar = re.sub(r'[^0-9.]', '', saldoAjustar)
            print(f'Saldo a ajustar {saldoAjustar}')
            

            try: 
                if int(saldoAjustar) == 0:
                    error = 'Error en formato plantilla'
                    print(error)
                    return False, error, '',''

            except:
                if float(saldoAjustar) == 0:
                    error = 'Error en formato plantilla'
                    print(error)
                    return False, error, '',''
        else:
            patron_SaldoAjustar = r"Saldo ajustar(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Cantidad pagar|Promocion|Tipo promocion|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
            resultado_saldoAjustar = re.search(patron_SaldoAjustar, comentario)
            if resultado_saldoAjustar:
                saldoAjustar = resultado_saldoAjustar.group(1)
                saldoAjustar = saldoAjustar.replace(":", "")
                saldoAjustar = saldoAjustar.replace(" ", "")
                saldoAjustar = saldoAjustar[0:5]
                saldoAjustar = re.sub(r'[^0-9.]', '', saldoAjustar)
                print(f'Saldo a ajustar {saldoAjustar}')
                

                try: 
                    if int(saldoAjustar) == 0:
                        error = 'Error en formato plantilla'
                        print(error)
                        return False, error, '',''

                except:
                    if float(saldoAjustar) == 0:
                        error = 'Error en formato plantilla'
                        print(error)
                        return False, error, '',''
            else:
                error = 'Error en formato plantilla'
                print(error)
                return False, error, '',''

        patron_fechaPago = r"Fecha pago(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Tipo promocion|Saldo ajustar|Promocion|Cantidad a pagar|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
        resultado_fechaPago = re.search(patron_fechaPago, comentario)
        if resultado_fechaPago:
            fechaPago2 = resultado_fechaPago.group(1)
            fechaPago2 = fechaPago2.replace(":", "")
            fechaPago2 = fechaPago2.rstrip()
            fechaPago2 = fechaPago2.lstrip()
        else:
            patron_fechaPago = r"Fecha de pago(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Tipo promocion|Saldo ajustar|Promocion|Cantidad a pagar|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
            resultado_fechaPago = re.search(patron_fechaPago, comentario)
            if resultado_fechaPago:
                fechaPago2 = resultado_fechaPago.group(1)
                fechaPago2 = fechaPago2.replace(":", "")
                fechaPago2 = fechaPago2.rstrip()
                fechaPago2 = fechaPago2.lstrip()
            else:
                error = 'Error en formato plantilla'
                print(error)
                return False, error, '',''

        print(fechaPago2)

        try:
            fechaPago = datetime.strptime(fechaPago2, "%d/%m/%Y").date()
            fechaPago = fechaPago - timedelta(days=2)
            fechaPago = str(fechaPago)
        except:
            try:
                fechaPago = datetime.strptime(fechaPago2, '%d-%m-%Y').date()
                fechaPago = fechaPago - timedelta(days=2)
                fechaPago = fechaPago.strftime("%d/%m/%Y")
            except:
                try:
                    fechaPago = datetime.strptime(fechaPago2, '%Y/%m/%d').date()
                    fechaPago = fechaPago - timedelta(days=2)
                    fechaPago = fechaPago.strftime("%d/%m/%Y")
                except:
                    try:
                        fechaPago = datetime.strptime(fechaPago2, '%Y-%m-%d').date()
                        fechaPago = fechaPago - timedelta(days=2)
                        fechaPago = fechaPago.strftime("%d/%m/%Y")
                    except  Exception as e:
                        error = 'Error en formato plantilla'
                        print(e)
                        print(error)
                        return False, error, '',''


        if 'LATE FEE' in promocion.upper():
            promo = 'LATE FEE'
            patron_cantidadPagar = r"Cantidad a pagar(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Saldo ajustar|Promocion|Tipo promocion|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
            resultado_cantidadPagar = re.search(patron_cantidadPagar, comentario)
            if resultado_cantidadPagar:
                cantidadPagar = resultado_cantidadPagar.group(1)
                cantidadPagar = cantidadPagar.replace(":", "")
                cantidadPagar = cantidadPagar.replace("$", "")
            else:
                error = 'No aplica sin cantidad a pagar late fee'
                print(error)
                return False, error, '',''
            
            patron_SaldoAjustar = r"Saldo ajustar(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Ciudad|Region|Hub|Gestionable|Promocion|Tipo gestion|Tipo promesa|No. Empleado|Nombre asesor|Fecha pago|Cantidad a pagar|Promocion|Tipo promocion|FOLIO|Fecha de creacion|Usuario de red|Fecha tolerancia|$))"
            resultado_saldoAjustar = re.search(patron_SaldoAjustar, comentario)
            if resultado_saldoAjustar:
                saldoAjustar = resultado_saldoAjustar.group(1)
                saldoAjustar = saldoAjustar.replace(":", "")
            else:
                error = 'Error en formato plantilla'
                print(error)
                return False, error, '',''
        else:
            if '150' in promocion:
                cantidadPagar = '150'
                promo = 'RX150'
            elif '250' in promocion:
                cantidadPagar = '250'
                promo = 'RX250'
            elif '100' in promocion:
                cantidadPagar = '100'
                promo = 'RX100'
            elif 'Baby' in promocion or 'baby' in promocion:
                promo = 'RX50'
                cantidadPagar = cantidad_pagar_p
            elif '200' in promocion:
                promo = 'RX200'
                cantidadPagar = cantidad_pagar_p
            elif '1000' in promocion or '1,000' in promocion:
                promo = 'RX1000'
                cantidadPagar = cantidad_pagar_p
            elif '20%' in promocion or '20 %' in promocion or '2 0 %' in promocion:
                promo = promocion
                cantidadPagar = cantidad_pagar_p
            elif '50%' in promocion or '50 %' in promocion or '5 0 %' in promocion:
                cantidadPagar = '0'
                promo = 'RX50%'
            else:
                error = 'No aplica promocion no detectada'
                print(error)
                return False, error, '',''

        print(f'Promocion: {promocion}')
        print(f'Cantidad a pagar: {cantidadPagar}')
        print('▬ Inician validaciones de cuenta ▬')
        sleep(5)
        
        print('▬ Tipo Cuenta')
        try:
            tipo_cuenta = driver.find_element(By.XPATH, pantalla_unica['tipo_cuenta']['xpath'])
            tipo_cuenta = tipo_cuenta.get_attribute("value")
        except Exception:
            print('cuenta Cablevision')
            tipo_cuenta = driver.find_element(By.XPATH, pantalla_unica['tipo_cuenta']['xpath2'])
            tipo_cuenta = tipo_cuenta.get_attribute("value")
        # tipo_cuenta = my_copy_by_xpath(driver, pantalla_unica['tipo_cuenta']['xpath'])
        if tipo_cuenta.upper() not in ['RESIDENCIAL', 'NEGOCIO']:
            error = 'No Aplica tipo cuenta'
            print('No Aplica ', error)
            return False, error,'',''
        

        print('▬ Subtipo Cuenta')
        try:
            subtipo_cuenta = driver.find_element(By.XPATH, pantalla_unica['subtipo_cuenta']['xpath'])
            subtipo_cuenta = subtipo_cuenta.get_attribute("value")
        except Exception:
            print('cuenta Cablevision')
            subtipo_cuenta = driver.find_element(By.XPATH, pantalla_unica['subtipo_cuenta']['xpath2'])
            subtipo_cuenta = subtipo_cuenta.get_attribute("value")
        # subtipo_cuenta = my_copy_by_xpath(driver, pantalla_unica['subtipo_cuenta']['xpath'])
        if subtipo_cuenta.upper() not in ['NORMAL']:
            error = 'No Aplica por subtipo de cuenta'
            print('No Aplica ', error)
            return False, error,'',''

        # print('▬ Saldo pendiente') 
        # try:
        #     saldo_pendiente = driver.find_element(By.XPATH, pantalla_unica['saldo_pendiente']['xpath'])
        #     saldo_pendiente = saldo_pendiente.get_attribute("value")
        # except Exception:
        #     print('cuenta Cablevision')
        #     saldo_pendiente = driver.find_element(By.XPATH, pantalla_unica['saldo_pendiente']['xpath2'])
        #     saldo_pendiente = saldo_pendiente.get_attribute("value")
        # # if open_item_selenium_wait(driver, xpath =  pantalla_unica['saldo_pendiente']['xpath']) != True: return False, True, ''

        # # saldo_pendiente = my_copy_by_xpath(driver, pantalla_unica['saldo_pendiente']['xpath'])
        # if ',' in saldo_pendiente:
        #     saldo_pendiente = saldo_pendiente.replace(',', '')
        # if saldo_pendiente != None:
        #     try:
        #         saldo_pendiente = float(saldo_pendiente)
        #     except Exception as e:
        #         print(f'No se pudo convertir rl saldo a numero: {e}')
        #         error = 'No Aplica saldo invalido'
        #         print('No Aplica ', error)
        #         return False,error,'',''
        # if saldo_pendiente <= 0:                    

        #     error = 'No Aplica sin saldo vencido'
        #     print('No Aplica ', error)
        #     return False,error,'',''
        # else:
        #     if '50%' in promocion or '50 %' in promocion or '5 0 %' in promocion:
        #         cantidadPagar = saldo_pendiente
        #         saldoMitad = cantidadPagar
        #     print(f'El saldo pendiente es de {saldo_pendiente} MXN')

        print('-> Validando Pago realizado')

        driver.find_element(By.XPATH, "//button[@aria-label='Historial de Pago Menú List']").click()
        sleep(6)

        # 29732943

        agregacionCol = busquedaOpc(driver, 'Columnas mostradas   [Ctrl+Mayús+K]', pantalla_consultad['opcMostarColum'])
        if agregacionCol != '':
            agregacionCol = busquedaOpc(driver, 'Columnas mostradas   [Ctrl+Mayús+K]', pantalla_consultad['opcMostarColum2'])
            if agregacionCol != '':
                error = 'Historial de Pagos'
                print(error)
                return False, error, '',''


        driver.find_element(By.XPATH, "//option[@value='Importe del Pago']").click()
        sleep(3)

        driver.find_element(By.XPATH, "//a[@aria-label='Columnas mostradas:Mostrar']").click()
        sleep(3)

        driver.find_element(By.XPATH, "//button[@aria-label='Columnas mostradas Applet de formulario:Guardar']").click()
        sleep(60)
        


        labelEngranePagos = 'Historial de Pago Applet de lista:Consulta'
        driver.find_element(By.XPATH, "//button[@aria-label='" + labelEngranePagos + "']").click()
        sleep(3)

        columnaNum = busquedaColuman(driver, 'Fecha de Pago')
        sleep(1)
        try:
            driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
            colFechaPago = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
        except:
            try:
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
                colFechaPago = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
            except:
                error = 'Historial de Pagos'
                print(error)
                return False, error, '',''
        
        colFechaPago.send_keys(f">= '{fechaPago}'")
        sleep(3)

        columnaNum = busquedaColuman(driver, 'Importe del Pago')
        sleep(1)
        try:
            driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
            colFechaPago = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
        except:
            try:
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
                colFechaPago = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
            except:
                error = 'Historial de Pagos'
                print(error)
                return False, error, '',''
        
        cantidadPagar2 = cantidadPagar.replace('$', '')
        colFechaPago.send_keys(f">= '{cantidadPagar2}'")
        sleep(3)


        columnaNum = busquedaColuman(driver, 'Estado')
        sleep(1)
        try:
            driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
            colEstado = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
        except:
            try:
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
                colEstado = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
            except:
                error = 'Historial de Pagos'
                print(error)
                return False, error, '',''
        colEstado.send_keys("'Aplicado'")
        colEstado.send_keys(Keys.RETURN)
        sleep(3)
        # colEstado.send_keys(Keys.RETURN)
        # sleep(3)

        try:
            driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
            pagoRealizado = True
        except:
            try:
                driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
                pagoRealizado = True
            except:
                # error = 'Error Cambio Campos'
                # pnt(error)
                # return False, error, '',''ri
                
                pagoRealizado = False
                error = 'No Aplica pago fecha rango'
                print(error)
                sleep(1000)
                return False, error, '',''

        # columnaNum = busquedaColuman(driver, 'Importe del Pago')
        # sleep(1)
        # try:
        #     driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
        #     colEstado = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
        # except:
        #     try:
        #         driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]").click()
        #         colEstado = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{columnaNum}]/input")
        #     except:
        #         error = 'Error Cambio Campos Historial Pagos'
        #         print(error)
        #         return False, error, '',''
        # colEstado.send_keys()
        # colEstado.send_keys(Keys.RETURN)
        # colEstado.send_keys(Keys.RETURN)
        # /html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[2]/div
        
        
        print('monto Pagado: ', cantidadPagar)

        if '150' in promocion:
            print('Se verifica por un RX150')
            
            if pagoRealizado == True: print('Pago Realizado Correcto de RX 150'); ajuste = str(saldoAjustar)
            else:
                error = 'No Aplica Pago Incorrecto'
                print(error)
                return False, error,'',''
        elif '100' in promocion:
            print('Se verifica por un RX100')
            # ajuste = saldo_pendiente
            
            if pagoRealizado == True: print('Pago Realizado Correcto de RX 100'); ajuste = str(saldoAjustar)
            else:
                error = 'No Aplica Pago Incorrecto'
                print(error)
                return False, error,'',''
        elif '250' in promocion:
            print('Se verifica por un RX250')
            # ajuste = saldo_pendiente
            
            if pagoRealizado == True: print('Pago Realizado Correcto de RX 250'); ajuste = str(saldoAjustar)
            else:
                error = 'No Aplica Pago Incorrecto'
                print(error)
                return False, error,'',''
        elif '20%' in promocion or '20 %' in promocion or '20%' in promocion or 'R X 2 0%' in promocion or 'R X 2 0 %' in promocion:
            print('Se verifica por un RX 20%')
            # ajuste = saldo_pendiente
            
            if pagoRealizado == True: print('Pago Realizado Correcto de RX 20'); ajuste = str(saldoAjustar)
            else:
                error = 'No Aplica Pago Incorrecto'
                print(error)
                return False, error,'',''

        elif '50%' in promocion or '50 %' in promocion or '50%' in promocion or 'R X 5 0%' in promocion or 'R X 5 0 %' in promocion:
            print('Se verifica por un RX50%')
            # ajuste = (saldo_pendiente * (-1)) - monto
            
            
            if pagoRealizado == True:
                ajuste = saldoAjustar
            else:
                error = 'No Aplica saldo y pago no coincide para rx 50%'
                print(error)
                return False, error, '',''

        
        elif 'LATE FEE' in promocion.upper():
            ajuste = str(saldoAjustar)

        else:
            error = 'No Aplica promocion no detectada'
            print(error)
            return False, error, '',''

            
        print('-> Monto del ajuste a aplicar: ', ajuste)

        print('▬ Estado de la cuenta')
        try:
            estado_cuenta = driver.find_element(By.XPATH, pantalla_unica['estado_cuenta']['xpath'])
            estado_cuenta = estado_cuenta.get_attribute("value")
        except Exception:
            print('cuenta Cablevision')
            estado_cuenta = driver.find_element(By.XPATH, pantalla_unica['estado_cuenta']['xpath2'])
            estado_cuenta = estado_cuenta.get_attribute("value")
        # estado_cuenta = my_copy_by_xpath(driver, pantalla_unica['estado_cuenta']['xpath'])
        if estado_cuenta.upper() not  in ['INACTIVA', 'INACTIVO', 'ACTIVO', 'ACTIVA','NO PAGO']:
            error = 'No Aplica por estado de la cuenta'
            print('No Aplica ', error)
            return False, error,'',''

        # print('validando fecha de los 5 dias')

        # fechaPagoAplicado = datos['fecha']
        # fechaPagoAplicado = datetime.strptime(fechaPagoAplicado, '%d/%m/%Y %H:%M:%S').date()
        # fechaPagoAplicado = fechaPagoAplicado.strftime('%d/%m/%Y')
        # fechaPagoAplicado = datetime.strptime(fechaPagoAplicado, '%d/%m/%Y').date()

        # rangoMenorDias = fechaPagoAplicado - timedelta(days=2)
        # rangoMayorDias = fechaPagoAplicado + timedelta(days=2)

        # rangoMenorDias = datetime.strptime(str(rangoMenorDias), '%Y-%m-%d').date()
        # rangoMenorDias = rangoMenorDias.strftime('%d/%m/%Y')
        # # rangoMenorDias = datetime.strptime(rangoMenorDias, '%d/%m/%Y').date()

        # rangoMayorDias = datetime.strptime(str(rangoMayorDias), '%Y-%m-%d').date()
        # rangoMayorDias = rangoMayorDias.strftime('%d/%m/%Y')
        # rangoMayorDias = datetime.strptime(rangoMayorDias, '%d/%m/%Y').date()


        # print('Validando pago realizado')
        # sleep(2)
        # it.send('{DOWN 6}')
        # sleep(3)
        # # driver.find_element(By.XPATH, historial_pagos['lupa']).click()
        # # sleep(4)
        # # driver.find_element(By.XPATH, historial_pagos['opcColumnas']).click()
        # # sleep(8)
        # # try:
        # #     driver.find_element(By.XPATH, historial_pagos['montoColum']).click()
        # #     sleep(3)
        # #     driver.find_element(By.XPATH, historial_pagos['asiganrColumn']).click()
        # #     sleep(3)
        # #     driver.find_element(By.XPATH, historial_pagos['guardarColumn']).click()
        # #     sleep(8)
        # # except Exception:
        # #     driver.find_element(By.XPATH, historial_pagos['guardarColumn']).click()
        # #     sleep(8)

        # try:

        #     driver.find_element(By.XPATH, historial_pagos['lupa']).click()
        #     sleep(4)
        
        # except Exception:
        #     try:
                
        #         driver.find_element(By.XPATH, historial_pagos['lupa2']).click()
        #         sleep(4)
            
        #     except Exception:
        #         error = 'Error Cuenta con Inconsistencia'
        #         print(error)
        #         return False, error, ''

        
        # queryFechas = f">= '{str(rangoMenorDias)}' AND <= '{str(rangoMayorDias)}'"

        # try:
        #     driver.find_element(By.XPATH, historial_pagos['inputFecha']).click()
        #     fechaPago = driver.find_element(By.XPATH, historial_pagos['inputFecha'] + '/input')
        # except Exception:
        #     driver.find_element(By.XPATH, historial_pagos['inputFechaCa']).click()
        #     fechaPago = driver.find_element(By.XPATH, historial_pagos['inputFechaCa'] + '/input')
        
        # fechaPago.send_keys(queryFechas)
        
        # sleep(1)
        
        # try:
        #     driver.find_element(By.XPATH, historial_pagos['inputStatus']).click()
        #     estadoPago = driver.find_element(By.XPATH, historial_pagos['inputStatus'] + '/input')
        # except Exception:
        #     driver.find_element(By.XPATH, historial_pagos['inputStatusCa']).click()
        #     estadoPago = driver.find_element(By.XPATH, historial_pagos['inputStatusCa'] + '/input')

        # estadoPago.send_keys('Aplicado')
        # estadoPago.send_keys(Keys.RETURN)
        # estadoPago.send_keys(Keys.RETURN)

        # sleep(1)
        
        # try:
        #     driver.find_element(By.XPATH, historial_pagos['resultado']).click()
        #     fechaRes = driver.find_element(By.XPATH, historial_pagos['resultado']+'/input')
        #     fechaRes = fechaRes.get_attribute("value")
        #     print('fechaObtenida : ', fechaRes)
            
        # except Exception:
            
        #     try:
        #         driver.find_element(By.XPATH, historial_pagos['resultadoCa']).click()
        #         fechaRes = driver.find_element(By.XPATH, historial_pagos['resultadoCa']+'/input')
        #         fechaRes = fechaRes.get_attribute("value")
        #         print('fechaObtenida : ', fechaRes)
            
        #     except Exception:
        #         error = 'Error Sin Pago'
        #         print(error)
        #         return False, error, ''


        # try:
        #     sleep(5)
        #     driver.find_element(By.XPATH, historial_pagos['pago']).click()
        #     sleep(6)
        # except Exception:
        #     sleep(5)
        #     driver.find_element(By.XPATH, historial_pagos['pagoCa']).click()
        #     sleep(6)

        # try:
        #     driver.find_element(By.XPATH, historial_pagos['inputMonto']).click()
        #     montoPagado = driver.find_element(By.XPATH, historial_pagos['inputMonto']+'/input')
        #     montoPagado = montoPagado.get_attribute("value")
        #     print('Monto del pago realizado: ', montoPagado)

        #     if str(monto) in montoPagado:
        #         print('Pago Realizado correctamente')
        #     else:
        #         error = 'Error Pago Fecha Rango'
        #         print(error)
        #         return False, error, ''

        # except Exception:
        #     error = 'Errro Pago no encontrado'
        #     print(error)
        #     return False, error, ''

        # try:
        #     sleep(3)
        #     driver.find_element(By.XPATH, paginaInicialFelcha).click()
        # except Exception:
        #     print('')

        # status_pantalla_unica = pantalla_unica_consulta(driver, no_cuenta) 
        # if status_pantalla_unica == False:
        #     text_box('Cuenta no valida', '▬')
        #     return False ,'Error Cuenta no valida',''

        sleep(6)



        #Busqueda CN Tipificado
        # if 'LATE FEE' not in promocion:

        #     if '20%' in promocion or '20 %' in promocion or '2 0 %' in promocion:
        #         resultadoBusqueda, error = busquedaCNTipificado(driver, 'CONVENIO COBRANZA', meses, True)
        #     else:
        #         resultadoBusqueda, error = busquedaCNTipificado(driver, 'CONVENIO COBRANZA', meses, False)

        #     if resultadoBusqueda == True:
        #         error = 'No Aplica CN Convenio Cobranza Previo Tipificado'
        #         print(error)
        #         return False, error,'',''
        #     else:
        #         print('No hay CN tipificado por convenio cobranza')

        #         if '20%' in promocion or '20 %' in promocion or '2 0 %' in promocion:
        #             resultadoBusqueda, error = busquedaCNTipificado(driver, 'CARGO EXTEMPORANEO', meses, True)
        #         else:
        #             resultadoBusqueda, error = busquedaCNTipificado(driver, 'CARGO EXTEMPORANEO', meses, False)

        #         if resultadoBusqueda == True:
        #             error = 'No Aplica CN Cargo Extemporaneo Previo Tipificado'
        #             print(error)
        #             return False, error,'',''
        #         else:
        #             print('Sin CN previo tipificado')

        print('• Monto de ajuste: ', ajuste)

        print('▬ Solicitudes de ajuste')

        # sleep(2)

        # #Busqueda Ajuste previo

        if 'RX' in promo:
            print('Buscando algun ajuste previo')
            try:
                driver.find_element(By.XPATH, pantalla_consultad['busquedaSolicitudAjuste']).click()
                sleep(5)
            except Exception as e:
                print(e)
                try:
                    driver.find_element(By.XPATH, pantalla_consultad['busquedaSolicitudAjuste']).click()
                except Exception as e:
                    print(e)
                    error = 'Error aplicacion ajuste:message'
                    return False, error,'',''
            sleep(5)
            fechaInicioMes = date.today() - timedelta(days=30)
            # fechaInicioMes = fechaInicioMes.replace(day=1)
            fechaInicioMes = fechaInicioMes.strftime('%d/%m/%Y')

            fechaInicioMes = ">= '{}'".format(fechaInicioMes)
            sleep(3)
            driver.find_element(By.XPATH, solicitud_ajuste['fechaAjuste']).click()
            sleep(2)
            fechaAjuste = driver.find_element(By.XPATH, solicitud_ajuste['fechaAjuste'] + '/input')
            fechaAjuste.send_keys(fechaInicioMes)
            sleep(2)
            driver.find_element(By.XPATH, solicitud_ajuste['motivoAjuste']).click()
            sleep(2)
            motivo = driver.find_element(By.XPATH, solicitud_ajuste['motivoAjuste'] + '/input')
            motivo.send_keys('CONVENIO DE COBRANZA')
            sleep(2)
            driver.find_element(By.XPATH, solicitud_ajuste['estadoAjuste']).click()
            sleep(2)
            estadoAjuste = driver.find_element(By.XPATH, solicitud_ajuste['estadoAjuste'] + '/input')
            estadoAjuste.send_keys('Aplicado')
            estadoAjuste.send_keys(Keys.RETURN)
            estadoAjuste.send_keys(Keys.RETURN)
            sleep(8)

        elif  'LATE FEE' in promo.upper():
            sleep(4)
            print('Buscando algun ajuste previo')
            try:
                driver.find_element(By.XPATH, pantalla_consultad['busquedaSolicitudAjuste']).click()
                sleep(5)
            except Exception as e:
                print(e)
                try:
                    driver.find_element(By.XPATH, pantalla_consultad['busquedaSolicitudAjuste']).click()
                except Exception as e:
                    print(e)
                    error = 'Error aplicacion ajuste:message'
                    return False, error,'',''
            sleep(8)
            fechaInicioMes = date.today() - timedelta(days=30)
            # fechaInicioMes = fechaInicioMes.replace(day=1)
            fechaInicioMes = fechaInicioMes.strftime('%d/%m/%Y')

            fechaInicioMes = ">= '{}'".format(fechaInicioMes)
            sleep(3)
            driver.find_element(By.XPATH, solicitud_ajuste['fechaAjuste']).click()
            sleep(2)
            fechaAjuste = driver.find_element(By.XPATH, solicitud_ajuste['fechaAjuste'] + '/input')
            fechaAjuste.send_keys(fechaInicioMes)
            sleep(2)
            driver.find_element(By.XPATH, solicitud_ajuste['motivoAjuste']).click()
            sleep(2)
            motivo = driver.find_element(By.XPATH, solicitud_ajuste['motivoAjuste'] + '/input')
            motivo.send_keys('CARGO POR PAGO EXTEMPORANEO')
            sleep(2)
            driver.find_element(By.XPATH, solicitud_ajuste['estadoAjuste']).click()
            sleep(2)
            estadoAjuste = driver.find_element(By.XPATH, solicitud_ajuste['estadoAjuste'] + '/input')
            estadoAjuste.send_keys('Aplicado')
            estadoAjuste.send_keys(Keys.RETURN)
            estadoAjuste.send_keys(Keys.RETURN)
            sleep(5)
        

        try:
            print('Obtenidnedo valor de la fecha del ajuste')
            driver.find_element(By.XPATH, solicitud_ajuste['fechaAjuste']).click()
            sleep(5)
            fechaAjusteObtenido = driver.find_element(By.XPATH, solicitud_ajuste['fechaAjuste'] + '/input')
            fechaAjusteObtenido = fechaAjusteObtenido.get_attribute("value")
            print('fecha Ajuste obtenido: ', fechaAjusteObtenido)
            sleep(5)
            fechaAjusteObtenido = formatoFecha(fechaAjusteObtenido, True)
            fechaActual = datetime.today()
            diferencia_fechas = fechaActual - fechaAjusteObtenido
            print(fechaActual)
            print(fechaAjusteObtenido)
            print(diferencia_fechas)
            print('Diferencia entre hoy y la feha de cierre: ', diferencia_fechas)
            sleep(5)
            
            if 'M' in promo.upper() or '20%' in promo:
                print('No aplica Busqueda de ajuste')
            else:
                if 'RX' in promo.upper():
                    limite = timedelta(days=120)

                elif 'LATE FEE' in promo.upper():
                    limite = timedelta(days=30)

                if diferencia_fechas > limite:
                    print('El ultimo ajuste es mayor a 4 meses')
                else:
                    print('Ultimo ajuste menor a 4 meses')
                    error = 'No Aplica Ajuste reciente'
                    print('No Aplica ', error)
                    return False, error,'',''
        except Exception:
            print('SIN AJUSTE PREVIO')
            
        sleep(5)
 
        print('Validaciones correctas')
        return True, '', ajuste, promo

    except Exception as e:
        print(f'No Aplica ajustando el cargo extemporaneo. Caso NO. {no_caso}. CUENTA: {no_cuenta}')
        description_error('11','validacion_cuenta_cargo_extemporaneo',e)
        print('No Aplica ', e)
        if 'Alert Text' in str(e):
            return False, 'Error aplicacion ajuste:alert text','',''
        elif 'Message' in str(e):
            return False, 'Error aplicacion ajuste:message','',''

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

