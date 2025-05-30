import requests
import json
import os 
from json.decoder import JSONDecodeError
from time import sleep
import socket


hostname= socket.gethostname()
ip = socket.gethostbyname(hostname)



#region URL

url = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/getCuentaCreacionOrdenes'
urlOrden = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/ActualizaCreacionOrden'
urlMeses = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/getAjustesTiempoAjuste'
#url_space ="https://api.ocr.space/parse/image"
#endregion
urlPassUser = 'https://rpabackizzi.azurewebsites.net/Bots/getProcess?ip='+str(ip)





'''OBTIENE LA ORDEN DE SERVICIO
Recibe: 
        NADA
Entrega:
        Un código de respuesta o los datos de una orden

'''
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
    
def get_orden_servicio():
    try:
        response = requests.get(url) 
        if response.status_code == 200:
            reseponseApi = json.loads(response.text)
            print('API correcta')
            return reseponseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
        return response.body_not_json

p = get_user()
print(p)

def get_tiempo_ajuste():
    try:
        response = requests.get(urlMeses) 
        if response.status_code == 200:
            reseponseApi = json.loads(response.text)
            print('API correcta')
            return reseponseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
        return response.body_not_json



'''ACTUALIZACIÓN DE DATOS DE
Recibe:  
        Datos (previamente estructurados)
Devuelve:
        Un código de respuesta
'''

def update(datos, parametros):

    try:
        response = requests.put(urlOrden, params=parametros, json=datos, verify=False)
        if response.status_code == 200:
            responseApi = json.loads(response.text)
            print('Actualizado')
            return responseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
            return response.body_not_json


# apiRequest = get_orden_servicio()
# print(apiRequest)
# info = apiRequest[0]
# print(info)

'''CUANDO A UNA ORDEN SE LE HACE EL PROCESO
Recibe: 
        id_lead(INTEGER) & source_id (STRING)
Devuelve: 
        Llama a UPDATE para actualizar los datos en la base
'''

def ajusteCerrado(id, casoNegocio, categoria, cuenta, estado, fechaApertura, mediosContacto, motivoCliente, motivos, solucion, submotivo, cve_usuario, fechaCompletado, fechaCaptura, status, procesando, ip, numAjuste, CNGenerado, statusCNGenerado, statusAjuste):
    datos = {
        
        'id' : id,
        'casoNegocio' : casoNegocio,
        'categoria' : categoria,
        'cuenta' : cuenta,
        'estado' : estado,
        'fechaApertura' : fechaApertura,
        'mediosContacto' : mediosContacto,
        'motivoCliente' : motivoCliente,
        'motivos' : motivos,
        'solucion' : solucion,
        'submotivo' : submotivo,
        'cve_usuario' : cve_usuario,
        'fechaCompletado' : fechaCompletado,
        'fechaCaptura' : fechaCaptura,
        'status' : status,
        'procesando' : procesando,
        'ip' : ip,
        'numeroOrden' : numAjuste,
        'cnGenerado' : CNGenerado,
        'statusNegocioGenerado' : statusCNGenerado,
        'estatusOrden' : statusAjuste

        }

    parametros = { 'id' : id }
    return update(datos, parametros)

# apiRequest = get_orden_servicio()
# info = apiRequest[0]
# print(info)
# ajusteCerrado(info['id'],info['casoNegocio'],info['categoria'],info['cuenta'],info['estado'],info['fechaApertura'],info['mediosContacto'],info['motivoCliente'],info['motivos'],info['solucion'],info['submotivo'],info['cve_usuario'],info['fechaCompletado'],info['fechaCaptura'],'No Aplica por producto nuevo', '1', 'vix10-PC', '1-162884197233', '', '', 'Cancelado')

'''LA CUENTA NO COINCIDE CON LA DE SEIEBEL
Recibe: 
        id_lead(INTEGER) & source_id (STRING)
Devuelve: 
        Llama a UPDATE para actualizar los datos en la base
'''

def cuenta_erronea(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 3
        }                     
    return update(datos)


'''CUANDO A UNA ORDEN SE LE HACE EL PROCESO
Recibe: 
        id_lead(INTEGER) & source_id (STRING)
Devuelve: 
        Llama a UPDATE para actualizar los datos en la base
'''

def cuenta_trabaja_izzi(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 4
        }                      
    return update(datos)

'''CUANDO NO COINCIDENTE CON LA DE SIEBEL
Recibe: 
        id_lead(INTEGER) & source_id (STRING)
Devuelve: 
        Llama a UPDATE para actualizar los datos en la base
'''

def cuenta_errorsiebel(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 5
        }                      
    return update(datos)

'''API SIN DATOS
Recibe: 
        id_lead(INTEGER) & source_id (STRING)
Devuelve: 
        Llama a UPDATE para actualizar los datos en la base
'''

def api_sin_datos():
    datos = {
            "lead_id":0,
            "error": False,
            "code": 4}                       
    return update(datos)

#------------------------------------------------------------------
''' ACTUALIZA DATOS DEL CASO DE NEGOCIO
Recibe: 
        datos (previamente estructurados)
Devuelve: 
        Llama a UPDATE para actualizar los datos en la base
'''
