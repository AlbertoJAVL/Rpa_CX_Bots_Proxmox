from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

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
        resultado = cargaElementos(driver, '//button[@title="Casos de Negocio Applet de lista:Nuevo"]')
        if resultado == False: return 1, 'Error Creacion CN', '-'
        print('-> CN Creado')
        cargaElementos(driver, '//input[@aria-label="Categoria"]')
        ingresoInfo(driver, '//input[@aria-label="Categoria"]', 'OUTBOUND', 'Categoria', True)
        ingresoInfo(driver, '//input[@aria-label="Motivo"]', 'SEGUIMIENTOS ESPECIALES', 'Motivo', True)
        ingresoInfo(driver, '//input[@aria-label="Submotivo"]', 'CALL BACK', 'SubMotivo', True)
        ingresoInfo(driver, '//input[@aria-label="Solución"]', 'SOLUCION EN LINEA', 'Solucion', True)
        ingresoInfo(driver, '//textarea[@aria-label="Comentarios"]', 'Call Back Gestión sin contacto', 'Comentarios')

        if 'Cablemodem' in tipoOrden: ingresoInfo(driver, '//input[@aria-label="Motivo Cliente"]', 'INTERNET', 'Motivo Cliente', True)
        elif 'Video' in tipoOrden: ingresoInfo(driver, '//input[@aria-label="Motivo Cliente"]', 'VIDEO', 'Motivo Cliente', True)
        elif 'Telefonia' in tipoOrden: ingresoInfo(driver, '//input[@aria-label="Motivo Cliente"]', 'TELEFONIA', 'Motivo Cliente', True)
        else: return 1, 'Error Tipo Orden Incorrecto', '-'

        numeroCN = driver.find_element(By.NAME, 'SRNumber')
        numeroCN = numeroCN.text
        print(numeroCN)

        cargaElementos(driver, '//input[@aria-labelledby="Status_Label_13"]')
        print('-> Cerrando CN')
        cargaElementos(driver, '//span[@id="s_13_1_12_0_icon"]')
        sleep(1000)
        # busquedaElemento(driver, "Cerrado", '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[{contador}]/div')
        # cargaElementos(driver, '//button[@title="Casos de negocio Applet de formulario:Guardar"]')

        return 1, 'Confirmado', numeroCN

    except Exception as e: 
        print(e)
        return 1, f'Error: {str(e)}', '-'