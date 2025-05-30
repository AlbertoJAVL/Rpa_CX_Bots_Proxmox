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


#region URL

# url = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/getOrden'
# urlCN = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/saveCN'
# urlOrden = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/updateOrden' #update ext
# user = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/getOrdenUserCC'
url_space ="https://api.ocr.space/parse/image"
#endregion

url = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/getCuentaDepuracionBasesCanceladasEXT'
urlCN = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/ActualizaDepuracionBasesCanceladasEXT'
urlOrden = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/ActualizaDepuracionBasesCanceladasCC' #update ext
user = 'https://rpabackizzi.azurewebsites.net/EjecucionDepuracion/getCuentaDepuracionBasesCanceladasCC'
urlPassWord = 'https://rpabackizzi.azurewebsites.net/Bots/getProcess?ip='+str(ip)


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
        response = requests.get(urlPassWord) 
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

#endregion

# apiresponse = get_orden_servicio()                
# info = apiresponse
# print(info)


def update(datos,parametros):

    try:
        response = requests.put(urlOrden,params=parametros,json=datos,verify=False)
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

def orden_cerrada(id,id_lead,comentarios,compania,estado,hub,motivoOrden,nodo,cuenta,numOrden,tipo,cn_generado,fechaCierre,fechaCompletado,fechaCarga,fechaCreado,cve_usuario,status,procesando,ip,source_id):
    datos = {
        "id": id,
        "lead_id": id_lead,
        "comentarios": comentarios,
        "compania": compania,
        "estado": estado,
        "hub": hub,
        "motivoOrden": motivoOrden,
        "nodo": nodo,
        "cuenta": cuenta,
        "numOrden": numOrden,
        "tipo":tipo,
        "cn_generado": cn_generado,
        "fechaHoraCierre": fechaCierre,
        "fechaCompletado": fechaCompletado,
        "fechaCarga": fechaCarga,
        "fechaCreado": fechaCreado,
        "cve_usuario": cve_usuario,
        "status": status,
        "procesando": procesando,
        "ip": ip,
        "source": source_id
        }            
    parametros = {"id":id}          
    return update(datos,parametros)

def cuenta_erronea(id_lead,source_id):
    datos = {
         "id": 0,
        "lead_id": 0,
        "comentarios": "string",
        "compania": "string",
        "estado": "string",
        "hub": "string",
        "motivoOrden": "string",
        "nodo": "string",
        "cuenta": "string",
        "numOrden": "string",
        "tipo": "string",
        "cn_generado": "string",
        "fechaHoraCierre": "2023-06-29T19:50:42.440Z",
        "fechaCompletado": "2023-06-29T19:50:42.441Z",
        "fechaCarga": "2023-06-29T19:50:42.441Z",
        "fechaCreado": "2023-06-29T19:50:42.441Z",
        "cve_usuario": "string",
        "status": "string",
        "procesando": "string",
        "ip": "string",
        "source": "string"
        }                     
    return update(datos)

def cuenta_trabaja_izzi(id_lead,source_id):
    datos = {
         "id": 0,
        "lead_id": 0,
        "comentarios": "string",
        "compania": "string",
        "estado": "string",
        "hub": "string",
        "motivoOrden": "string",
        "nodo": "string",
        "cuenta": "string",
        "numOrden": "string",
        "tipo": "string",
        "cn_generado": "string",
        "fechaHoraCierre": "2023-06-29T19:50:42.440Z",
        "fechaCompletado": "2023-06-29T19:50:42.441Z",
        "fechaCarga": "2023-06-29T19:50:42.441Z",
        "fechaCreado": "2023-06-29T19:50:42.441Z",
        "cve_usuario": "string",
        "status": "string",
        "procesando": "string",
        "ip": "string",
        "source": "string"
        }                      
    return update(datos)




#region Caso de Negocio Apis

def update_cn(datos):

    try:
        response = requests.put(urlCN, data=datos)
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

def caso_negocio_cerrado(id_lead,source_id,cn):
    datos = {
         "id": 0,
        "lead_id": 0,
        "comentarios": "string",
        "compania": "string",
        "estado": "string",
        "hub": "string",
        "motivoOrden": "string",
        "nodo": "string",
        "cuenta": "string",
        "numOrden": "string",
        "tipo": "string",
        "cn_generado": "string",
        "fechaHoraCierre": "2023-06-29T19:50:42.440Z",
        "fechaCompletado": "2023-06-29T19:50:42.441Z",
        "fechaCarga": "2023-06-29T19:50:42.441Z",
        "fechaCreado": "2023-06-29T19:50:42.441Z",
        "cve_usuario": "string",
        "status": "string",
        "procesando": "string",
        "ip": "string",
        "source": "string"
        }                      
    return update_cn(datos)

def caso_negocio_existe(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "cn_generado":'cn_existente',
        "error": True,
        "code": 2
        }                      
    return update_cn(datos)

#endregion 





#region Api Space


# imagenesRuta = 'Screenshot/captura.jpg'
# listaArchivos = glob.glob(imagenesRuta) # * means all if need specific format then *.csv
# ultimoArchivo = max(listaArchivos, key=os.path.getctime)

# img = cv2.imread(ultimoArchivo)

# peticio = requests.post(url_space, 
#                         files = {img, file_bytes},
#                         data = {"apiKey":"563815dbb488957"
# )
#endregion 