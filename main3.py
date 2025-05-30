from time import sleep
from dotenv import load_dotenv
import sys,os,re
import requests
# import #socket_boot as #socket
import socket



ID = ""
STATUS = ""


def changeStatusBot(estado):
    try:
        hostname= socket.gethostname()
        ip = socket.gethostbyname(hostname)
        url = f'https://rpabackizzi.azurewebsites.net/Bots/updateProcessStatusBot?ip={ip}&estado={estado}'
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        response.raise_for_status()

        # Accede a los datos de la respuesta (pueden ser JSON, texto, etc.)
        # print("Contenido de la respuesta:", response.text)
        return response.text


    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None
        

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def stop():
    output = os.popen('wmic process get description,processid').read()
    separador = output.split('\n')
    for val in separador:
        # print(val)
        b = re.search("powershell.exe",val)
        # c = re.search("siebel.exe",val)
        c = re.search("chrome.exe",val)
        d = re.search("py.exe",val)
        if b:
            os.system('TASKKILL /F /IM powershell.exe /T')
        if c:
            os.system('taskkill /IM chrome.exe')
            os.system('taskkill /IM py.exe')

while True:
    sleep(3)
    load_dotenv(override=True)
    id_1=os.getenv('proceso')
    status_1=os.getenv('status')
    print(id_1)
    print(status_1)
    if ID!= id_1 or STATUS!= status_1:
        ID = id_1
        STATUS = status_1

        if (ID == "1" or ID == "3" or ID == "4" or ID == "29") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Not Done (Validacion)")
            stop()
            sleep(5)
            # aa = resource_path('./Boot_Cancelacion/main.py')
            aa ='./Rpa_Not_done/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "1" or ID == "3" or ID == "4" or ID == "29") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Not Done (Validacion)")
            stop()
            changeStatusBot(0)
        elif (ID == "5") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Not Done Canelacion OS (Sin Validacion)")
            stop()
            sleep(5)
            aa ='./Rpa_Not_done_Cancelacion/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "5") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Not Done Canelacion OS (Sin Validacion)")
            stop()
            changeStatusBot(0)
        elif (ID == "19") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Not Done Generacon CN (Sin Validacion)")
            stop()
            sleep(5)
            aa ='./Rpa_Not_done_Generacion_CN/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "19") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Not Done Generacon CN (Sin Validacion)")
            stop()
            changeStatusBot(0)
        elif (ID == "20" or ID=="21" or ID=="22" or ID == "30" or ID =="45") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Ajustes (Validacion)")
            stop()
            sleep(5)
            aa ='./Rpa_Ajustes_CV/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "20" or ID=="21" or ID=="22" or ID == "30" or ID =="45") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Ajustes (Validacion)")
            stop()
            changeStatusBot(0)
        elif (ID == "23" or ID =="46" or ID =="47" or ID =="48" or ID =="49") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Ajustes (Sin Validacion)")
            stop()
            sleep(5)
            aa ='./Rpa_Ajustes_SV/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "23" or ID =="46" or ID =="47" or ID =="48" or ID =="49") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Ajustes (Sin Validacion)")
            stop()
            changeStatusBot(0)
        elif (ID == "24" or ID == "25" or ID == "26" or ID == "27" or ID == "28" or ID=="31") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Depuracion CC")
            stop()
            sleep(5)
            aa ='./Rpa_Depuracion_CC/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "24" or ID == "25" or ID == "26" or ID == "27" or ID == "28" or ID=="31") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Depuracion CC")
            stop()
            changeStatusBot(0)
        elif (ID == "32") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de RPA Ajustes (Extemporaneo)")
            stop()
            sleep(5)
            aa ='./Rpa_cargoExt_convenio_cob/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "32") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de RPA Ajustes (Extemporaneo)")
            stop()
            changeStatusBot(0)
        elif (ID == "33") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Depuracio Ext")
            stop()
            sleep(5)
            aa ='./Rpa_Depuracion_Ext/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "33") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Depuracio Ext")
            stop()
            changeStatusBot(0)
        elif (ID == "34" or ID =="37") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Creacion de Orden")
            stop()
            sleep(5)
            aa ='./RPA_VIX/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "34" or ID =="37") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Creacion de Orden")
            stop()
            changeStatusBot(0)
        elif (ID == "35") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Creacion de Orden")
            stop()
            sleep(5)
            aa ='./Rpa_ExtraccionesAutomatizadas/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "35") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Creacion de Orden")
            stop()
            changeStatusBot(0)
        elif (ID == "36") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Creacion de Orden")
            stop()
            sleep(5)
            aa ='./Rpa_ExtraccionesManuales/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "36") and STATUS=="STOPED":
            print("Iniciando el proceso STOP de Creacion de Orden")
            stop()
            changeStatusBot(0)
        elif (ID == "43" or ID =="44") and STATUS=="STARTED":
            print("Iniciando el proceso STARTED de Ordenes Call Trouble")
            stop()
            sleep(5)
            aa ='./Rpa_Call_Trouble/tele.py'
            os.system(f"start powershell python {aa}")
            changeStatusBot(1)
        elif (ID == "43" or ID =="44") and STATUS=="STOPED":
            print("Deteniendo el proceso STOP de Ordenes Call Trouble")
            stop()
            changeStatusBot(0)
    else:
        print("No han cambiado las variables")
        # changeStatusBot(0)