from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, date, timedelta
from time import sleep
from rutas import *


import  pyautogui  as pg

def cargandoElemento(driver, elemento, atributo, valorAtributo, path = False):

    cargando = True
    contador = 0

    while cargando:

        sleep(1)
        try: 
            
            if path == False: 
                driver.find_element(By.XPATH, f"//{elemento}[@{atributo}='{valorAtributo}']").click()
                return True
            else: 
                print('aqui')
                driver.find_element(By.XPATH, path).click()
                return True
            
        
        except:
            contador += 1
            if contador == 60: return False

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

def busqueda_descripcion(driver):
    
    # Applet Detalles (click)
    driver.find_element(By.XPATH, path_applet_detalles).click()

    buscandoItem = True
    contadorItems = 0

    # Busqueda Cargo
    while buscandoItem:

        try:
            
            contadorItems += 1

            # Descripcion Item (click)
            driver.find_element(By.XPATH, f"//*[@id='{str(contadorItems)}_s_2_l_Comments']").click()
            sleep(2)

            # Valor Item
            nombreCargo = driver.find_element(By.XPATH, f"//*[@id='{str(contadorItems)}_Comments']")
            nombreCargo = nombreCargo.get_attribute("value")

            if 'Cargo por pago tardío' in nombreCargo:
                # Monto Item (click)
                driver.find_element(By.XPATH, f"//*[@id='{str(contadorItems)}_s_2_l_Amount']").click()
                sleep(2)

                # Valor Item
                importe = driver.find_element(By.XPATH, f"//*[@id='{str(contadorItems)}_Amount']")
                importe = importe.get_attribute("value")
                print('♦ Pago Localizado ♦')
                pg.press('up', presses=20)

                # Regreso a Pantalla Unica Consulta
                driver.find_element(By.XPATH, path_regreso_pantalla_uc).click()
                return True, importe
            
        except: 
            if contadorItems >= 12: return False, ''

def busquedaCN(driver, fecha12Meses, fechaHoy, motivo, submotivo, solucion):
    # Lupa Casos de Negocio (Click)
    print(f'→ Validando CN {solucion}')
    driver.find_element(By.XPATH, "//button[@title='Casos de Negocio Applet de lista:Consulta']").click()
    sleep(10)

    # Busqueda Campo Fecha Apertura CN
    fecha_cn = obtencionColumna(driver, 'Fecha de Apertura', path_encabezados_cn)
    driver.find_element(By.XPATH, path_campo_cn.replace('{contador}', fecha_cn)).click()
    input_fecha_cn = driver.find_element(By.XPATH, f"{path_campo_cn.replace('{contador}', fecha_cn)}/input[2]")
    sleep(2)
    input_fecha_cn.send_keys(f">= '{fecha12Meses}' AND <= '{fechaHoy}'")
    print('♦ Rango de Fecha Ingresado ♦')

    # Busqueda Campo Motivo CN 
    motivo_cn = obtencionColumna(driver, 'Motivo', path_encabezados_cn)
    driver.find_element(By.XPATH, path_campo_cn.replace('{contador}', motivo_cn)).click()
    input_motivo_cn = driver.find_element(By.XPATH, f"{path_campo_cn.replace('{contador}', motivo_cn)}/input[2]")
    sleep(2)
    input_motivo_cn.send_keys(motivo)
    if motivo != '': input_motivo_cn.send_keys(Keys.RETURN)

    # Busqueda Campo Sub Motivo CN 
    subMotivo_cn = obtencionColumna(driver, 'Submotivo', path_encabezados_cn)
    driver.find_element(By.XPATH, path_campo_cn.replace('{contador}', subMotivo_cn)).click()
    input_subMotivo_cn = driver.find_element(By.XPATH, f"{path_campo_cn.replace('{contador}', subMotivo_cn)}/input[2]")
    sleep(2)
    input_subMotivo_cn.send_keys(submotivo)
    if submotivo != '': input_subMotivo_cn.send_keys(Keys.RETURN)

    # Busqueda Campo Solucion CN 
    solucion_cn = obtencionColumna(driver, 'Solución', path_encabezados_cn)
    driver.find_element(By.XPATH, path_campo_cn.replace('{contador}', solucion_cn)).click()
    input_solucion_cn = driver.find_element(By.XPATH, f"{path_campo_cn.replace('{contador}', solucion_cn)}/input[2]")
    sleep(2)
    input_solucion_cn.send_keys(solucion)
    input_solucion_cn.send_keys(Keys.RETURN)
    input_solucion_cn.send_keys(Keys.RETURN)

    print('♦ Plantilla CN Ingresada ♦')
    sleep(10)

    try: 
        # CN Reciente (click)
        driver.find_element(By.XPATH, path_resultado_cn).click()
        print('♥ CN Reciente ♥')
        return True
    except: 
        print('♥ Sin CNs Previos ♥')
        return False

def busquedaOS(driver, limiteInferior, limiteSuperior, tipoOS, cuenta):

    # Pantalla Consulta (Click)
    driver.find_element(By.XPATH, "//a[@title='Pantalla Única de Consulta']").click()
    
    # Buscando Elemento
    lupa_busqueda_cuenta = cargandoElemento(driver, 'button', 'title', 'Pantalla Única de Consulta Applet de formulario:Consulta')
    if lupa_busqueda_cuenta == False: return False, 'Error Pantalla NO Carga'
    sleep(5)

    # Ingreso Cuenta
    input_busqueda_cuenta = driver.find_element(By.XPATH, "//input[@aria-label='Numero Cuenta']")
    input_busqueda_cuenta.click()
    sleep(1)
    input_busqueda_cuenta.send_keys(cuenta)
    input_busqueda_cuenta.send_keys(Keys.RETURN)
    print('♦ Cuenta Ingresada ♦')

    # Cargando Cuenta
    lupa_busqueda_cuenta = cargandoElemento(driver, 'span', 'id', 'Saldo_Vencido_Label_12')
    if lupa_busqueda_cuenta == False: return False, 'Error Pantalla NO Carga'
    print('♥ Cuenta OK! ♥')
    sleep(5)

    driver.find_element(By.XPATH, "//button[@aria-label='Ordenes de Servicio Menú List']").click()
    sleep(3)

    pos_opc_nueva_consulta = obtencionColumna(driver, 'Nueva consulta              [Alt+Q]', path_opc_menu)
    driver.find_element(By.XPATH, f'{path_opc_menu.replace("{contador}", pos_opc_nueva_consulta)}/a').click()
    sleep(5)

    fecha_orden = obtencionColumna(driver, 'Fecha de la Orden', path_encabezados_ordenes_servicio)
    driver.find_element(By.XPATH, path_campo_ordenes_servicio.replace('{contador}', fecha_orden)).click()
    input_fecha_os = driver.find_element(By.XPATH, f"{path_campo_ordenes_servicio.replace('{contador}', fecha_orden)}/input[2]")
    sleep(2)
    input_fecha_os.send_keys(f">= '{limiteInferior}' AND <= '{limiteSuperior}'")

    tipo_orden = obtencionColumna(driver, 'Tipo', path_encabezados_ordenes_servicio)
    driver.find_element(By.XPATH, path_campo_ordenes_servicio.replace('{contador}', tipo_orden)).click()
    input_tipo_os = driver.find_element(By.XPATH, f"{path_campo_ordenes_servicio.replace('{contador}', tipo_orden)}/input[2]")
    sleep(2)
    input_tipo_os.send_keys(tipoOS)
    input_tipo_os.send_keys(Keys.RETURN)
    input_tipo_os.send_keys(Keys.RETURN)

    sleep(10)

    try: 
        # OS busqueda (click)
        driver.find_element(By.XPATH, path_resultado_ordenes_servicio).click()
        print('♥ OS Reciente ♥')
        return True
    except: 
        print('♥ Sin OS Previa ♥')
        return False

def obtener_nombre_mes(numero_mes):

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    nombre_mes = meses.get(int(numero_mes))
    if nombre_mes: return nombre_mes
    else: return 'Número de mes invalido'

def obtenerFechasOS(driver):

    fechas = []            
    obteniendoFechas = True
    contador = 1

    while obteniendoFechas:
        
        contador += 1
        try:
            path = path_resultado_ordenes_servicio2.replace('{contador}', str(contador))
            fechaObtenida = driver.find_element(By.XPATH, path)
            fechaObtenida = fechaObtenida.get_attribute("value")

            fechas.append(fechaObtenida[:10])

        except: return fechas

def home(driver): driver.find_element(By.XPATH, "//a[@title='Pantalla Única de Consulta']").click()
def home2(driver): driver.find_element(By.XPATH, "//a[@title='Página inicial']").click()

# Función de apertura para generar validaciones


def validacionSubEstado(driver, os):

    try:

        columna = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'
        columna2 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input[2]'
        columna3 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input'
        
        print('→ Cierre OS')

        # Pantalla Consulta (Click)
        lupa_busqueda_os = cargandoElemento(driver, 'a', 'title', 'Ordenes de Servicio')
        if lupa_busqueda_os == False: return 'Error Pantalla NO Carga'
        # driver.find_element(By.XPATH, "//a[@title='Ordenes de Servicio']").click()
        
        # Buscando Elemento
        print('→ Cargando Pantalla busqueda OS')
        lupa_busqueda_os = cargandoElemento(driver, 'button', 'title', 'Ordenes de servicio Applet de lista:Consulta')
        if lupa_busqueda_os == False: return 'Error Pantalla NO Carga'
        sleep(5)

        # Ingreso OS
        print('→ Obteniendo posicion columna busqueda No Orden')
        posicion = obtencionColumna(driver, 'Nº de orden', columna)
        if posicion == False: return 'Error Pantalla NO Carga'
        sleep(3)

        # driver.find_element(By.XPATH, columna.replace('{contador}', posicion)).click()
        try: input_busqueda_os = driver.find_element(By.XPATH, columna2.replace('{contador}', posicion))
        except: input_busqueda_os = driver.find_element(By.XPATH, columna3.replace('{contador}', posicion))
        input_busqueda_os.send_keys(os)
        input_busqueda_os.send_keys(Keys.RETURN)
        print('→ OS Ingresada OK!')

        print('→ Cargando OS ←')
        sleep(15)

        posicion = obtencionColumna(driver, 'Sub-Estado', columna)
        if posicion == False: return 'Error Pantalla NO Carga'
        sleep(3)
        print('Acceso Sub Estado')

        input_subEstado_os = driver.find_element(By.XPATH, columna2.replace('{contador}', posicion).replace('/input[2]', ''))
        input_subEstado_os = driver.execute_script("return arguments[0].textContent;", input_subEstado_os)
        print(f'Sub-Estado: {input_subEstado_os}')

        if 'ok cliente' in input_subEstado_os: return True
        else: return False


    except Exception as e: 
        print(f'ERROR EN FUNCION INICIO. ERROR: {e}')
        return 'FCierreOS'
    


  
def cierreOS(driver, os):

    try:

        columna = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'
        columna2 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input[2]'
        columna3 = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]/input'

        print('→ Cierre OS')

        # Pantalla Consulta (Click)
        lupa_busqueda_os = cargandoElemento(driver, 'a', 'title', 'Ordenes de Servicio')
        if lupa_busqueda_os == False: return 'Error Pantalla NO Carga'
        # driver.find_element(By.XPATH, "//a[@title='Ordenes de Servicio']").click()
        
        # Buscando Elemento
        print('→ Cargando Pantalla busqueda OS')
        lupa_busqueda_os = cargandoElemento(driver, 'button', 'title', 'Ordenes de servicio Applet de lista:Consulta')
        if lupa_busqueda_os == False: return 'Error Pantalla NO Carga'
        sleep(5)

        # Ingreso OS
        print('→ Obteniendo posicion columna busqueda No Orden')
        posicion = obtencionColumna(driver, 'Nº de orden', columna)
        if posicion == False: return 'Error Pantalla NO Carga'
        sleep(3)

        # driver.find_element(By.XPATH, columna.replace('{contador}', posicion)).click()
        try: input_busqueda_os = driver.find_element(By.XPATH, columna2.replace('{contador}', posicion))
        except: input_busqueda_os = driver.find_element(By.XPATH, columna3.replace('{contador}', posicion))
        input_busqueda_os.send_keys(os)
        input_busqueda_os.send_keys(Keys.RETURN)
        print('→ OS Ingresada OK!')

        print('→ Cargando OS ←')
        cargandoElemento(driver, '', '', '', f'//a[contains(text(), "{os}")]')

        cargandoElemento(driver, 'input', 'aria-label', 'Sub-Estado')
        sleep(3)

        driver.find_element(By.XPATH, "//input[@aria-label='Sub-Estado']").click()
        sleep(2)
        input_subestado = driver.find_element(By.XPATH, "//input[@aria-label='Sub-Estado']")
            
        sleep(2)
        input_subestado.clear()
        sleep(2)
        input_subestado.send_keys("ok cliente")
        input_subestado.send_keys(Keys.RETURN)
        print('♦ Campo Sub Estado ♦')

        driver.find_element(By.XPATH, "//input[@aria-label='Estado']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//button[@aria-label='Orden de servicio Applet de formulario:Guardar']").click()

        resultado = validacionSubEstado(driver, os)
        if resultado == True: pass
        else: cierreOS(driver, os)

        return 'Completado'

    except Exception as e: 
        print(f'ERROR EN FUNCION INICIO. ERROR: {e}')
        return 'Error FCierreOS'
    

def inicio(driver, cuenta, comentario, os):

    try:

        pathEstado = '/html/body/div[1]/div/div[5]/div/div[8]/ul[1]/li[{contador}]/div'

        resultado = validacionSubEstado(driver, os)
        if resultado == True: return 'No aplica: Modificacion OS Previa'

        print('→ Buscando Cuenta')

        # Pantalla Consulta (Click)
        # driver.find_element(By.XPATH, "//a[@title='Pantalla Única de Consulta']").click()
        lupa_busqueda_cuenta = cargandoElemento(driver, 'a', 'title', 'Pantalla Única de Consulta')
        if lupa_busqueda_cuenta == False: return 'Error Pantalla NO Carga'

        # Buscando Elemento
        lupa_busqueda_cuenta = cargandoElemento(driver, 'button', 'title', 'Pantalla Única de Consulta Applet de formulario:Consulta')
        if lupa_busqueda_cuenta == False: return 'Error Pantalla NO Carga'
        sleep(5)

        # Ingreso Cuenta
        input_busqueda_cuenta = driver.find_element(By.XPATH, "//input[@aria-label='Numero Cuenta']")
        input_busqueda_cuenta.click()
        sleep(1)
        input_busqueda_cuenta.send_keys(cuenta)
        input_busqueda_cuenta.send_keys(Keys.RETURN)
        print('♦ Cuenta Ingresada ♦')

        # Cargando Cuenta
        lupa_busqueda_cuenta = cargandoElemento(driver, 'span', 'id', 'Saldo_Vencido_Label_12')
        if lupa_busqueda_cuenta == False: return 'Error Pantalla NO Carga'
        print('♥ Cuenta OK! ♥')
        sleep(5)

        # # Estado Cuenta
        # estado = driver.find_element(By.XPATH, f"//input[@aria-labelledby='AccountStatus_Label_12']")
        # estado = estado.get_attribute("value")
        # print(f'{estado}')

        # if 'Activo' not in estado: return False, 'Error Estado Cuenta'

        # # Sub Estado Cuenta
        # subEstado = driver.find_element(By.XPATH, f"//input[@aria-labelledby='ADL_Status_Label_12']")
        # subEstado = subEstado.get_attribute("value")
        # print(f'{subEstado}')

        # if 'Instalada' not in subEstado: return False, 'Error Sub Estado Cuenta'

        # # Validacion Ajuste Previo ultimos 6 meses
        # fechaHoy = date.today()
        # fecha6Meses = fechaHoy - relativedelta(months=6)

        # fechaHoy = fechaHoy.strftime('%d/%m/%Y')
        # fecha6Meses = fecha6Meses.strftime('%d/%m/%Y')

        # Lupa Ajustes (Click)
        print('→ Validando Ajuste Reciente')
        driver.find_element(By.XPATH, "//button[@title='Casos de Negocio Applet de lista:Nuevo']").click()
        sleep(10)

        # Busqueda Campo Categoria
        driver.find_element(By.XPATH, "//input[@aria-label='Categoria']").click()
        input_categoria = driver.find_element(By.XPATH, "//input[@aria-label='Categoria']")
        sleep(2)
        input_categoria.send_keys("MONITOR")
        input_categoria.send_keys(Keys.RETURN)
        print('♦ Categoria Ingresada ♦')

        # Busqueda Campo Motivo
        driver.find_element(By.XPATH, "//input[@aria-label='Motivo']").click()
        input_motivo = driver.find_element(By.XPATH, "//input[@aria-label='Motivo']")
        sleep(2)
        input_motivo.send_keys("CONFIRMA SERVICIO CORRECTO")
        input_motivo.send_keys(Keys.RETURN)
        print('♦ Motivo Ingresado ♦')

        # Busqueda Campo Submotivo
        driver.find_element(By.XPATH, "//input[@aria-label='Submotivo']").click()
        input_submotivo = driver.find_element(By.XPATH, "//input[@aria-label='Submotivo']")
        sleep(2)
        input_submotivo.send_keys("LLAMADA DE SERVICIO ACTIVO")
        input_submotivo.send_keys(Keys.RETURN)
        print('♦ Submotivo Ingresado ♦')

        # Busqueda Campo Solucion
        driver.find_element(By.XPATH, "//input[@aria-label='Solución']").click()
        input_solucion = driver.find_element(By.XPATH, "//input[@aria-label='Solución']")
        sleep(2)
        input_solucion.send_keys("REGISTRO DE LLAMADA")
        input_solucion.send_keys(Keys.RETURN)
        print('♦ Solución Ingresada ♦')
        
        sleep(5)
        
        try:
            alert = Alert(driver)
            alert_txt = alert.text
            print(f'♦ {alert_txt} ♦')
            alert.accept()
            return 'Error CN Previo'
        except: pass

        # Busqueda Campo Comentario
        driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']").click()
        input_comentario = driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']")
        sleep(2)
        input_comentario.send_keys(comentario)
        print('♦ Comentario Ingresado ♦')

        noCN = driver.find_element(By.XPATH, f'//a[@name="SRNumber"]')
        noCN = noCN.text
        print(f'♦ CN Generado: {noCN} ♦')

        driver.find_element(By.XPATH, f'//a[contains(text(), "{noCN}")]').click()
        print(f'♦ Acceso al CN: {noCN} OK!♦')

        print('→ Cargando Pantalla CN ←')
        cargandoElemento(driver, 'input', 'aria-label', 'Motivo del cierre')

        # Busqueda Campo Motivo Cierre
        driver.find_element(By.XPATH, "//input[@aria-label='Motivo del cierre']").click()
        input_motivo_cierre = driver.find_element(By.XPATH, "//input[@aria-label='Motivo del cierre']")
        sleep(2)
        input_motivo_cierre.send_keys("CIERRE ADMINISTRATIVO")
        print('♦ Campo Motivo Cierre ♦')

        # Busqueda Campo Orden Servicio Asociada
        driver.find_element(By.XPATH, "//input[@aria-label='Orden de servicio asociada']").click()
        input_orden_servicio_asociada = driver.find_element(By.XPATH, "//input[@aria-label='Orden de servicio asociada']")
        sleep(2)
        input_orden_servicio_asociada.send_keys(os)
        print('♦ Campo Orden Servicio Asociada ♦')

        # Formulario Dinamico
        driver.find_element(By.XPATH, '//div[contains(text(), "Formulario dinámico")]').click()
        print(f'♦ Acceso a Formulario Dinamico OK!♦')

        for posicion in range(1,4):
            driver.find_element(By.XPATH, f'//*[@id="{str(posicion)}_s_2_l_TT_Tipo_LOV"]').click()
            input_pregunta_dinamica = driver.find_element(By.XPATH, '//input[@name="TT_Tipo_LOV"]')
            sleep(2)
            input_pregunta_dinamica.send_keys("SI")
            input_pregunta_dinamica.send_keys(Keys.RETURN)

        sleep(15)
        # Busqueda Campo Estado
        driver.find_element(By.XPATH, "//input[@aria-label='Estado']").click()
        # sleep(10000)
        sleep(5)
        driver.find_element(By.XPATH, "//span[@id='s_1_1_143_0_icon']").click()
        sleep(5)
        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: 
            pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[{contador}]/div'
            posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
            if posicion == False: return 'Error Pantalla NO Carga'
        driver.find_element(By.XPATH, pathEstado.replace('{contador}', posicion)).click()

        sleep(3)
        driver.find_element(By.XPATH, "//button[@aria-label='Caso de negocio Applet de formulario:Guardar']").click()
        # sleep(1000)
        print('♦ Campo Estado ♦')

        return noCN

    except Exception as e: 
        print(f'ERROR EN FUNCION INICIO. ERROR: {e}')
        return 'Error FInicio'
  