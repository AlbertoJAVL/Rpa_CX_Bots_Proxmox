#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

#---------- UTILERIAS --------------------#
from utileria import *
# import Services.ApiCyberHubOrdenes as api

# ----------SYSTEM -------------------
from time import sleep
import win32clipboard as cp

#-----------OTRAS--------------------
from json.decoder import JSONDecodeError
import socket

ERROR = "HA OCURRIDO UN ERROR EN LA FUNCION "
# SIEBEL = 'https://crmqa.izzi.mx/siebel/app/eCommunications/esn'
# SIEBEL = 'https://crmtest.izzi.mx/siebel/app/ecommunications/esn?SWECmd=Start'
SIEBEL = 'https://crm.izzi.mx/siebel/app/ecommunications/esn'

def start_webdriver():
    '''
    Esta funcion inicializa el webdriver (Chrome)
    
    out: 
        - driver: instancia de google chrome
    '''
    try:
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1024,768')
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        print(ip)
        print(type(ip))

        if '192.168.61.' in ip: driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome(
                                    executable_path =r"C:\\Rpa_CX_Bots_Proxmox\\chromedriver.exe",
                                    options=options
                                    )
        sleep(3)
        print('▬ Webdriver abierto correctamente')
        return driver
    except Exception as e:
        print('Error al abrir Web Driver')

def login_siebel(user, password):
    '''
    Funcion que hace el logeo en SIEBEL
    args:
        - user (str): usuario de siebel
        - pass (str): contraseña de siebel

    out:
        - driver(obj): instancia del navegador
        - stutus (bool): True si el incio de sesion fue correcto, False en caso contrario
    '''
    driver  = start_webdriver()
    driver.maximize_window()
    try:
        driver.get(SIEBEL)
        act = webdriver.ActionChains(driver)
        sleep(3)
        #En caso de que el explorador tenga conflicto con el protocolo de seguridad
        if  "Privacy" in driver.title or "privacidad" in driver.title or "Privacidad" in driver.title:
            print('♀ Error de privacidad')
            sleep(3)
            elem = driver.find_element(By.ID, "details-button").click()
            sleep(2)
            act.key_down(Keys.TAB)
            sleep(2)
            elem = driver.find_element(By.ID, "proceed-link").click()
            sleep(3)
            print('♀ Error de privacidad CERRADO')

            sleep(5)

        #Busca que el titulo de la pesataña sea el correcto
        if "Siebel Communications" in driver.title:
            #USER
            elem = driver.find_element(By.NAME,"SWEUserName")
            elem.clear()
            elem.send_keys(user)
            sleep(1)

            #PASSWORD
            elem = driver.find_element(By.NAME,"SWEPassword")
            elem.clear()
            elem.send_keys(password)
            sleep(1)

            #LOGIN (click)
            driver.find_element(By.ID,"s_swepi_22").click()
            sleep(5)
            
            #Validacion de credencailaes correctas
            try:
                status_bar  = driver.find_element(By.ID,"statusBar")
                act.click(status_bar)
                act.double_click(status_bar).perform()
                texto = my_copy(driver)
                if 'incorrecta' in texto:
                    print('CLAVES INVALIDAS')
                    driver.close()
                    return False
            except:
                print(f'INICIO DE SESION EXITOSO: {user}', '▬')
        else:
            print('NO SE PUDO ENCONTRAR LA PESTAÑA DE SIEBEL')
            driver.close()
            return False

        #sleep(10000) #Borrar después
        return driver, True
    except Exception as e:
        print('Error Login Siebel')
        driver.close()




def loginVISA(user, password):

    try:
        opciones = webdriver.ChromeOptions()
        opciones.add_argument('--ignore-certificate-errors') 
        opciones.add_experimental_option("excludeSwitches", ['enable-automation'])
        driver = webdriver.Chrome(options=opciones)

        driver.maximize_window()

        url = 'https://crm.izzi.mx/siebel/app/ecommunications/esn'
        driver.get(url)

        act = webdriver.ActionChains(driver)
        sleep(3)
        #En caso de que el explorador tenga conflicto con el protocolo de seguridad
        if  "Privacy" in driver.title or "privacidad" in driver.title or "Privacidad" in driver.title:
            print('♀ Error de privacidad')
            sleep(3)
            elem = driver.find_element(By.ID, "details-button").click()
            sleep(2)
            act.key_down(Keys.TAB)
            sleep(2)
            elem = driver.find_element(By.ID, "proceed-link").click()
            sleep(3)
            print('♀ Error de privacidad CERRADO')

            sleep(5)

        #Busca que el titulo de la pesataña sea el correcto
        if "Siebel Communications" in driver.title:
            #USER
            elem = driver.find_element(By.NAME,"SWEUserName")
            elem.clear()
            elem.send_keys(user)
            sleep(1)

            #PASSWORD
            elem = driver.find_element(By.NAME,"SWEPassword")
            elem.clear()
            elem.send_keys(password)
            sleep(1)

            #LOGIN (click)
            driver.find_element(By.ID,"s_swepi_22").click()
            sleep(5)
            
            #Validacion de credencailaes correctas
            try:
                status_bar  = driver.find_element(By.ID,"statusBar")
                act.click(status_bar)
                act.double_click(status_bar).perform()
                texto = my_copy(driver)
                if 'incorrecta' in texto:
                    print('CLAVES INVALIDAS')
                    driver.close()
                    return False
            except:
                print(f'INICIO DE SESION EXITOSO: {user}', '▬')
        else:
            print('NO SE PUDO ENCONTRAR LA PESTAÑA DE SIEBEL')
            driver.close()
            return False

        #sleep(10000) #Borrar después
        return driver, True
    except Exception as e:
        print('Error Login Siebel')
        driver.close()