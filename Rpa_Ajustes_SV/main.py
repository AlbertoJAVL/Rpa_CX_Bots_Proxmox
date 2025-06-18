#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bot de ajustes Siebel – versión robusta
"""
import os, gc, socket, logging, psutil
from contextlib import contextmanager
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from logging.handlers import RotatingFileHandler
from actividades import *

# ── Módulos propios ──────────────────────────────────────────────────────────
from eliminar_archivos_temporales import eliminar_archivos
import Services.ApiCyberHubOrdenes as api
from logueo import login_siebel
from utileria import text_box



# ── Config & logging ─────────────────────────────────────────────────────────
load_dotenv()                                        # Lee .env

LOG_PATH       = os.getenv("LOG_PATH", "rpa.log")
MAX_LOG_MB     = int(os.getenv("MAX_LOG_MB", 5))
BACKUP_COUNT   = int(os.getenv("BACKUP_COUNT", 5))
MEM_THRESHOLD  = int(os.getenv("MEM_THRESHOLD", 85))   # %
FINALIZADO_ERROR = 'FLUJO FINALIZADO CON ERROR'

logger = logging.getLogger("rpa")
logger.setLevel(logging.INFO)
h = logging.handlers.RotatingFileHandler(LOG_PATH,
                                         maxBytes=MAX_LOG_MB*1024*1024,
                                         backupCount=BACKUP_COUNT,
                                         encoding="utf-8")
h.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(h)

# ── Lógica principal de un ciclo ─────────────────────────────────────────────
def ejecutar_ciclo() -> bool:
    """Devuelve True si todo salió bien, False si hubo error lógico."""
    user = api.get_user()

    while True:
        orden = api.get_orden_servicio()[0]
        if orden == "SIN INFO":
            logger.info("Sin órdenes; pausa 15 s")
            sleep(15)
            return True

        if orden != "SIN INFO":
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            response = api.ajusteCerrado(
                    orden['id'],
                    orden['cuenta'],
                    orden['motivoAjuste'],
                    orden['comentarioAjuste'],
                    orden['cantidadAjustar'],
                    orden['tipoAplicacion'],
                    orden['cve_usuario'],
                    orden['fechaCompletado'],
                    orden['fechaCaptura'], 
                    'Registro pendiente', 
                    '0', 
                    ip, 
                    '-', 
                    '-', 
                    '-', 
                    orden['subStatus'],
                    orden['usuarioReproceso'],
                    orden['fechaReproceso'],
                    orden['usuarioCambio'],
                    orden['fechaCambio']
                    )
            print(f"Registro enocntrado reprocesando: {response}")
            try:
                workflow()
                logger.info("Orden %s procesada OK", orden["id"])
            except Exception as e:
                logger.exception("Fallo en orden %s: %s", orden.get("id"), e)
                return False

def workflow():
    '''
    Funcion encargada de hacer el flujo completo del bot

    '''
    try:
        #Inicio de sesion
        response = api.get_user()
        user = response['procesoUser']
        password = response['procesoPassword']
        driver, status_logueo = login_siebel(user, password)
        # driver, status_logueo = login_siebel('rpaajustes2.service', '6yckCF6GjhyxjJSU/')
        

        if status_logueo != True:
            print('Logueo Incorrecto')
            text_box(FINALIZADO_ERROR,'♦')
            return False
        
        while status_logueo == True:

            apiresponse = api.get_orden_servicio()
            info = apiresponse[0]
            print(info)

            host = socket.gethostname()
            ip = socket.gethostbyname(host)

            if info != 'SIN INFO':
                response = api.ajusteCerrado(
                    info['id'],
                    info['cuenta'],
                    info['motivoAjuste'],
                    info['comentarioAjuste'],
                    info['cantidadAjustar'],
                    info['tipoAplicacion'],
                    info['cve_usuario'],
                    info['fechaCompletado'],
                    info['fechaCaptura'], 
                    'Procesando', 
                    '0', 
                    ip, 
                    '-', 
                    '-', 
                    '-', 
                    info['subStatus'],
                    info['usuarioReproceso'],
                    info['fechaReproceso'],
                    info['usuarioCambio'],
                    info['fechaCambio']
                    )
                ajuste = info['cantidadAjustar']
                tipoAjuste = info['tipoAplicacion']
                no_cuenta = info['cuenta']
                motivoAjuste = info['motivoAjuste'].upper()
                ComentariosAjuste = info['comentarioAjuste']
                fecha = info['fechaCaptura']

                fechaCompletado = info['fechaCompletado']
                if fechaCompletado == None: pass
                else:
                    fechaCompletado = fechaCompletado[:10]

                if 'CARGO' in motivoAjuste or 'PAGO' in motivoAjuste or 'EXTEMPORANEO' in motivoAjuste: motivoAjuste = 'CARGO POR PAGO EXTEMPORANEO'
                elif 'CONVENIO' in motivoAjuste or 'COBRANZA' in motivoAjuste: motivoAjuste = "CONVENIO DE COBRANZA"
                else: 
                    status = 'Error Base Convenio'
                    response = api.ajusteCerrado(
                        info['id'],
                        info['cuenta'],
                        info['motivoAjuste'],
                        info['comentarioAjuste'],
                        info['cantidadAjustar'],
                        info['tipoAplicacion'],
                        info['cve_usuario'],
                        info['fechaCompletado'],
                        info['fechaCaptura'], 
                        status, 
                        '0', 
                        ip, 
                        '-', 
                        '-', 
                        estatusAjuste, 
                        info['subStatus'],
                        info['usuarioReproceso'],
                        info['fechaReproceso'],
                        info['usuarioCambio'],
                        info['fechaCambio'])
                    print(response)
                    driver.close()
                    driver.quit()
                    return False

                sleep(5)
                resultadoAplicacionAjuste, error, numAjuste, estatusAjuste = aplicacionAjuste(driver, fechaCompletado, ajuste, no_cuenta, tipoAjuste,motivoAjuste,ComentariosAjuste,fecha, info['subStatus'], info['numeroAjuste'])
                print('Aplicacion de Ajuste completa')
                if resultadoAplicacionAjuste == False:
                    print(error)
                    status = error
                    status2 = '-'
                    response = api.ajusteCerrado(
                        info['id'],
                        info['cuenta'],
                        info['motivoAjuste'],
                        info['comentarioAjuste'],
                        info['cantidadAjustar'],
                        info['tipoAplicacion'],
                        info['cve_usuario'],
                        info['fechaCompletado'],
                        info['fechaCaptura'], 
                        str(status), 
                        '0', 
                        ip, 
                        numAjuste, 
                        '-', 
                        estatusAjuste, 
                        str(status2),
                        info['usuarioReproceso'],
                        info['fechaReproceso'],
                        info['usuarioCambio'],
                        info['fechaCambio'])
                    print(response)
                    driver.close()
                    driver.quit()
                    return False
                        
                else:
                    resultadoCreacionCN, error, cnGenerado = generacionCN(driver)
                    print('Creacion de nuevo caso de negocio, completa')
                    if resultadoCreacionCN == False:
                        print('Falla al crear el caso de negocio')
                        status = error
                        status2 = '-'
                        response = api.ajusteCerrado(
                            info['id'],
                            info['cuenta'],
                            info['motivoAjuste'],
                            info['comentarioAjuste'],
                            info['cantidadAjustar'],
                            info['tipoAplicacion'],
                            info['cve_usuario'],
                            info['fechaCompletado'],
                            info['fechaCaptura'],
                            status, 
                            '0', 
                            ip, 
                            numAjuste, 
                            '-', 
                            estatusAjuste, 
                            status2,
                            info['usuarioReproceso'],
                            info['fechaReproceso'],
                            info['usuarioCambio'],
                            info['fechaCambio'])
                        print(response)
                        driver.close()
                        driver.quit()
                        return False
                    else:
                        print('Ajuste Completado')
                        status = 'Aplicación correcta'
                        status2 = '-'
                        response = api.ajusteCerrado(
                            info['id'],
                            info['cuenta'],
                            info['motivoAjuste'],
                            info['comentarioAjuste'],
                            info['cantidadAjustar'],
                            info['tipoAplicacion'],
                            info['cve_usuario'],
                            info['fechaCompletado'],
                            info['fechaCaptura'], 
                            status, 
                            '0', 
                            ip, 
                            numAjuste, 
                            cnGenerado, 
                            estatusAjuste,
                            status2,
                            info['usuarioReproceso'],
                            info['fechaReproceso'],
                            info['usuarioCambio'],
                            info['fechaCambio'])
                        print(response)
            
            else:
                try:
                    # os.system('cls')
                    print('Esperando mas Ajustes')
                    sleep(15)
                    print('Regreso a HOME')
                    result = open_item_selenium_wait(driver, xpath = home['home_from_sidebar']['xpath'])
                    if result == False:
                        driver.close()
                        driver.quit()
                        return False
                    text_box('FIN EL CICLO COMPLETO', '-')
                    os.system('cls')
                except Exception as e:
                    logger = logging.getLogger("rpa")
                    logger.exception("Fallo en orden %s: %s", e) 
                    driver.close()
                    driver.quit()
                    return False
    except Exception as e: 
        print(e)
        return False

# ── Bucle infinito con gestión de errores ───────────────────────────────────
def main():
    conteo_errores = 0                      # ← YA NO se reinicia dentro del while
    while True:
        try:
            eliminar_archivos()
            ok = ejecutar_ciclo()
            conteo_errores = 0 if ok else conteo_errores + 1
            if conteo_errores >= 5:
                logger.error("Umbral de errores (5) alcanzado – revisar RPA")
                conteo_errores = 0
        except Exception as exc:
            logger.exception("Excepción no controlada: %s", exc)
            conteo_errores += 1

        if psutil.virtual_memory().percent > MEM_THRESHOLD:
            logger.warning("Memoria al %s %% – reiniciando navegador",
                           psutil.virtual_memory().percent)

        sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupción manual.")
