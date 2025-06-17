#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

#---------- UTILERIAS --------------------#
from utileria import *
#----ANTIGUAS-----
from myFunctions import myPrint
import Services.ApiCyberHubOrdenes as api

# ----------SYSTEM -------------------
from time import sleep
import win32clipboard as cp

#-----------OTRAS--------------------
from json.decoder import JSONDecodeError
import socket

ERROR = "HA OCURRIDO UN ERROR EN LA FUNCION "
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
        description_error('01','start_webdriver',e)

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
        if  "privacidad" in driver.title:
            print('♀ Error de privacidad')
            sleep(3)
            elem = driver.find_element(By.ID, "details-button").click()
            sleep(2)
            act.key_down(Keys.TAB)
            sleep(2)
            elem = driver.find_element(By.ID, "proceed-link").click()
            sleep(3)
            print('♀ Error de privacidad CERRADO')

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
            
            #Validacion de credencailaes validas
            try:
                status_bar  = driver.find_element(By.ID,"statusBar")
                act.click(status_bar)
                act.double_click(status_bar).perform()
                texto = my_copy(driver)
                if 'incorrecta' in texto:
                    print('CLAVES INVALIDAS')
                    driver.quit()
                    return '', False
            except:
                print('CLAVES VALIDAS')
        else:
            text_box('NO SE PUDO ENCONTRAR LA PESTAÑA DE SIEBEL')
            driver.quit()
            return '', False

        #sleep(10000) #Borrar después
        return driver, True
    except Exception as e:
        description_error('02','login_siebel',e)
        driver.quit()
        return '', False






#### --------------------------NO REVISADAS-------------------------------

'''VERIFICA USUSARIO Y ORDENES'''

def verifica_logueo():
    try:
        data = api.usuario()
        
        if data != None:
            print('▬'*50)
            print('Orden encontrada')
            usser = data['user']
            password= data['password']
            myPrint('USSER: {0} \nPASS: {1}'.format(usser,password), '✧')
            print('▬'*50)
            
            sesion = usser
            #start = login(usser,password)
            return data

        else:
            #print('Usuairo inválido, relogueo.')
            verifica_logueo()
    except JSONDecodeError:
            return data.body_not_json



'''COSNULTA LA ORDEN DE LA API'''

def ConsultaApi():
    flag = False 
    while flag == False:
        myPrint('Conuslta orden','♦')
        orden = api.get_orden_servicio()
        status = orden['status']
        if status == True:
            keys = orden['access_data']
            user = keys['user']
            password = keys['password']
            if user == 'p-lggarciah' or user == 'p-jlima':
                print('▬'*50)
                print('Orden encontrada')
                myPrint('USSER: {0} \nPASS: {1}'.format(user,password), '✧')
                print('▬'*50)
                #print(orden)
                sleep(10)
                print(user, password)
                return orden, user, password
                
            else:
                print('Usuario no válido')
        else:
            print("No hay ordenes")
            print("Espere...")
            sleep(10)
            print('▬▬Reiniciando programa▬▬')
            #Recursvidad
            


