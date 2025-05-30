import requests
import json
import os 
import autoit as a
from json.decoder import JSONDecodeError
from tkinter import messagebox as MessageBox
from time import sleep
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


#region URL
url = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/getCuentaDepuracionBasesCanceladasEXT'
urlOrdenExt = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/ActualizaDepuracionBasesCanceladasEXT'
urlOrden = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/ActualizaDepuracionBasesCanceladasCC' #update ext
user = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/getCuentaDepuracionBasesCanceladasCC'
urlPassUser = 'https://rpabackizzi.azurewebsites.net/Bots/getProcess?ip='+str(ip)
#endregion




#region Datos
def usuario():
    flag = True
    while flag == True:
        a = get_data_user()
        print('respuesta de API: ',a)
        if a['info'] == 'sin_info':
            print('Esperando...')
            sleep(5)
            flag == True

        else:
            print('Orden recibida')
            flag == False
            user = a['access_data']
            print('user',user)
            return user

def get_data_user():
    try:
        response = requests.get(user) 
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
    
def get_data_user2():
    try:
        response = requests.get(urlPassUser) 
        if response.status_code == 200:
            reseponseApi = json.loads(response.text)
            print(reseponseApi)
            return reseponseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
        return response.body_not_json
        

def get_orden_servicio():
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

#endregion

# apiresponse = get_orden_servicio()                
# info = apiresponse
# print(info)


def update(datos,parametros):

    try:
        response = requests.put(urlOrdenExt,params=parametros,json=datos,verify=False)
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

def orden_cerrada(id,id_lead,cuenta,compania,numOrden,tipo,motivoOrden,fechatecnico,comentarios,hub,rpt,region,responde,transferir,nombrecontacto,comentariosCyber,nodo,source_id,fechaCarga,status,fechaCierre,cn_generado,usuarioCreo,usuarioRegistro,procesando,fechaCompletado,fechaCreado,cve_usuario,ip):
    datos = {
        "id": id,
        "lead_id": id_lead,
        "cuenta": cuenta,
        "compania": compania,
        "numOrden": numOrden,
        "tipo":tipo,
        "motivoOrden": motivoOrden,
        "fechaTecnico": fechatecnico,
        "comentarios": comentarios,
        "hub": hub,
        "rpt": rpt,
        "region":region,
        "quienResponde": responde,
        "transferir": transferir,
        "nombreContacto": nombrecontacto,
        "comentariosCyber": comentariosCyber,
        "nodo": nodo,
        "source": source_id,
        "time_carga": fechaCarga,
        "status": status,
        "fechaHoraCierre": fechaCierre,
        "cn_generado": cn_generado,
        "usuario_creo": usuarioCreo,
        "user_registro": usuarioRegistro,
        "procesando": procesando,
        "fechaCompletado": fechaCompletado,
        "fechaCreado": fechaCreado,
        "cve_usuario": cve_usuario,
        "ip": ip
        
        
       
        }            
    parametros = {"id":id}          
    return update(datos,parametros)




