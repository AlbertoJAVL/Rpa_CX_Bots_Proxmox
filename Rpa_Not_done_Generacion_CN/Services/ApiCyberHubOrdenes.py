import requests
import json
import os 
import autoit as a
from json.decoder import JSONDecodeError
from tkinter import messagebox as MessageBox
from time import sleep
import socket


hostname= socket.gethostname()
ip = socket.gethostbyname(hostname)



url = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/getCuentaCasosNegocioSinValidacion'
urlOrden = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/ActualizaCasosNegocioSinValidacion'
urlPassUser = 'https://rpabackizzi.azurewebsites.net/Bots/getProcess?ip='+str(ip)




#region Datos


def get_user():
    try:
        response = requests.get(urlPassUser) 
        if response.status_code == 200:
            reseponseApi = json.loads(response.text)
            return reseponseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
        return response.body_not_json

def get_extraccion():
    try:
        response = requests.get(url) 
        if response.status_code == 200:
            reseponseApi = json.loads(response.text)
            return reseponseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
        return response.body_not_json

apiresponse = get_extraccion()          

info = apiresponse[0]
# nOrden = info['numeroOrden']
# cuenta = info['cuenta']
print(info)
# print(nOrden, cuenta)

# datosSR = info['parametrosExtraccion']

# print(datosSR)

#endregion




def update(datos,parametros):

    try:
        response = requests.put(urlOrden, params=parametros, json=datos, verify=False)
        if response.status_code == 200:
            responseApi = json.loads(response.text)
            return responseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
            return response.body_not_json

def notDone_cerrado(casoNegocio, id, cuenta, categoria, motivos, submotivos, solucion, motivoCliente,comentarios,estado, cve_usuario, fechaCompletado, fechaCaptura, status, procesando, ip):
    datos = {
        
        'id' : id,
        'cuenta' : cuenta,
        'categoria' : categoria,
        'motivos' : motivos,
        'submotivos' : submotivos,
        'solucion' : solucion,
        'motivoCliente' : motivoCliente,
        'comentarios':comentarios,
        'estado':estado,
        'cve_usuario' : cve_usuario,
        'casoNegocio' : casoNegocio,
        'fechaCompletado' : fechaCompletado,
        'fechaCaptura' : fechaCaptura,
        'status' : status,
        'procesando' : procesando,
        'ip' : ip,
        
        }         
    parametros = {"id":id}             
    return update(datos, parametros)

