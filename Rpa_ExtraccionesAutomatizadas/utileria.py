
#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

# ----------SYSTEM -------------------
from time import sleep
import win32clipboard as cp

ERROR = "HA OCURRIDO UN ERROR EN LA UTILERIA "

def text_box(string, character = '*'):
    '''
    Funcion que imprime un string en una caja

    args:
        - string (str): cadena a setear
        - character (str): carcater que enmarca el texto
            - default: *
    '''

    len_string = len(string) + 4

    print(character*len_string)
    print(character + ' ' + string + ' ' +character )
    print(character*len_string)

def my_copy(driver):
    '''
    Funcion que teclea 'ctrl + c' para copiar un texto previamente seleccionado y lo asigna a una variable

    args:
        - driver: instancia del navegador

    out:
        - texto: str  
    '''
    act = webdriver.ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

    try: 
        sleep(5)
        cp.OpenClipboard() 
        texto = cp.GetClipboardData()
        cp.EmptyClipboard()
        cp.CloseClipboard()
        if texto and texto != ' ' and texto !='vacio':
            print(f'Texto copiado: {texto}')
        else:
            return False
        return texto
    except Exception as e:
        mensaje = f"{ERROR} my_copy. ERROR ENCONTRADO {e}"
        print(mensaje)

def description_error(numero_error, nombre_funcion, error = 'No identificado'):
    '''
    Funcion que manda el tipo de error con su descripcion
    
    args:
        - numero_error (int): identificador del error
        - nombre_funcion (str): nombre de la funcion donde se tiene el error
        - error (exception): error que lanza el except de la funcion 

    '''
    
    mensaje = f'CYBER-{str(numero_error)}: HA OCURRIDO UN ERROR EN LA FUNCION: {str(nombre_funcion)}.'
    text_box(mensaje)
    print('ERROR ENCONTRADO: \n ')
    print(error)
    print('▒'*len(mensaje))
    sleep(10)


def open_item_selenium(driver, id = None, name = None, xpath = None, clase = None):
    '''
    Funcion que da clics en un item según el metodo de apertura encontrado. Con espera definida

    args:
        - driver
        - Minimo uno de los siguientes:
            - id (str)
            - name
            - xpath
            - clase
    out:
        bool: True si pudo localizar y abirir el elemento indicado

    '''

    sleep(2)
    try:
        if id ==None:
            a = 2/0 #Buscar un excepcion 
        #print('Busqueda por ID')

        driver.find_element(By.ID, id).click()
        return True
    except Exception as e:
        #print(e)
        try:
            if name != None:
                    #print('Busqueda por NAME')
                    driver.find_element(By.ID, name).click()
                    return True
            if xpath != None:
                    #print('Busqueda por XPATH')
                    driver.find_element(By.ID, xpath).click()
                    return True
            if clase != None:
                    #print('Busqueda por CLASS_NAME')
                    driver.find_element(By.ID, clase).click()
                    return True
        except Exception as e:
            print(f'No se pudo abrir el item especificado')
            description_error('06','open_item_selenium_wait.',e)
            return False

def open_item_selenium_wait(driver, id = None, name = None, xpath = None, clase = None):
    '''
    Funcion que da clics en un item según el metodo de apertura encontrado. Con espera definida

    args:
        - driver
        - Minimo uno de los siguientes:
            - id (str)
            - name
            - xpath
            - clase
    out:
        bool: True si pudo localizar y abirir el elemento indicado

    '''

    wait = WebDriverWait(driver, 30)
    act = webdriver.ActionChains(driver)
    sleep(2)
    try:
        if id ==None:
            a = 2/0 #Buscar un excepcion 
        #print('Busqueda por ID')
        wait.until(EC.element_to_be_clickable((By.ID, id))).click()
        return True
    except Exception as e:
        #print(e)
        try:
            if name != None:
                    #print('Busqueda por NAME')
                    wait.until(EC.element_to_be_clickable((By.NAME, name))).click()
                    return True
            if xpath != None:
                    #print('Busqueda por XPATH')
                    wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    return True
            if clase != None:
                    #print('Busqueda por CLASS_NAME')
                    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, clase))).click()
                    return True
        except Exception as e:
            print(f'No se pudo abrir el item especificado')
            description_error('06','open_item_selenium_wait.',e)
            return False
