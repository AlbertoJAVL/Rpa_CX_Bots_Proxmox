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


url = 'https://rpabackizzi.azurewebsites.net/Reporte/getCuentaExtraccionAutomatizadas2prueba'
urlOrden = 'https://rpabackizzi.azurewebsites.net/Reporte/ActualizaEjecucionExtraccionAutomatizados2Prueba'
urlHorario = 'https://rpabackizzi.azurewebsites.net/Reporte/getExtraccionAutomatizadosAsc'
urlUpdateExtraccion = 'https://rpabackizzi.azurewebsites.net/Reporte/GuardarFormularioEjecucionExtraccionAutomatizados2'
urlUsrPass = 'https://rpabackizzi.azurewebsites.net/Bots/getProcess?ip='+str(ip)

urlCN = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/saveCN'
# urlOrden = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/updateOrden'
user = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/getOrdenUserExt'
#url_space ="https://api.ocr.space/parse/image"
#endregion


def get_data_user2():
    try:
        response = requests.get(urlUsrPass) 
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



def get_extraccion():
    try:
        response = requests.get(url, verify=False) 
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

# apiresponse = get_extraccion()          

# info = apiresponse[0]

# # datosSR = info['parametrosExtraccion']

# print(info)

#endregion


#region Orden de Servicio 

def post_extraccion(datos, parametros):
    try:
        response = requests.put(urlUpdateExtraccion, params=parametros, json=datos, verify=False)
        print(response.status_code)
        if response.status_code == 200:
            responseApi = json.loads(response.text)
            return responseApi
        elif response.status_code == 401:
            return print('Unauthorized')
        elif response.status_code == 404:
            return print('Not Found')
        elif response.status_code == 500:
            return print('Internal Server Error ')
    
    except JSONDecodeError:
        return response.body_not_json


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

def extraccion_cerrada(id, tipoExtraccion, fechaExtraccion, parametrosExtraccion, archivo, cve_usuario, fechaCompletado, status, ip, horaProgramacion, nombreCron, scheduleExpression, tipoProgramacion, correo, medioExtraccion, proceso):
    datos = {
        "id":id,
        "tipoExtraccion":tipoExtraccion,
        "fechaExtraccion": fechaExtraccion,
        "parametrosExtraccion": parametrosExtraccion,
        "archivo":archivo,
        "cve_usuario":cve_usuario,
        "fechaCompletado":fechaCompletado,
        "status":status,
        "procesando" : "1",
        "ip" : ip,
        'horaProgramacion':horaProgramacion,
        "nombreCron" :  nombreCron,
        "scheduleExpression" : scheduleExpression,
        "tipoProgramacion" : tipoProgramacion,
        "correo": correo,
        "medioExtraccion": medioExtraccion,
        'proceso' : proceso
        }

    parametros = { 'id' : id }      
                
    return update(datos, parametros)

# p = extraccion_cerrada(1, 'tipoExtraccion', 'fechaExtraccion', 'parametrosExtraccion', 'archivo', 'cve_usuario', '2023-08-27 12:00:00', 'status', 'ip', 'horaProgramacion', 'nombreCron', 'scheduleExpression', '1')
# print(p)

def cuenta_erronea(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 3
        }                     
    return update(datos)

def cuenta_trabaja_izzi(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 4
        }                      
    return update(datos)

def cuenta_errorsiebel(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 5
        }                      
    return update(datos)

def api_sin_datos():
    datos = {
            "lead_id":0,
            "error": False,
            "code": 4}                       
    return update(datos)
#endregion


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
        "source_id":source_id,
        "lead_id":id_lead,
        "cn_generado":cn,
        "error": False,
        "code": 1
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