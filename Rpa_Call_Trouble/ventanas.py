from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

from time import sleep



def cargaElementos(driver, xpath):

    cargando = True
    contador = 0

    while cargando:
        try:
            driver.find_element(By.XPATH, xpath).click()
            sleep(5)
            return True
        
        except:
            sleep(1)
            contador += 1
            if contador == 50: return False

def ingresoInfo(driver, xpath, valor, nombreCampo = 'Campo X', enter = False):

    campo = driver.find_element(By.XPATH, xpath)
    campo.click()
    campo.clear()
    campo.send_keys(valor)
    if enter == True: campo.send_keys(Keys.RETURN); sleep(2)
    print(f'-> {nombreCampo} OK!')

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
    
def busquedaElemento(driver, elemento, xpath):

    buscandoElemento = True
    contador = 0

    while buscandoElemento:
        
        try:
            print('buscando...')
            contador += 1
            xpathF = xpath.replace('{contador}', str(contador))
            valor = driver.find_element(By.XPATH, xpathF)
            valor = driver.execute_script("return arguments[0].textContent;", valor)

            if elemento in valor:
                driver.find_element(By.XPATH, xpathF).click()
                buscandoElemento = False

            if contador == 200: return False

        except: 
            if contador == 200: return False

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
    
def busquedaCuenta(driver, cuenta, tipoOrden, motivoOrden, comentarios):

    try:

        sleep(5)
        validacion = cargaElementos(driver, "//a[@title='Pantalla Única de Consulta']")
        if validacion == False:
            return 1, 'Error Pantalla NO Carga', ''
        
        validacion = cargaElementos(driver, '//button[@title="Pantalla Única de Consulta Applet de formulario:Consulta"]')
        if validacion == False:
            return 1, 'Error Pantalla NO Carga', ''
        print('-> Pantalla Unica Consulta Cargada')

        validacion = cargaElementos(driver, '//input[@aria-label="Numero Cuenta"]')
        if validacion == False:
            return 1, 'Error Pantalla NO Carga', ''
        
        numeroCuenta = driver.find_element(By.XPATH, '//input[@aria-label="Numero Cuenta"]')
        numeroCuenta.send_keys(cuenta)
        numeroCuenta.send_keys(Keys.RETURN)
        print('-> Numero Cuenta Ingresado Correctamente')
        # sleep(1000)
        
        validacion = cargaElementos(driver, '//input[@aria-label="Saldo Total"]')
        if validacion == False:
            return 1, 'Error Pantalla NO Carga', ''
        
        saldoTotal = driver.find_element(By.XPATH, '//input[@aria-label="Saldo Total"]')
        saldoTotal.send_keys(Keys.F2)

        sleep(5)
        cargaElementos(driver, '//input[@name="s_13_2_215_0"]')

        saldo30Dias = driver.find_element(By.NAME, 's_13_2_215_0')
        saldo30Dias = saldo30Dias.get_attribute('value')
        print(saldo30Dias)

        # if float(saldo30Dias) < 130: return 1, 'Error Saldo 30 Días', ''


        driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/button').click()
        sleep(3)
        alert = driver.switch_to.alert
        alert.accept()
        sleep(5)

        print('-> Cuenta Cargada Correctamente')
        return '', ''
        cargaElementos(driver, "//button[@title='Ítems de Facturación Applet de lista:Generar Trouble Call']")

        cargandoAlertText = True
        contador = 0
        numeroOrden = ''

        while cargandoAlertText:

            try:

                alert = driver.switch_to.alert
                alert_text = alert.text
                print("Texto del cuadro emergente:", alert_text)
                alert.accept()

                if 'Se generó la orden' not in alert_text: return 1, f'Error Orden Generada Previamente', ''

                alert_text = alert_text.split(' ')
                for indice, valor in enumerate(alert_text):
                    if 'No.' in valor:
                        numeroOrden = alert_text[indice + 1]
                        numeroOrden = numeroOrden.replace(',', '')
                        print('-> Solicitud Generada Correctamente')
                        print(f'-> Numero Orden Generado: -{numeroOrden}-')
                        cargandoAlertText = False
                        break

            except:

                sleep(1)
                contador += 1
                if contador == 100: return 1, 'Error Alert Text', ''

        
        print('-> Iniciando Busqueda De Orden Para Rellenado')
        driver.find_element(By.XPATH, "//button[@aria-label='Ordenes de Servicio Menú List']").click()
        sleep(5)
        busquedaElemento(driver, "Nueva consulta              [Alt+Q]", '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]/a')
        
        sleep(5)
        busquedaOrdenServicio = driver.find_element(By.XPATH, "//input[@name='Order_Number__eService_']")
        busquedaOrdenServicio.click()
        busquedaOrdenServicio.send_keys(numeroOrden)
        busquedaOrdenServicio.send_keys(Keys.RETURN)
        print('-> Orden Ingresada Correctamente')

        cargandoOrden = True
        contador = 0

        while cargandoOrden:
            try:
                driver.find_element(By.XPATH, "//td[@aria-roledescription='Fecha de la Orden']").click()
                break
            
            except:
                contador += 1
                if contador == 50: return 1, 'Error Buscando Orden Generada', ''

        # driver.find_element(By.LINK_TEXT, '1-186737932921').click()
        driver.find_element(By.LINK_TEXT, numeroOrden.replace(' ', '')).click()
        print('-> Accediendo a Orden')

        validacion = cargaElementos(driver, '//input[@aria-label="No. VTS"]')
        if validacion == False:
            return 1, 'Error Pantalla NO Carga', ''
        print('-> Orden Cargada Correctamente, rellenando...')

        cargaElementos(driver, '//input[@name="s_1_1_187_0"]')

        numeroOrden = driver.find_element(By.NAME, 's_1_1_187_0')
        numeroOrden = numeroOrden.get_attribute('value')
        print(numeroOrden)


        ingresoInfo(driver, '//input[@aria-label="No. VTS"]', 'U001', 'VTS')
        ingresoInfo(driver, '//input[@aria-label="Vendedor"]', 'CVVENSINCOMISION', 'Vendedor')
        ingresoInfo(driver, '//input[@aria-label="Clave del Tecnico Principal"]', 'CVVENSINCOMISION', 'Clave del Tecnico Principal')
        ingresoInfo(driver, '//input[@aria-label="Tipo de orden"]', tipoOrden, 'Tipo de orden')
        ingresoInfo(driver, '//input[@aria-label="Motivo de la orden"]', motivoOrden, 'Motivo de la orden')
        ingresoInfo(driver, '//input[@aria-label="Referido"]', 'Call Center', 'Referido')
        ingresoInfo(driver, '//textarea[@aria-label="Comentarios"]', comentarios, 'Comentarios')
        ingresoInfo(driver, '//input[@aria-label="Horario de Atención"]', 'Matutino Trouble Call 9-14', 'Horario atencion')
        sleep(2)
        driver.find_element(By.XPATH, '//button[@title="Orden de servicio Applet de formulario:Programar"]').click()

        cargandoFechaAtencion = True
        contador = 0

        while cargandoFechaAtencion:

            sleep(1)

            try:
                contador += 1
                driver.find_element(By.XPATH, '//button[@title="Orden de servicio Applet de formulario:Fecha de Atención"]').click()
                cargandoFechaAtencion = False

            except:
                if contador == 360: return 1, 'Error Programacion', numeroOrden

        cargaElementos(driver, '//button[@title="Fecha/Hora de atención Applet de lista:Ok"]')
        cargaElementos(driver, '//input[@aria-label="Fecha Solicitada"]')
        validacion = cargaElementos(driver, '/html/body/div[1]/div/div[5]/div/div[8]/div[1]/div/div[3]/ul/li[1]/span/a')
        return 1, '', numeroOrden

    except Exception as e: 
        print(e)
        return 1, f'Error: {str(e)}', '-'

def generacionCN(driver, tipoOrden):

    try:
        print('-> Generando CN')
        #Creacion CN
        btn_creacion_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Casos de Negocio Applet de lista:Nuevo')
        if btn_creacion_Ajuste == False: return 1, 'Error Pantalla', '-'

        elemento_monto_Ajuste, res = cargandoElemento(driver, 'input', 'aria-label', 'Solución')
        if elemento_monto_Ajuste == False: return 1, 'Error Pantalla', '-'
        print('-> CN Creado')
        sleep(5)

        #Categoria
        textoLabelCategoriaCN = 'Categoria'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelCategoriaCN + "']").click()
        categoriaCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelCategoriaCN + "']")
        categoriaCN.clear()
        categoriaCN.send_keys('OUTBOUND')
        categoriaCN.send_keys(Keys.RETURN)
        sleep(3)

        #Motivo
        textoLabelMotivoCN = 'Motivo'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMotivoCN + "']").click()
        motivoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMotivoCN + "']")
        motivoCN.clear()
        motivoCN.send_keys('SEGUIMIENTOS ESPECIALES')
        motivoCN.send_keys(Keys.RETURN)
        sleep(3)

        #Submotivo
        textoLabelSubMotivoCN = 'Submotivo'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelSubMotivoCN + "']").click()
        subMotivoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelSubMotivoCN + "']")
        subMotivoCN.clear()
        subMotivoCN.send_keys('CALL BACK')
        subMotivoCN.send_keys(Keys.RETURN)
        sleep(3)

        #Solucion
        try:
            textoLabelsolucionCN = 'Solución'
            driver.find_element_by_xpath("//input[@aria-label='" + textoLabelsolucionCN + "']").click()
            solucionCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelsolucionCN + "']")
            solucionCN.clear()
            solucionCN.send_keys('SOLUCION EN LINEA')
            solucionCN.send_keys(Keys.RETURN)
        except Exception:
            alerta = Alert(driver)
            textoAlerta = alerta.text

            if 'Ya existe un Caso de Negocio en proceso con esta tipificacion' in textoAlerta:
                alerta.accept()
                error = 'Error CN previo'
                textoLabelCancelarCN = 'Casos de negocio Applet de formulario:Cancelar'
                driver.find_element_by_xpath("//button[@aria-label='" + textoLabelCancelarCN + "']").click()
                return 1, error,'-'
            else: return 1, f'Error: {textoAlerta}', '-'

        #Comentario
        textoLabelcomentarioCN = 'Comentarios'
        driver.find_element_by_xpath("//textarea[@aria-label='" + textoLabelcomentarioCN + "']").click()
        comentarioCN = driver.find_element_by_xpath("//textarea[@aria-label='" + textoLabelcomentarioCN + "']")
        comentarioCN.clear()
        comentarioCN.send_keys('Call Back Gestión sin contacto')
        sleep(3)

        #Motivo Cliente
        valMotivoCliente = ''
        if 'Cablemodem' in tipoOrden: valMotivoCliente = 'INTERNET'
        elif 'Video' in tipoOrden: valMotivoCliente = 'VIDEO'
        elif 'Telefonia' in tipoOrden: valMotivoCliente = 'TELEFONIA'
        else: return 1, 'Error Tipo Orden Incorrecto', '-'

        textoLabelmotivoClienteCN = 'Motivo Cliente'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoClienteCN + "']").click()
        motivoClienteCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoClienteCN + "']")
        motivoClienteCN.clear()
        motivoClienteCN.send_keys(valMotivoCliente)
        motivoClienteCN.send_keys(Keys.RETURN)

        numeroCN = driver.find_element(By.NAME, 'SRNumber')
        numeroCN = numeroCN.text
        print(numeroCN)
        sleep(3)
        
        #Estado
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]').click()
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span').click()
        sleep(5)
        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: return 1, 'Error Pantalla NO Carga', '-'
        
        sleep(5)
        print('-> CN Cerrado')
        driver.find_element(By.XPATH, "//button[@aria-label='Casos de negocio Applet de formulario:Guardar']").click()
        print('CN Guardado')
        sleep(7)

        return 1, 'Confirmado', numeroCN

    except Exception as e: 
        print(e)
        return 1, f'Error: {str(e)}', '-'