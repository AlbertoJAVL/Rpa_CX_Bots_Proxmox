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

#---------Mis funciones---------------#
from utileria import *
from logueo import *
from rutas import *
from myFunctions import  AlertaSaldoVencido

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

def pantalla_unica_consulta(driver, cuenta_api):
    '''
    Esta funcion ingresa a Pantalla Unica de Consulta y busca una cuenta.
    arg:
        - driver
        - cuenta_api (str): el numero de cuenta a buscar

    out: 
        - bool: True si ingresó correctamente a Pantalla Unica e ingreso la cuenta

    '''
    
    try:
        text_box('Pantalla Unica de Consulta', '☼')

        # Entra a pantalla unica
        lupa_busqueda_cn, res = cargandoElemento(driver, 'a', 'title', 'Pantalla Única de Consulta')
        if lupa_busqueda_cn == False:
            if 'Inconsistencia' in res: return False
            else:  return False

        # Elemento de busqueda de cuenta
        lupa_busqueda_cn, res = cargandoElemento(driver, 'button', 'aria-label', 'Pantalla Única de Consulta Applet de formulario:Consulta')
        if lupa_busqueda_cn == False: 
            if 'Inconsistencia' in res: return False
            else: return False
        
        # Input de ingreso de cuenta
        lupa_busqueda_cn, res = cargandoElemento(driver, 'input', 'aria-label', 'Numero Cuenta')
        if lupa_busqueda_cn == False: 
            if 'Inconsistencia' in res: return False
            else: return False
        
        # Ingreso de cuenta
        inputNCta = driver.find_element(By.XPATH, "//input[@aria-label='Numero Cuenta']")
        inputNCta.send_keys(cuenta_api)
        inputNCta.send_keys(Keys.RETURN)

        # Validacion de pantalla cargada
        cargaPantalla, res = cargandoElemento(driver, '', '', '', path= "//*[contains(@aria-label,'Perfil de Pago')]")
        if cargaPantalla == False: 
            if 'Inconsistencia' in res: return False
            else: return False

        print('Se ingresó el numero de cuenta correctamente')

        return True
        
    except Exception as e:
        print(f'No se pudo entrar a Pnatlla Unica de Consulta')
        description_error('08','pantalla_unica_consulta.',e)
        return False

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
    
def nuevo_caso_negocio(driver, medio_contacto, categoria, motivo, sub_motivo, solucion, motivo_cierre, comentarios, estado):
    '''
    Esta fucnion crea un nuevo caso de negocio en pantalla unica de servicio
    
    args:
        - driver
        - medio_contacto
        - categoria
        - categoria
        - motivo
        - sub_motivo
        - solucion
        - motivo_cierre
        - comentarios
        - estado

    out: Puede tener tres tipos de respuestas
        - numeric (integer): 0 para caso repetito, 2 para caso abierto
        - False (boolean): en caso de que la funcion tenga un error
        - numero_caso_negocio (str):  el numero del caso de negocio creado
    '''
    try:

        wait = WebDriverWait(driver, 120)
        act = webdriver.ActionChains(driver)

        text_box('Nuevo Caso de Negocio')
        
        # Creacion CN
        btn_creacion_Ajuste, res = cargandoElemento(driver, 'button', 'aria-label', 'Casos de Negocio Applet de lista:Nuevo')
        if btn_creacion_Ajuste == False: return False

        print('▬▬Agregar caso de negocio▬▬')
        AlertaSaldoVencido(driver)

        #Medio de Contacto
        textoLabelMedioContactoCN = 'Medio de contacto'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMedioContactoCN + "']").click()
        medioContactoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMedioContactoCN + "']")
        medioContactoCN.clear()
        medioContactoCN.send_keys(medio_contacto)
        medioContactoCN.send_keys(Keys.RETURN)
        print('OK: MEDIO DE CONTACTO')
        sleep(2)

        #Categoría
        textoLabelCategoriaCN = 'Categoria'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelCategoriaCN + "']").click()
        categoriaCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelCategoriaCN + "']")
        categoriaCN.clear()
        categoriaCN.send_keys(categoria)
        categoriaCN.send_keys(Keys.RETURN)
        print('OK: CATEGORÍA')
        sleep(2)

        #Motivo
        textoLabelMotivoCN = 'Motivo'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMotivoCN + "']").click()
        motivoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelMotivoCN + "']")
        motivoCN.clear()
        motivoCN.send_keys(motivo)
        motivoCN.send_keys(Keys.RETURN)
        print('OK: MOTIVO')
        sleep(2)

        #Submotivo
        textoLabelSubMotivoCN = 'Submotivo'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelSubMotivoCN + "']").click()
        subMotivoCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelSubMotivoCN + "']")
        subMotivoCN.clear()
        subMotivoCN.send_keys(sub_motivo)
        subMotivoCN.send_keys(Keys.RETURN)
        print('OK: SUBMOTIVO')
        sleep(2)

        #Solucion
        try:
            textoLabelsolucionCN = 'Solución'
            driver.find_element_by_xpath("//input[@aria-label='" + textoLabelsolucionCN + "']").click()
            solucionCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelsolucionCN + "']")
            solucionCN.clear()
            solucionCN.send_keys(solucion)
            solucionCN.send_keys(Keys.RETURN)
            sleep(5)
        except Exception:
            try:
                alerta = Alert(driver)
                alerta.accept()
                return 0
            except: pass
        print('OK: SOLUCION')
        sleep(2)

        #Motivo de Cierre
        textoLabelmotivoCierreCN = 'Motivo del Cierre'
        driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoCierreCN + "']").click()
        motivoCierreCN = driver.find_element_by_xpath("//input[@aria-label='" + textoLabelmotivoCierreCN + "']")
        motivoCierreCN.clear()
        motivoCierreCN.send_keys(motivo_cierre)
        motivoCierreCN.send_keys(Keys.RETURN)
        print('OK: MOTIVO DE CIERRE')
        sleep(5)

        #Comentarios
        textoLabelcomentarioCN = 'Comentarios'
        driver.find_element_by_xpath("//textarea[@aria-label='" + textoLabelcomentarioCN + "']").click()
        comentarioCN = driver.find_element_by_xpath("//textarea[@aria-label='" + textoLabelcomentarioCN + "']")
        comentarioCN.clear()
        comentarioCN.send_keys(comentarios)
        print('OK: COMENTARIOS')
        
        numero_caso_negocio =  driver.find_element(By.XPATH, caso_negocio['numero_caso']['xpath'])
        numero_caso_negocio = numero_caso_negocio.get_attribute("value")

        #ESTADO
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]').click()
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span').click()
        sleep(5)
        pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div'
        posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
        if posicion == False: 
            pathEstadoCNOpc = '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[{contador}]/div'
            posicion = obtencionColumna(driver, 'Cerrado', pathEstadoCNOpc)
            if posicion == False: return False
            
        driver.find_element(By.XPATH, pathEstadoCNOpc.replace('{contador}', posicion)).click()
        
        sleep(5)
        print('OK: ESTADO')
        print('Caso terminado')

        driver.find_element(By.XPATH, "//button[@aria-label='Casos de negocio Applet de formulario:Guardar']").click()
        print('CN Guardado')
        sleep(7)

        #Falta comprobar que si se haya cerrado.
        

        return numero_caso_negocio
        
    except Exception as e:
        print(f'No se pudo completar el caso de negocio')
        description_error('10','nuevo_caso_negocio.',e)
        return False
    

def AlertaCasoNegocio(driver):
    '''
    Esta funcion confirma si hay un caso de negocio tipificado de la misma manera que el insertado

    args: 
        - driver
    
    out:
        - bool: True si el caso esta repetido
    '''
    sleep(3)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        return True
    except Exception as e:
        return False
    

####----------------PRUEBAS DE CASO DE NEGOCIO------------------------------

# USER = "p-jlima"
# PASS = 'sobu*8vlDros'
# driver = driver, status_logueo = login_siebel(USER, PASS)

# pantalla_unica_consulta(driver, cuenta_api='24676204')
# nuevo_caso_negocio(driver,  
#                 medio_contacto  = 'Outbound',
#                 categoria  = 'OUTBOUND',
#                 motivo  = 'SEGUIMIENTOS ESPECIALES',
#                 sub_motivo  = 'LIMPIEZA DE POOL',
#                 solucion  = 'ORDEN YA COMPLETA',
#                 comentarios  = 'COMENTARIOS PRUEBA',
#                 motivo_cierre  = 'BO CONFIRMA Y SOLUCIONA',
#                 estado  = 'Cerrado')
