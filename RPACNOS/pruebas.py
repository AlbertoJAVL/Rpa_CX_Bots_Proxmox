from funcionalidad import inicio, cierreOS
from login import loginSiebel
from time import sleep

# Inicio de Sesion    
driver, status_logueo = loginSiebel('kjdominguez', 'Enero.18570733')
sleep(1000)
# inicio(driver, '44792976', 'Contesta xxxx (nombre de quien validó el servicio técnico) Tel xxx (teléfono de contacto) confirma servicio ok', '1-208477909894')
# sleep(10)
# cierreOS(driver, '1-208477909894')

# FMTY-024284454