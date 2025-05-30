#----------Selenium--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

#-------------System-------------------#
from time import sleep

#---------Mis funciones---------------#
from utileria import *
from logueo import *
from rutas import *
from myFunctions import  AlertaSaldoVencido


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
        wait = WebDriverWait(driver, 120)
        text_box('Pantalla Unica de Consulta', '☼')

        #Entra a la ventana de Pantalla Unica de Consulta
        open_item_selenium_wait(driver, xpath = pantalla_unica['home']['xpath'] )

        #Espera a que la página tenga el titulo de Home 
        element = wait.until(EC.title_contains('Resumen'))
        print('Entró a la Pantalla Unica')
        sleep(20)

        #LUPA DE BUSQUEDA
        try:
            print('click label')
            driver.find_element(By.XPATH, "//button[@aria-label='Pantalla Única de Consulta Applet de formulario:Consulta']").click()
        except:
            status_open = open_item_selenium_wait(driver, id = pantalla_unica['lupa']['id'] ,name = pantalla_unica['lupa']['name'], xpath =  pantalla_unica['lupa']['xpath'])
            print(f"Va a buscar la cuenta: {cuenta_api}")
            if status_open == False:
                description_error('07','pantalla_unica_consulta','No se encontró la lupa de búsqueda')
                return False
        sleep(15)
        #Se posiciona para escirbir en el campo de numero de orden
        element = driver.find_element(By.XPATH, pantalla_unica['ingresar_cuenta']['xpath'])
        element.clear()                    #Limpia lo que haya en el campo
        element.send_keys(cuenta_api)    #Introduce el numero de orden
        element.send_keys(Keys.RETURN)     #Enter

        #Resvisa si tiene saldo pendiente
        open_item_selenium_wait(driver ,name = pantalla_unica['saldo_pendiente']['name'], xpath =  pantalla_unica['saldo_pendiente']['xpath'])

        print('Se ingresó el numero de cuenta correctamente')

        return True
        
    except Exception as e:
        print(f'No se pudo entrar a Pnatlla Unica de Consulta')
        description_error('08','pantalla_unica_consulta.',e)
        return False

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
        #Busca la lupa de casos
        open_item_selenium_wait(driver ,name = caso_negocio['lupa']['name'], xpath = caso_negocio['lupa']['xpath'])
        sleep(10)
        print('▬▬Agregar caso de negocio▬▬')
        AlertaSaldoVencido(driver)

        #Medio de Contacto
        element = driver.find_element(By.XPATH, caso_negocio['medio_contacto']['xpath'] )
        element.clear() 
        element.send_keys(medio_contacto)
        print('OK: MEDIO DE CONTACTO')

        #Categoría
        element = driver.find_element(By.XPATH, caso_negocio['categoria']['xpath'] )
        element.send_keys(categoria)
        print('OK: CATEGORÍA')

        #Motivo
        element = driver.find_element(By.XPATH, caso_negocio['motivo']['xpath'] )
        element.send_keys(motivo)
        print('OK: MOTIVO')

        #Submotivo
        element = driver.find_element(By.XPATH, caso_negocio['sub_motivo']['xpath'] )
        element.send_keys(sub_motivo)
        print('OK: SUBMOTIVO')

        #Solucion
        element = driver.find_element(By.XPATH, caso_negocio['solucion']['xpath'] )
        element.send_keys(solucion)
        element.send_keys(Keys.ENTER)
        print('OK: SOLUCION')
        
        #En caso de que haya caso de negocio repetido
        status_caso_repetido = AlertaCasoNegocio(driver)
        if status_caso_repetido == True:
            print('EL caso de negocio esta repetido')
            response_caso_negocio = 0 #Respuesta de que ya existe
            sleep(2)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s_13_1_27_0_Ctrl"]'))).click() #FALTA MAEPAR
            AlertaSaldoVencido(driver)
            return response_caso_negocio 


        #Copiar el numero del caso
        
        # act.click(element_num_caso)
        # act.double_click(element_num_caso).perform()
        # numero_caso_negocio = my_copy(driver)
        # print('CASO DE NEGOCIO',numero_caso_negocio)
      

        # if numero_caso_negocio != '':
        #     print('Caso de negocio:', numero_caso_negocio)
        # else: 
        #     print('No se copio caso de negocio')
        #     return False #Ver que debe regresar

        #Motivo de Cierre
        element = driver.find_element(By.XPATH, caso_negocio['motivo_cierre']['xpath'] )
        element.send_keys(motivo_cierre)
        element.send_keys(Keys.ENTER)
        print('OK: MOTIVO DE CIERRE')

        sleep(30)

        #Comentarios
        driver.find_element(By.XPATH, caso_negocio['comentarios']['xpath'] ).click()
        element = driver.find_element(By.XPATH, caso_negocio['comentarios']['xpath'] + '/textarea')
        element.send_keys(comentarios)
        element.send_keys(Keys.ENTER)
        print('OK: COMENTARIOS')
        

        #ESTADO
        element = driver.find_element(By.XPATH, caso_negocio['estado']['xpath'] )
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

        element.send_keys(estado)
        sleep(2)

        numero_caso_negocio =  driver.find_element(By.XPATH, caso_negocio['numero_caso']['xpath'])
        numero_caso_negocio = numero_caso_negocio.get_attribute("value")

        element.send_keys(Keys.ENTER)
        
        print('OK: ESTADO')
        print('Caso terminado')

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
