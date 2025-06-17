#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

#-------------System-------------------#
from time import sleep
import os
import win32clipboard as cp

#---------Mis funciones---------------#


from utileria import *
from logueo import *
from rutas import *

from myFunctions import  AlertaSaldoVencido


def pantalla_ordenes_Servicio(driver, numero_orden):

    try:
        '''
        Funcion que ingresa a la pantalla de Ordenes de Servicio e ingresa una orden

        args:
            - driver (obj): instancia del navegador

        out:
            - driver (obj): instancia del navegador
            - stutus (bool): True si se pudo ingresar a 'Ordenes de Servicio' e ingreso la orden, False en caso contrario
        '''
        #Se define el maximo de espera para los elementos, si esto se excede, se genera una excepción
        wait = WebDriverWait(driver, 30)

        text_box('Pantalla:: Ordenes de Servicio', '☼')
        
        #Espera a que la página tenga el titulo de Home 
        element = wait.until(EC.title_contains('inicial'))

        #Entra a la ventana de Ordenes de servicio
        open_item_selenium_wait(driver, xpath ='//*[@id="s_sctrl_tabScreen"]/ul/li[6]' )

        #LUPA DE BUSQUEDA
        status_open = open_item_selenium_wait(driver, id='s_1_1_21_0_Ctrl',name ='s_1_1_21_0', xpath='//*[@id="s_1_1_21_0_Ctrl"]')
        if status_open == False:
            description_error('03','pantalla_ordenes_Servicio','No se encontró la lupa de búsqueda')
            return status_open
        
        #Se posiciona para escirbir en el campo de numero de orden
        print('Busqueda del numero de orden')
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1_s_1_l_Order_Number"]')))
        element.click()
        element = driver.find_element(By.XPATH,'//*[@id="1_Order_Number"]')
        element.clear()                    #Limpia lo que haya en el campo
        element.send_keys(numero_orden)    #Introduce el numero de orden
        element.send_keys(Keys.RETURN)     #Enter
        print('Se ingresó de número de orden')

        return driver, True
    
    except Exception as e:

        return driver, False

    

def validacion_orden_servicio(driver):
    '''
    Funcion que valida una orden de servicio al ser ingresada en la pantala 'Ordenes de servicio'
    
    args:
        - driver (obj): instancia del navegador
    
    out:
        - stutus (bool): True si la orden es valida, False en caso contrario
        - driver (obj): instancia del navegador
    '''
    text_box('Validación de Orden de Servicio', '☼')
    try:
        act = webdriver.ActionChains(driver)
        wait = WebDriverWait(driver, 30)

        print('▬Revisa si la orden esta vacia')

        '''------COPIA CON DOBLE CLICK-------'''
        #Localiza número orden en pantalla
        sleep(2)
        n_orden = driver.find_element(By.XPATH,"//*[@id='a_2']/div/table/tbody/tr[3]/td[4]/div/input")
        act.click(n_orden)
        act.double_click(n_orden).perform()
        texto = n_orden.get_attribute("value")
        if texto:
            print('Orden valida')
        else:
            print('La orden no es valida')
            return False, '', ''
    except Exception as e:
        print('No se pudo copiar en el portapapeles')
        description_error('04-1','validacion_orden_servicio',e)            
        response = 'PRUEBA'
        print('Respuesta de API (Orden erronea):: ',response)
        return False, '', ''
    

    try:
        print('▬Validacion del estado de la orden')
        #Se va al estado inmediato para copiarlo
        sleep(2)
        element_estado =  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div/form/div/span/div[3]/div/div/table/tbody/tr[15]/td[9]/div/input')
        act.click(element_estado)
        act.double_click(element_estado).perform()
        estado_orden = element_estado.get_attribute("value")
        print('Obtencion de estado')
        estado_orden = estado_orden.lower().strip()
        text_box('La cuenta está: ' + estado_orden,'◘')
        # #response = api.orden_cerrada(id_lead,sourceApi)
        # response = 'PRUEBA'
        # print ('Respuesta de la API: ',response)
        return True, driver, estado_orden
    
    except Exception as e:
        print(f'No se pudo validar el estado de la orden')
        description_error('04-3','validacion_orden_servicio',e)            
        return False, '', ''


def cerrar_orden_servicio(driver, cuenta_api, source_api, comentarios, motivo, estadoC):
    '''
    Funcion que cierra la orden de servicio 

    args:
        - driver (obj): instancia del navegador
        - cuenta_api (str): numero de cuenta liada a la orden de servicio, viene de la api
        - source_api(str): fuente de los datos
    out:
        - stutus (bool): True si la orden es valida, False en caso contrario
        - driver (obj): instancia del navegador
    '''
    act = webdriver.ActionChains(driver)
    wait = WebDriverWait(driver, 120)

    text_box('Cerrar orden pendiente / abierta', '☼')
    #Hace click en el enlace generado por la misma orden de servicio
    print('Clic en el enlace de la orden')
    element = driver.find_element(By.NAME,'Order Number').click() 
    #Se va a la cuenta para copiarla
    print('Llegue a la orden')
    element_cuenta = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[5]/td[3]/div/input')))
    act.click(element_cuenta)
    act.double_click(element_cuenta).perform()
    cuenta_siebel = my_copy(driver)
    
    if int(cuenta_siebel) != int(cuenta_api):
        text_box('Las cuentas no coinciden o la fuente no es la correcta', '▒')
        print(f'cuenta_siebel: {cuenta_siebel}')
        print(f'cuenta_api:    {cuenta_api}')
        print(f'source_api:    {source_api}')
        return  False
    

    #Se deben poner los campos que viene de la api de la API
    status_llenado = rellena_campos_orden_servicio(driver, comentarios, motivo, estadoC)
    if status_llenado != True:
        return False
    
    print('Validacion de cancelacion')
    
    #Entra a pantalla HOME
    #Si hay alerta no se canceló bien

    status_home = open_item_selenium_wait(driver, xpath =  home['home_from_sidebar']['xpath'] )
    if status_home == False:
        #IMPORTANTE:: No se ha localizado la alerta 
        sleep(10)
        text_box('Hay alerta de NO CANCELADO','▒')
        alert = driver.switch_to.alert
        alert.accept()
        #--------
        # cerrada = cerrarOrdenAgain(driver,numero_orden,comentarios, motivo, estado_orden)
        # #--------
        # if cerrada != True:
        #     response = api.cuenta_erronea(id_lead,source_id)
        #     print('Respuesta de API (ERROR DE CUENTA)',response)
    sleep(2)
    print('Se canceló con éxito ☺')
    return True


def rellena_campos_orden_servicio(driver, comentarios, motivo, estado): 
    '''
    Funcion que llena los campos al cerrar la orden de servicio

    args:
        - driver
        - comentarios
        - motivo
        - estado
    
    out: 
        - stutus (bool): True si se ingresaron todos los campos de la orden, False en caso contrario
    '''
    try:
        act = webdriver.ActionChains(driver)
        wait = WebDriverWait(driver, 120)
        
        text_box('Se llenan campos de Orden de Servicio','☼')
        #COMENTARIOS
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[11]/td[7]/div/textarea')))
        element.clear() 
        element.send_keys(comentarios)
        print('OK: comentarios')

        #MOTIVO
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[5]/td[9]/div/input')))
        sleep(0.5)
        element.clear()
        sleep(0.5)
        element.send_keys(motivo) #poner los de la API
        element.send_keys(Keys.ENTER)#if motivo o bie, entrar al drop y seleecionar
        print('OK: motivo')

        #Estado
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_1"]/div/table/tbody/tr[7]/td[9]/div/input')))
        sleep(2)
        act.double_click(element).perform()
        sleep(1)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        sleep(1)
        #-Paste
        element.send_keys(estado) 
        element.send_keys(Keys.ENTER)
        sleep(2)
        print('OK: estado')
        return True
    except Exception as e:
        print(f'No se pudieron ingresar los campos de la orden')
        description_error('05','rellena_campos_orden_servicio',e)
        return False    


def cerrarOrdenAgain(driver,numeroOrdenApi,comentarios, motivo, estado):
    print('▬▬Se volverá a intentar cerrar la orden▬▬')
    act = webdriver.ActionChains(driver)
    wait = WebDriverWait(driver, 120)
    #Pantalla de ORDENES
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[6]')))
    element.click()
    print('█Pantalla de Ordenes de Servicio')
    sleep(10)
    #LUPA
    try:
        lupa = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s_1_1_24_0_Ctrl"]')))
        #lupa.location_once_scrolled_into_view
        lupa.click()
        print('█Busqueda')
    except Exception as e:
        print('La ventana debe estar abierta')
        driver.quit()
        exit()
    #Insertar 
    #Se posiciona para escirbir en el campo de numero de orden
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1_s_1_l_Order_Number"]')))
    element.click()
    print('█Posicion')
    element = driver.find_element(By.XPATH,'//*[@id="1_Order_Number"]')
    element.clear()                    #Limpia lo que haya en el campo
    element.send_keys(numeroOrdenApi)  #Introduce el numero de orden
    element.send_keys(Keys.RETURN)     #Enter
    print('█Ingreso de número de orden')
    sleep(2)

    '''------COPIA CON DOBLE CLICK-------'''
    #Se va al estado inmediato para copiarlo
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1_s_1_l_Status"]'))).click()
    element = driver.find_element(By.XPATH, '//*[@id="1_Status"]')
    print('█Estado (inmediato)')
    #Doble click
    act = webdriver.ActionChains(driver)
    act.double_click(element).perform()
    #Copiar el estado (CRTL + C)
    #act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    '''------FIN COPIA DEOBLE CLICK-------'''
    #Hace click en el enlace generado
    sleep(2)
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[6]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]/a').click() 
    sleep(10)
    print('█Enlace')
    #Casmpos
    rellena_campos_orden_servicio(driver, comentarios, motivo, estado)
    #Mover a HOME
    #Entra a pantalla HOME
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[1]')))
    print('█Home')
    element.click()
    #Si hay alerta no se cancelo bien
    try:
        element = wait.until(EC.element_to_be_clickable((By.ID, 's_4_1_11_0_mb')))
        print('█Se canceló con éxito en el segundo intento')
        return True
    #FALTA RESVISAR LAS CUENTAS QUE DIGAN VIDEO
    except Exception as e:
        sleep(10)
        print('█Hay alerta de NO CANCELADO')
        alert = driver.switch_to.alert
        alert.accept()
        return False
    #Alerta
    #MARCAR COMO ERRONEA
    
    