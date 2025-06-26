#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
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



def ingresoDatosAuto(driver, label, dato, tElemento, tEtiqueta,final):
    
    driver.find_element(By.XPATH, f"//{tElemento}[@{tEtiqueta}='" + label + "']").click()
    elemento = driver.find_element(By.XPATH, f"//{tElemento}[@{tEtiqueta}='" + label + "']")
    elemento.clear()
    elemento.send_keys(dato)
    elemento.send_keys(Keys.RETURN)

    if final == True:
        elemento.send_keys(Keys.RETURN)
# busquedaCNTipificado(driver, "SE CANALIZA BO SUCURSALES", "SUC AJUSTE FACTURACION", "SUC ACLARACION-EDO DE CTA", motivoCliente)
def busquedaCNTipificado(driver, estado, solucion, subMotivo, motivo, motivoCliente):
    
    #Lupa
    obtencionValorClick(driver,'Click','Casos de Negocio Applet de lista:Consulta', 'button', 'aria-label')
    sleep(3)

    obtencionValorClick(driver,'Click','s_1_l_altCombo', 'td', 'aria-labelledby')
    sleep(1)

    if estado == " ":
        pass
    else:
        ingresoDatosAuto(driver, 's_1_l_Status s_1_l_altCombo', estado, 'input', 'aria-labelledby', False)
        sleep(1)

    obtencionValorClick(driver,'Click','Motivo', 'td', 'aria-roledescription')
    sleep(1)
    
    #Motivo
    ingresoDatosAuto(driver, 's_1_l_CV_Area s_1_l_altCombo', motivo, 'input', 'aria-labelledby', False)
    sleep(1)

    obtencionValorClick(driver,'Click','Submotivo', 'td', 'aria-roledescription')
    sleep(1)
    
    #SubMotivo
    ingresoDatosAuto(driver, 's_1_l_CV_Sub-Area s_1_l_altCombo', subMotivo, 'input', 'aria-labelledby', False)
    sleep(1)

    obtencionValorClick(driver,'Click','Solución', 'td', 'aria-roledescription')
    sleep(1)

    #Solucion
    ingresoDatosAuto(driver, 's_1_l_Retention_Tools s_1_l_altCombo', solucion, 'input', 'aria-labelledby', False)
    sleep(1)

    obtencionValorClick(driver,'Click','Motivo Cliente', 'td', 'aria-roledescription')
    sleep(1)

    #MotivoCliente
    ingresoDatosAuto(driver, 's_1_l_TT_Motivo_Cliente s_1_l_altCombo', motivoCliente, 'input', 'aria-labelledby', True)
    sleep(8)

    try:
        
        obtencionValorClick(driver,'Click','Motivo Cliente', 'td', 'aria-roledescription')
        sleep(1)
        return True
    except Exception:
        return False

def busquedaAjustePrevio(driver, motivoAjuste):
    
    #Lupa Ajustes
    obtencionValorClick(driver, 'Click', 'Solicitudes de Ajuste Applet de lista:Consulta', 'button', 'aria-label')
    sleep(3)

    driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]').click()
    estado = driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]/input')
    estado.clear()
    estado.send_keys('Aplicado')
    estado.send_keys(Keys.RETURN)
    sleep(1) 

    obtencionValorClick(driver,'Click','Motivo del ajuste', 'td', 'aria-roledescription')
    sleep(1)
    
    ingresoDatosAuto(driver, 's_5_l_Reason_For_Request s_5_l_altCombo', motivoAjuste, 'input', 'aria-labelledby', False)
    sleep(1)

    fecha12Meses = date.today()
    fecha12Meses = fecha12Meses - timedelta(days=365)
    fecha12Meses = f"> '{fecha12Meses.strftime('%d/%m/%Y')}'"
    obtencionValorClick(driver,'Click','Fecha del ajuste', 'td', 'aria-roledescription')
    sleep(1)

    ingresoDatosAuto(driver, 's_5_l_Request_Date s_5_l_altDateTimeZone', fecha12Meses, 'input', 'aria-labelledby', True)
    sleep(1)

    
    sleep(8)

    try:
        obtencionValorClick(driver,'Click','Motivo del ajuste', 'td', 'aria-roledescription')
        sleep(1)
        return True
    except Exception:
        return False


def buscandoOpcEngrane(driver, xpathOpc, busqueda):
    contador = 0
    buscandoCol = True

    while buscandoCol == True:
        try:
            contador += 1
            xpathF = xpathOpc.replace('{contador}', str(contador))
            nameOpc = driver.find_element(By.XPATH,  xpathF)
            opc = nameOpc.text
            print(opc)

            if busqueda in opc:
                xpathF = xpathOpc.replace('{contador}', str(contador))
                driver.find_element(By.XPATH,  xpathF).click()
                return True

        except Exception as e:
            print('buscando...')
            if contador == 20:
                error = 'Error Buscando Opcion'
                print(error)
                buscandoCol = False
                return error

def prueba(driver, no_cuenta):
    wait = WebDriverWait(driver, 120)
    act = webdriver.ActionChains(driver)
    text_box('AJSUTE POR CONVENIO COBRANZA', '▬')
    status_pantalla_unica = pantalla_unica_consulta(driver, no_cuenta) 
    if status_pantalla_unica == False:
        text_box('Cuenta no valida', '▬')
        return False ,'Error Cuenta no valida',''

    obtencionValorClick(driver,'Click','Casos de Negocio Applet de lista:Consulta', 'button', 'aria-label')
    sleep(3)
    
    contador = 0
    buscandoColumna = True

    while buscandoColumna == True:
        try:
            contador += 1
            xpath = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'
            xpathF = xpath.replace('{contador}', str(contador))
            valor = driver.find_element(By.XPATH, xpathF)
            contenido = driver.execute_script("return arguments[0].textContent;", valor)
            
            if 'Motivo Cliente' in contenido:
                xpathClick = '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]'
                xpathF = xpathClick.replace('{contador}', str(contador))
                valor = driver.find_element(By.XPATH, xpathF).click()
            print(contenido)
            sleep(2)
        except:
            print('Buscando...')

def buscandoColumna(driver, xpath, colBuscada):
    contador = 0
    buscandoCol = True

    while buscandoCol == True:
        try:
            contador += 1
            xpathCol = xpath.replace('{contador}', str(contador))
            nameColumna = driver.find_element(By.XPATH,  xpathCol)
            columna = driver.execute_script("return arguments[0].textContent;", nameColumna)

            if colBuscada in columna:
                buscandoCol = False
                print(columna)
                return str(contador)

        except Exception as e:
            print('buscando...')
            if contador == 1000:
                error = 'Error Buscando Columna'
                print(error)
                buscandoCol = False
                return error



def obtencionValorClick(driver,accion,label, tElemento, tEtiqueta):
    
    if accion == True:
        
        elemento = driver.find_element(By.XPATH, f"//{tElemento}[@{tEtiqueta}='" + label + "']")
        elemento = elemento.get_attribute("value")
        return elemento

    else:

        driver.find_element(By.XPATH, f"//{tElemento}[@{tEtiqueta}='" + label + "']").click()







def validacion_cuenta_retencion(driver, no_cuenta, cn):
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
        status_pantalla_unica = pantalla_unica_consulta(driver, no_cuenta) 
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '▬')
            return False ,'Error Cuenta no valida',''
        
        print('▬ Inician proceso BOT ▬')


        # Busqueda CN Tipificado

        print('▬ Validacion CN Tipificado Retencion')

        driver.find_element(By.XPATH, "//button[@aria-label='Casos de Negocio Applet de lista:Consulta']").click()
        sleep(3)

        columna = buscandoColumna(driver, casos_negocio['columnas'], 'Estado')
        xpath = casos_negocio['filas'].replace('{contador}', columna)
        driver.find_element(By.XPATH, xpath).click()
        sleep(2)

        columna = buscandoColumna(driver, casos_negocio['columnas'], 'Caso de Negocio')
        xpath = casos_negocio['filas'].replace('{contador}', columna)
        driver.find_element(By.XPATH, xpath).click()
        casoNegocio = driver.find_element(By.XPATH, xpath + '/input')
        casoNegocio.send_keys(cn)
        casoNegocio.send_keys(Keys.RETURN)
        sleep(5)

        columna = buscandoColumna(driver, casos_negocio['columnas'], 'Comentarios')
        xpath = casos_negocio['filas'].replace('{contador}', columna)

        try: driver.find_element(By.XPATH, xpath).click()
        except:
            error = 'Error Sin CN Ret'
            print('<<<<<<<<<<<<<<<<<<<<<<<' + error + ">>>>>>>>>>>>>>>>>>")
            return False, error,''

        comentario = driver.find_element(By.XPATH, xpath + '/textarea')
        # comentario = driver.execute_script("return arguments[0].textContent;", comentario)
        comentario = comentario.get_attribute("value")
        print('##################')
        print(comentario)
        print('##################')
        comentario = comentario.replace("\n", "")
        
        comentario = unidecode(comentario)
        comentario = comentario.replace('á', 'a')
        comentario = comentario.replace('é', 'e')
        comentario = comentario.replace('í', 'i')
        comentario = comentario.replace('ó', 'o')
        comentario = comentario.replace('ú', 'u')

        patron_promocion = r"Tipo promocion(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Gestionable|Promocion|Tipo gestion|Tipo promesa|Nombre asesor|Fecha pago|Saldo ajustar|Cantidad a pagar|$))"
        resultado_promocion = re.search(patron_promocion, comentario)
        if resultado_promocion:
            promocion = resultado_promocion.group(1)
            promocion = promocion.replace(":", "")
        else:
            patron_promocion = r"Tipo de promocion(.+?)(?=(?:Numero cuenta|Nombre|Estatus cuenta|Numero telefonico|Gestionable|Promocion|Tipo gestion|Tipo promesa|Nombre asesor|Fecha pago|Saldo ajustar|Cantidad a pagar|$))"
            resultado_promocion = re.search(patron_promocion, comentario)
            if resultado_promocion:
                promocion = resultado_promocion.group(1)
                promocion = promocion.replace(":", "")
            else:
                error = 'Error Formato Plantilla'
                print(error)
                return False, error, ''

        if 'VIX' not in promocion:
            error = 'Error Sin Promocion'
            print(error)
            return False, error, ''
        else:
            print('<<<<<<<<<< Promocion Correcta >>>>>>>>>>')

        
        print('▬ Accediendo a Orden de Servicio')
        driver.find_element(By.XPATH, "//button[@aria-label='Ordenes de Servicio Menú List']").click()
        sleep(5)
        opc = buscandoColumna(driver, ordenes_servicio['opcEngrane'], 'Nueva consulta              [Alt+Q]')
        xpath = ordenes_servicio['opcEngrane'].replace('{contador}', opc)
        driver.find_element(By.XPATH, xpath).click()
        sleep(3)
        columna = buscandoColumna(driver, ordenes_servicio['columnas'], 'Estado')
        xpath = ordenes_servicio['filas'].replace('{contador}', columna)
        driver.find_element(By.XPATH, xpath).click()
        estado = driver.find_element(By.XPATH, xpath + '/input')
        estado.send_keys('"Completa"')
        estado.send_keys(Keys.RETURN)
        sleep(6)

        # driver.find_element(By.XPATH, "//button[@aria-label='Ordenes de Servicio Menú List']").click()
        # sleep(5)
        # opc = buscandoColumna(driver, ordenes_servicio['opcEngrane'], 'Ordenar - Avanzado   [Ctrl+Mayús+O]')
        # xpath = ordenes_servicio['opcEngrane'].replace('{contador}', opc)
        # driver.find_element(By.XPATH, xpath).click()
        # sleep(6)

        # driver.find_element(By.XPATH, "//input[@aria-label='Campo 1']").click()
        # fechaOrdenamiento = driver.find_element(By.XPATH, "//input[@aria-label='Campo 1']")
        # fechaOrdenamiento.clear()
        # fechaOrdenamiento.send_keys('Fecha de la Orden')
        # sleep(2)
        # driver.find_element(By.XPATH, "//input[@aria-labelledby='rdbDesc1_Label_14 s_14_1_38_0_Descendente']").click()
        # sleep(2)
        # driver.find_element(By.XPATH, "//button[@aria-label='Orden de clasificación Applet de formulario:Aceptar']").click()
        # sleep(10)

        driver.find_element(By.XPATH, "//div[@un='Fecha de la Orden']").click()
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/ul/li[2]/a").click()
        sleep(5)
        driver.find_element(By.XPATH, ordenes_servicio['ordenServicio']).click()
        sleep(15)

        try:

            item = driver.find_element(By.XPATH,  itemProductos['items'])
            item = driver.execute_script("return arguments[0].textContent;", item)
            driver.find_element(By.XPATH, itemProductos['regresoPantallaUnica']).click()
        
        except:
            print('Buscando portafgolio segunda orden')
            driver.find_element(By.XPATH, itemProductos['regresoPantallaUnica']).click()
            sleep(20)
            driver.find_element(By.XPATH, ordenes_servicio['ordenServicio2']).click()
            sleep(15)
        
            try:

                item = driver.find_element(By.XPATH,  itemProductos['items'])
                item = driver.execute_script("return arguments[0].textContent;", item)
                driver.find_element(By.XPATH, itemProductos['regresoPantallaUnica']).click()
            
            except:
                error = 'No Aplica Sin Portafolio'
                print(f'<<<<<<<<<< {error} >>>>>>>>>>>>>>>')
                return False, error, ''

        print('###############')
        print('PORTAFOLIO: ', item)
        print('###############')
        print('<<<<<<<<< VALIDACIONES EXITOSAS >>>>>>>>>>>>')
        return True, '', item
    except Exception:
        error = 'Error Validaciones'
        print(error)
        return False, error, ''

def terminoPromocion(driver, tipoPortafolio):

    sleep(2)
    print('▬ Asignacion de Paquete VIX')

    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            driver.find_element(By.XPATH, "//button[@aria-label='Pantalla Única de Consulta Applet de formulario:Resumen de la Cuenta']").click()
            cambiandoPantalla = False
            sleep(5)
        except:
            sleep(5)
            contador += 1
            if contador == 10:
                error = 'Error Cargar Cuenta'
                print(error)
                return False, error,'',''


    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            driver.find_element(By.XPATH, "//button[@aria-label='Ítems de facturación Applet de lista:Consulta']").click()
            cambiandoPantalla = False
            sleep(7)

        except:
            sleep(5)
            contador += 1
            if contador == 10:
                error = 'Error Cargar Cuenta'
                print(error)
                return False, error,'',''

    opc = buscandoColumna(driver, ordenes_servicio['columnasProductos'], 'Nº Serie Equipo Serv.')
    xpath = ordenes_servicio['filasProductos'].replace('{contador}', opc)
    driver.find_element(By.XPATH, xpath).click()

    opc = buscandoColumna(driver, ordenes_servicio['columnasProductos'], 'Producto')
    xpath = ordenes_servicio['filasProductos'].replace('{contador}', opc)
    driver.find_element(By.XPATH, xpath).click()
    producto = driver.find_element(By.XPATH, xpath + '/input')
    if 'MODULAR' in tipoPortafolio.upper():
        producto.send_keys('ViX Premium M')
    else:
        producto.send_keys('ViX Premium lealtad promo')
    producto.send_keys(Keys.RETURN)

    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            contador += 1
            driver.find_element(By.XPATH, xpath).click()
            cambiandoPantalla = False
            error = 'No Aplica Complemento Ya Activo'
            print(error)
            return False, error,'',''

        except:
            sleep(5)
            if contador == 5:
                cambiandoPantalla = False
                print('Sin producto pre cargado')
    
    driver.find_element(By.XPATH, "//button[@aria-label='Ítems de facturación Applet de lista:Consulta']").click()
    sleep(7)
    opc = buscandoColumna(driver, ordenes_servicio['columnasProductos'], 'Nº Serie Equipo Serv.')
    xpath = ordenes_servicio['filasProductos'].replace('{contador}', opc)
    driver.find_element(By.XPATH, xpath).click()

    opc = buscandoColumna(driver, ordenes_servicio['columnasProductos'], 'Producto')
    xpath = ordenes_servicio['filasProductos'].replace('{contador}', opc)
    driver.find_element(By.XPATH, xpath).click()
    producto = driver.find_element(By.XPATH, xpath + '/input')
    producto.send_keys('')
    producto.send_keys(Keys.RETURN)
    
    driver.find_element(By.XPATH, "//button[@aria-label='Ítems de facturación Applet de lista:Modificar']").click()
    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            driver.find_element(By.XPATH, "//a[@un='OTT']").click()
            sleep(10)
            cambiandoPantalla = False
        except:
            sleep(5)
            contador += 1
            if contador == 10:
                error = 'Error Cargar OTT'
                print(error)
                return False, error,'',''

    try:
        driver.find_element(By.XPATH, "//input[@value='ViX Premium M']").click()
    except:
        try:
            driver.find_element(By.XPATH, "//input[@value='ViX Premium lealtad promo']").click()
        except:
    
            if 'MODULAR' in tipoPortafolio.upper():
                driver.find_element(By.XPATH, "//input[@un='OTT_OTT modular_Quantity']").click()
                sleep(7)
                driver.find_element(By.XPATH, "//input[@value='ViX Premium M']").click()
            else:
                driver.find_element(By.XPATH, "//input[@un='OTT_OTT wow_Quantity']").click()
                sleep(7)
                driver.find_element(By.XPATH, "//input[@value='ViX Premium lealtad promo']").click()

    sleep(5)

    driver.find_element(By.XPATH, "//button[@un='Terminado']").click()

    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']").click()
            comentarios = driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']")
            comentarios.send_keys('Alta de complemento por convenio de cobranza')
            sleep(5)
            cambiandoPantalla = False
        except:
            sleep(5)
            contador += 1
            if contador == 10:
                error = 'Error Llenado OS'
                print(error)
                return False, error,'',''
    
    driver.find_element(By.XPATH, "//input[@aria-label='No. VTS']").click()
    noVTS = driver.find_element(By.XPATH, "//input[@aria-label='No. VTS']")
    noVTS.send_keys('A001')
    sleep(5)

    driver.find_element(By.XPATH, "//input[@aria-label='Vendedor']").click()
    vendedor = driver.find_element(By.XPATH, "//input[@aria-label='Vendedor']")
    vendedor.send_keys('CVVENSINCOMISION')
    sleep(5)
    
    driver.find_element(By.XPATH, "//input[@aria-label='Clave del Tecnico Principal']").click()
    claveTecnico = driver.find_element(By.XPATH, "//input[@aria-label='Clave del Tecnico Principal']")
    claveTecnico.send_keys('CVVENSINCOMISION')
    sleep(5)

    driver.find_element(By.XPATH, "//input[@aria-label='Motivo de la orden']").click()
    motivoOrden = driver.find_element(By.XPATH, "//input[@aria-label='Motivo de la orden']")
    motivoOrden.send_keys('Video')
    motivoOrden.send_keys(Keys.RETURN)
    sleep(5)

    driver.find_element(By.XPATH, "//input[@aria-label='Referido']").click()
    sleep(3)
    driver.find_element(By.XPATH, ordenes_servicio['referido']).click()
    sleep(10)
    driver.find_element(By.XPATH, "//li[@data-licval='Call Center']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']").click()
    sleep(6)
    driver.find_element(By.XPATH, "//button[@aria-label='Orden de servicio Applet de formulario:Programar']").click()
    sleep(100)

    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']").click()
            sleep(5)
            cambiandoPantalla = False
        except:
            sleep(5)
            contador += 1
            if contador == 10:
                error = 'Error Llenado OS'
                print(error)
                
                estado = driver.find_element(By.XPATH, "//input[@aria-label='Estado']")
                estado = driver.execute_script("return arguments[0].textContent;", estado)

                os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                os = driver.execute_script("return arguments[0].textContent;", os)
                return False, error, estado, os
    
    validandoItemsProgra = True
    contador = 1
    totalItems = 0

    modular = ['Promocion 1 mes sin costo ViX Premium V 11', 'Promocion ViX Premium de por vida RX ladrillos V 1']
    normal = ['Promocion Vix 50-12 meses wiw I+T V 3', 'Promocion ViX Premium de por vida RX wow V 2']
    

    while validandoItemsProgra == True:
        try:
            xpath = ordenes_servicio['portafolios'].replace('{contador}', str(contador))
            itemProgra = driver.find_element(By.XPATH, xpath)
            item = driver.execute_script("return arguments[0].textContent;", itemProgra)


            if 'MODULAR' in tipoPortafolio.upper():

                if 'Promocion ViX Premium de por vida RX ladrillos' in item:

                    xpath = ordenes_servicio['precios'].replace('{contador}', str(contador))
                    itemProgra = driver.find_element(By.XPATH, xpath)
                    itemPrecio = driver.execute_script("return arguments[0].textContent;", itemProgra)

                    if '-' in itemPrecio[0]:
                        validandoItemsProgra = False
                        print('############# Programacion Exitosa ############')
                        sleep(10)
                    else:
                        validandoItemsProgra = False
                        error = 'No Aplica por precio nuevo'
                        print(error)

                        os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                        os = driver.execute_script("return arguments[0].textContent;", os)
                        
                        driver.find_element(By.XPATH, "//input[@aria-label='Motivo de Cancelacion']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuMotivosCancelacion']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['motivosCancelacion'], 'Orden mal generada')
                        driver.find_element(By.XPATH, ordenes_servicio['motivosCancelacion'].replace('{contador}', opc)).click()
                        sleep(4)

                        driver.find_element(By.XPATH, "//input[@aria-label='Estado']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuEstatus']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['estados'], 'Cancelado')
                        driver.find_element(By.XPATH, ordenes_servicio['estados'].replace('{contador}', opc)).click()
                        sleep(7)

                        driver.find_element(By.XPATH, "//button[@aria-label='Orden de servicio Applet de formulario:Guardar']").click()
                        sleep(10)

                        
                        return False, error, 'Cancelado', os

                else:
                    contador += 1
                    if contador == 50:
                        validandoItemsProgra = False
                        error = 'No Aplica por producto nuevo'
                        print(error)
                        
                        os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                        os = driver.execute_script("return arguments[0].textContent;", os)
                        
                        driver.find_element(By.XPATH, "//input[@aria-label='Motivo de Cancelacion']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuMotivosCancelacion']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['motivosCancelacion'], 'Orden mal generada')
                        driver.find_element(By.XPATH, ordenes_servicio['motivosCancelacion'].replace('{contador}', opc)).click()
                        sleep(4)

                        driver.find_element(By.XPATH, "//input[@aria-label='Estado']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuEstatus']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['estados'], 'Cancelado')
                        driver.find_element(By.XPATH, ordenes_servicio['estados'].replace('{contador}', opc)).click()
                        sleep(7)

                        driver.find_element(By.XPATH, "//button[@aria-label='Orden de servicio Applet de formulario:Guardar']").click()
                        sleep(10)

                        return False, error, 'Cancelado', os

            else:


                if 'Promocion ViX Premium de por vida RX' in item:

                    xpath = ordenes_servicio['precios'].replace('{contador}', str(contador))
                    itemProgra = driver.find_element(By.XPATH, xpath)
                    itemPrecio = driver.execute_script("return arguments[0].textContent;", itemProgra)

                    if '-' in itemPrecio[0]:
                        validandoItemsProgra = False
                        print('############# Programacion Exitosa ############')
                        sleep(10)
                    else:
                        validandoItemsProgra = False
                        error = 'No Aplica por precio nuevo'
                        print(error)
                        
                        os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                        os = driver.execute_script("return arguments[0].textContent;", os)
                        
                        driver.find_element(By.XPATH, "//input[@aria-label='Motivo de Cancelacion']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuMotivosCancelacion']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['motivosCancelacion'], 'Orden mal generada')
                        driver.find_element(By.XPATH, ordenes_servicio['motivosCancelacion'].replace('{contador}', opc)).click()
                        sleep(4)

                        driver.find_element(By.XPATH, "//input[@aria-label='Estado']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuEstatus']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['estados'], 'Cancelado')
                        driver.find_element(By.XPATH, ordenes_servicio['estados'].replace('{contador}', opc)).click()
                        sleep(7)

                        driver.find_element(By.XPATH, "//button[@aria-label='Orden de servicio Applet de formulario:Guardar']").click()
                        sleep(10)
                        
                        return False, error, 'Cancelado', os

                else:
                    contador += 1
                    if contador == 50:
                        validandoItemsProgra = False
                        error = 'No Aplica por producto nuevo'
                        print(error)
                        
                        os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                        os = driver.execute_script("return arguments[0].textContent;", os)
                        
                        driver.find_element(By.XPATH, "//input[@aria-label='Motivo de Cancelacion']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuMotivosCancelacion']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['motivosCancelacion'], 'Orden mal generada')
                        driver.find_element(By.XPATH, ordenes_servicio['motivosCancelacion'].replace('{contador}', opc)).click()
                        sleep(4)

                        driver.find_element(By.XPATH, "//input[@aria-label='Estado']").click()
                        sleep(2)
                        driver.find_element(By.XPATH, ordenes_servicio['menuEstatus']).click()
                        sleep(7)
                        opc = buscandoColumna(driver, ordenes_servicio['estados'], 'Cancelado')
                        driver.find_element(By.XPATH, ordenes_servicio['estados'].replace('{contador}', opc)).click()
                        sleep(7)

                        driver.find_element(By.XPATH, "//button[@aria-label='Orden de servicio Applet de formulario:Guardar']").click()
                        sleep(10)
                        
                        return False, error, 'Cancelado', os
        except:
            contador += 1
            if contador == 50:
                validandoItemsProgra = False
                error = 'No Aplica por producto nuevo'
                print(error)

                # estado = driver.find_element(By.XPATH, "//input[@aria-label='Estado']")
                # estado = driver.execute_script("return arguments[0].textContent;", estado)

                # os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                # os = driver.execute_script("return arguments[0].textContent;", os)
                return False, error, '',''

    driver.find_element(By.XPATH, "//button[@aria-label='Enviar']").click()

    sleep(200)

    cambiandoPantalla = True
    contador = 0

    while cambiandoPantalla == True:
        try: 
            driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']").click()
            sleep(5)
            cambiandoPantalla = False
            estado = driver.find_element(By.XPATH, "//input[@aria-label='Estado']")
            estado = driver.execute_script("return arguments[0].textContent;", estado)

            os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
            os = driver.execute_script("return arguments[0].textContent;", os)
            print('################## ENvío Exitoso ####################')
            return True, '', estado, os
        except:
            sleep(5)
            contador += 1
            if contador == 10:
                error = 'Error Llenado OS'
                print(error)

                estado = driver.find_element(By.XPATH, "//input[@aria-label='Estado']")
                estado = driver.execute_script("return arguments[0].textContent;", estado)

                os = driver.find_element(By.XPATH, "//input[@aria-label='Número']")
                os = driver.execute_script("return arguments[0].textContent;", os)
                return False, error, estado, os
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
    
    
def cierreActividad(driver, no_cuenta):

    try:
        wait = WebDriverWait(driver, 120)
        act = webdriver.ActionChains(driver)
        status_pantalla_unica = pantalla_unica_consulta(driver, no_cuenta) 
        if status_pantalla_unica == False:
            text_box('Cuenta no valida', '▬')
            return False ,'Error Cuenta no valida',''
        
        print('▬ Inician proceso BOT Generacion CN ▬')
        sleep(12)

        driver.find_element(By.XPATH, "//button[@aria-label='Casos de Negocio Applet de lista:Nuevo']").click()
        sleep(5)

        driver.find_element(By.XPATH, "//input[@aria-label='Categoria']").click()
        categoria = driver.find_element(By.XPATH, "//input[@aria-label='Categoria']")
        categoria.send_keys('SERVICIOS')
        categoria.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH, "//input[@aria-label='Motivo']").click()
        motivo = driver.find_element(By.XPATH, "//input[@aria-label='Motivo']")
        motivo.send_keys('MOD AL CONTRATO')
        motivo.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH, "//input[@aria-label='Submotivo']").click()
        subMotivo = driver.find_element(By.XPATH, "//input[@aria-label='Submotivo']")
        subMotivo.send_keys('COMPLEMENTO DE VIDEO')
        subMotivo.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH, "//input[@aria-label='Solución']").click()
        solucion = driver.find_element(By.XPATH, "//input[@aria-label='Solución']")
        solucion.send_keys('UPGRADE')
        solucion.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']").click()
        comentario = driver.find_element(By.XPATH, "//textarea[@aria-label='Comentarios']")
        comentario.send_keys('Alta de complemento por convenio de cobranza')

    
        cnGenerado = driver.find_element(By.XPATH, "//a[@un='Caso de Negocio']")
        cnGenerado = driver.execute_script("return arguments[0].textContent;", cnGenerado)

        driver.find_element(By.XPATH, "//input[@aria-label='Motivo del Cierre']").click()
        motivoCierre = driver.find_element(By.XPATH, "//input[@aria-label='Motivo del Cierre']")
        motivoCierre.send_keys('RAC INFORMA Y SOLUCIONA')
        motivoCierre.send_keys(Keys.RETURN)
        sleep(5)

        driver.find_element(By.XPATH, "//input[@aria-label='Motivo Cliente']").click()
        sleep(1)
        driver.find_element(By.XPATH, casos_negocio['motivoCliente']).click()
        sleep(1)
        opc = buscandoColumna(driver, casos_negocio['opcionesMC'], 'VIX+')
        xpath = casos_negocio['opcionesMC'].replace('{contador}', opc)
        driver.find_element(By.XPATH, xpath).click()


        # driver.find_element(By.XPATH, "//input[@aria-label='Motivo del Cierre']").click()
        # sleep(1)
        # driver.find_element(By.XPATH, casos_negocio['motivoCliente']).click()
        # sleep(1)
        # opc = buscandoColumna(driver, casos_negocio['opcionesMC'], 'RAC INFORMA Y SOLUCIONA')
        # xpath = casos_negocio['opcionesMC'].replace('{contador}', opc)
        # driver.find_element(By.XPATH, xpath).click()
        sleep(10)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]').click()
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span').click()
        sleep(5)
        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: 
            pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[{contador}]/div'
            posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
            if posicion == False:: return False, 'Error Pantalla NO Carga', '-'
        driver.find_element(By.XPATH, pathEstadoCNOpc.replace('{contador}', posicion)).click()
        sleep(5)
        driver.find_element(By.XPATH, "//button[@aria-label='Casos de negocio Applet de formulario:Guardar']").click()
        sleep(5)

        print('<<<<<<<<<<<<<<< CN Completado con Exito >>>>>>>>>>>>>>>>>>')
        return True,'', cnGenerado

    except Exception as e:
        print(e)
        error = 'Error Creacion CN'
        print(error)
        return False, error,''


        # Busqueda CN Tipificado
    
    print('▬ Profundizando CN')

    driver.find_element(By.XPATH, "//button[@aria-label='Casos de Negocio Applet de lista:Consulta']").click()
    sleep(3)

    columna = buscandoColumna(driver, casos_negocio['columnas'], 'Estado')
    xpath = casos_negocio['filas'].replace('{contador}', columna)
    driver.find_element(By.XPATH, xpath).click()
    estado = driver.find_element(By.XPATH, xpath + '/input')
    estado.send_keys("Abierto") 

    columna = buscandoColumna(driver, casos_negocio['columnas'], 'Motivo')
    xpath = casos_negocio['filas'].replace('{contador}', columna)
    driver.find_element(By.XPATH, xpath).click()
    motivo = driver.find_element(By.XPATH, xpath + '/input')
    motivo.send_keys("SUC ACLARACION-EDO DE CTA")

    columna = buscandoColumna(driver, casos_negocio['columnas'], 'Submotivo')
    xpath = casos_negocio['filas'].replace('{contador}', columna)
    driver.find_element(By.XPATH, xpath).click()
    submotivo = driver.find_element(By.XPATH, xpath + '/input')
    submotivo.send_keys("SUC AJUSTE FACTURACION")

    columna = buscandoColumna(driver, casos_negocio['columnas'], 'Solución')
    xpath = casos_negocio['filas'].replace('{contador}', columna)
    driver.find_element(By.XPATH, xpath).click()
    solucion = driver.find_element(By.XPATH, xpath + '/input')
    solucion.send_keys("SE CANALIZA A BO SUCURSALES")

    columna = buscandoColumna(driver, casos_negocio['columnas'], 'Motivo Cliente')
    xpath = casos_negocio['filas'].replace('{contador}', columna)
    driver.find_element(By.XPATH, xpath).click()
    motivoCliente = driver.find_element(By.XPATH, xpath + '/input')
    motivoCliente.send_keys("RETENCION")

    columna = buscandoColumna(driver, casos_negocio['columnas'], 'Estado')
    xpath = casos_negocio['filas'].replace('{contador}', columna)
    driver.find_element(By.XPATH, xpath).click()
    estado = driver.find_element(By.XPATH, xpath + '/input')
    estado.send_keys("Abierto") 
    estado.send_keys(Keys.RETURN)
    estado.send_keys(Keys.RETURN)
    sleep(5)

    try: driver.find_element(By.XPATH, casos_negocio['numeroCN']).click()
    except:
        error = 'Error Sin CN Ret'
        print('<<<<<<<<<<<<<<<<<<<<<<<' + error + ">>>>>>>>>>>>>>>>>>")
        return False, error
    try: 
        sleep(7)
        driver.find_element(By.XPATH, casos_negocio['actividades']).click()
        sleep(8)
        columna = buscandoColumna(driver, casos_negocio['columnasAct'], 'Comentarios')
        xpath = casos_negocio['filasAct'].replace('{contador}', columna)
        driver.find_element(By.XPATH, xpath).click()
        comentarioAct = driver.find_element(By.XPATH, xpath + '/textarea')
        comentarioAct.clear()

        if proceso == True: 

            comentarioAct.send_keys("RPF CON BENEFICIO AUTOMATICO BOT")
            columna = buscandoColumna(driver, casos_negocio['columnasAct'], 'Motivo del cierre')
            xpath = casos_negocio['filasAct'].replace('{contador}', columna)
            driver.find_element(By.XPATH, xpath).click()
            motivoCierre = driver.find_element(By.XPATH, xpath + '/input')
            motivoCierre.clear()
            motivoCierre.send_keys('SE APLICA AJUSTE')
            motivoCierre.send_keys(Keys.RETURN)

            columna = buscandoColumna(driver, casos_negocio['columnasAct'], 'Estado')
            xpath = casos_negocio['filasAct'].replace('{contador}', columna)
            driver.find_element(By.XPATH, xpath).click()
            sleep(1)
            driver.find_element(By.XPATH, casos_negocio['casillaEstado']).click()
            sleep(2)
            columna = buscandoColumna(driver, casos_negocio['estadoCerrado'], 'CERRADA')
            xpath = casos_negocio['estadoCerrado'].replace('{contador}', columna)
            driver.find_element(By.XPATH, xpath).click()
            sleep(3)

        else: 
            comentarioAct.send_keys("NO CUMPLE CON REGLAS DE APLICACION BOT")

            columna = buscandoColumna(driver, casos_negocio['columnasAct'], 'Motivo de la cancelación')
            xpath = casos_negocio['filasAct'].replace('{contador}', columna)
            driver.find_element(By.XPATH, xpath).click()
            motivoCancelacion = driver.find_element(By.XPATH, xpath + '/input')
            motivoCancelacion.clear()
            motivoCancelacion.send_keys('FALTA SOPORTE')

            columna = buscandoColumna(driver, casos_negocio['columnasAct'], 'Estado')
            xpath = casos_negocio['filasAct'].replace('{contador}', columna)
            driver.find_element(By.XPATH, xpath).click()
            sleep(1)
            driver.find_element(By.XPATH, casos_negocio['casillaEstado']).click()
            sleep(2)
            columna = buscandoColumna(driver, casos_negocio['estadoCerrado'], 'CANCELADA')
            xpath = casos_negocio['estadoCerrado'].replace('{contador}', columna)
            driver.find_element(By.XPATH, xpath).click()
            sleep(3)


        it.send('{CTRLDOWN}S{CTRLUP}')
        print('<<<<<<<<<<<<< ACTIVIDAD CERRADA/CANCELADA CON EXITO >>>>>>>>>>>>>>>>>')
        return True, ''
    except Exception as e:
        print(e)
        sleep(1000)
