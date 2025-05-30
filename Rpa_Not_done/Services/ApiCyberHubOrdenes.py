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

url = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/getCuentaEjecucionNotDone'
urlOrden = 'https://rpabackizzi.azurewebsites.net/AjustesNotDone/ActualizaEjecucionNotDone'
user = 'https://rpabackizzi.azurewebsites.net//Bots/getProcess?ip='+str (ip)




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

# info = apiresponse[0]
# # nOrden = info['numeroOrden']
# # cuenta = info['cuenta']
# print(info)
# print(nOrden, cuenta)

# datosSR = info['parametrosExtraccion']

# print(datosSR)

#endregion


#region Orden de Servicio 

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

def notDone_cerrado(id, ciudad, comentarios, creadoPor, cuenta, direccion, estadoOrden, fechaApertura, fechaSolicitada, hub, motivoCancelacion, motivoOrden, motivoReprogramacion, nombreCliente, numeroOrden, numRepro, paquete, perfilPago, plaza, referido, rpt, situacionAnticipo, subtipoCliente, subtipoOrden, tecnico, telefono, tipCliente, tipoOrden, ultimaModificacionPor, vendedor, cve_usuario, fechaCompletado, fechaCaptura, status, procesando, ip, nuevoCN, statusNCN, resultadoLlamada, clasificacionOrden):
    datos = {
        
        'id' : id,
        'ciudad' : ciudad,
        'comentarios' : comentarios,
        'creadoPor' : creadoPor,
        'cuenta' : cuenta,
        'direccion' : direccion,
        'estadoOrden' : estadoOrden,
        'fechaApertura' : fechaApertura,
        'fechaSolicitada' : fechaSolicitada,
        'hub' : hub,
        'motivoCancelacion' : motivoCancelacion,
        'motivoOrden' : motivoOrden,
        'motivoReprogramacion' : motivoReprogramacion,
        'nombreCliente' : nombreCliente,
        'numeroOrden' : numeroOrden,
        'numRepro' : numRepro,
        'paquete' : paquete,
        'perfilPago' : perfilPago,
        'plaza' : plaza,
        'referido' : referido,
        'rpt' : rpt,
        'situacionAnticipo' : situacionAnticipo,
        'subtipoCliente' : subtipoCliente,
        'subtipoOrden' : subtipoOrden,
        'tecnico' : tecnico,
        'telefono' : telefono,
        'tipCliente' : tipCliente,
        'tipoOrden' : tipoOrden,
        'ultimaModificacionPor' : ultimaModificacionPor,
        'vendedor' : vendedor,
        'cve_usuario' : cve_usuario,
        'fechaCompletado' : fechaCompletado,
        'fechaCaptura' : fechaCaptura,
        'status' : status,
        'procesando' : procesando,
        'ip' : ip,
        'casoNegocio' : nuevoCN,
        'statusCasoNegocio' : statusNCN,
        'resultadoLlamada' : resultadoLlamada,
        'clasificacionOrden' : clasificacionOrden

        }         
    parametros = {"id":id}             
    return update(datos, parametros)

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