import win32clipboard as cp

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep

'''Copiar, asignar a una variable y limiar el clipboard'''
def copyAsignar(element,driver):
    try:
        act = webdriver.ActionChains(driver)
        act.double_click(element).perform()
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        cp.OpenClipboard() 
        asignacion = cp.GetClipboardData()
        cp.SetClipboardText('')
        cp.CloseClipboard()
        return asignacion
    except Exception as e:
        print("Hubo un error al copiar un elemento: ",element)
        print('ERROR', e)

'''SEPARACION DE IMPRESION'''

def myPrint(texto,caracter):
    print(caracter*40)
    print(texto)
    print(caracter*40)




'''CIERRE DE ALERTA DE SALDO VENCIDO'''
def AlertaSaldoVencido(driver):
    sleep(3)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print('SI hubo alerta')
        sleep(3)
    except Exception as e:
        print('NO hubo alerta')

'''CASO DE NEGOVIO REPETIDO'''
def AlertaCasoNegocio(driver):
    sleep(3)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print('CASO DUPLICADO :C')
        return True
    except Exception as e:
        print('CASO SIN DUPLICAR :D')
        return False