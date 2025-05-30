import subprocess
from subprocess import Popen
from time import sleep
import requests
from datetime import datetime
import pytz
import autoit
import os
import re
import socket

count = 0

hostname= socket.gethostname()
ip = socket.gethostbyname(hostname)

def send_msg():
    IST = pytz.timezone('America/Mexico_City')
    raw_TS = datetime.now(IST)
    curr_date= raw_TS.strftime("%d-%m-%Y")
    curr_time= raw_TS.strftime("%H-%M-%S")
    msg = f"Extraccion Automatizadas Vix 16 {ip} se ha detenido:  {curr_date} at {curr_time}"
    telegram_api=f"https://api.telegram.org/bot6819354375:AAFb2UuBWfbOkT83YDyt2IH_lHSUgOpnkuU/sendMessage?chat_id=-1002094293899&text={msg}"
    tel_resp = requests.get(telegram_api)
    if tel_resp.status_code == 200:
        print("INFO: Notification has been sent on Telegram")
    else:
        print("ERROR: Could not send Message")

def close_explorer():
    mas=0
    output = os.popen('wmic process get description, processid').read()
    separador = output.split("\n")
    for val in separador:
        a = re.search("iexplore.exe",val)
        if a:
            mas+=1
    if mas !=0:
        for i in range(mas-1):
            os.system('taskkill /IM Iexplore.exe')


def ini_bot():
    while True:
        count=0
        sleep(10)
        # a = autoit.process_exists("cmd.exe")
        a = autoit.process_exists("py.exe")
        print(a)
        # print(a)
        # if a !=0:
        #     output = os.popen('wmic process get description, processid').read()
        #     separador = output.split("\n")
        #     for val in separador:
        #         b = re.search("iexplore.exe",val)
        #         if b:
        #             count+=1
        #     # print("Esto es el count",count)
        #     if count >=2:
        #         # print("hay mas de tres ventanas abiertas")
        #         close_explorer()
        if a==0:
            send_msg()
            os.startfile(r"C:\Rpa_CX_Bots_Proxmox\Rpa_ExtraccionesAutomatizadas\extracciones.bat")  
            sleep(30)


try:
    ini_bot()
except Exception as e:
    ini_bot()
    print("Keyboardinterrupt exception is caught")
  