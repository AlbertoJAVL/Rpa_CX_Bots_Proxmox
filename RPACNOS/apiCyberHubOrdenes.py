from json.decoder import JSONDecodeError
import requests
import json
from time import sleep
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


url = 'https://rpabackizzi.azurewebsites.net/okcliente/getCuentaOkCliente'
urlUpdate = 'https://rpabackizzi.azurewebsites.net/okcliente/ActualizaOkCliente'

def get_orden_servicio():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            responseApi = json.loads(response.text)
            print('API CORRECTA')
            print(responseApi)
            return responseApi
        elif response.status_code == 401: return print("Anauthorized")
        elif response.status_code == 404: return print("Not Found")
        elif response.status_code == 500: return print("Internal Server Error")
        
    except JSONDecodeError: return response.body_not_json

def update(datos, parametros):

    try:
        response = requests.put(urlUpdate, params=parametros, json=datos, verify=False)
        if response.status_code == 200:
            responseApi = json.loads(response.text)
            print('ACTUALIZADO')
            return responseApi
        
        elif response.status_code == 401: return print("Anauthorized")
        elif response.status_code == 404: return print("Not Found")
        elif response.status_code == 500: return print("Internal Server Error")

    except JSONDecodeError: return response.body_not_json

def ajusteCerrado(id, cnGenerado, fechaCaptura, fechaCompletado, status, cve_usuario, ip, cuenta, numeroOrden, hub, tipoOferta, fechaEncuesta, nombre, telefono):
    datos = {
        'id' : id,
        'cnGenerado' : cnGenerado,
        'fechaCaptura' : fechaCaptura,
        'fechaCompletado' : fechaCompletado,
        'status' : status,
        'cve_usuario' : cve_usuario,
        'ip' : ip,
        'cuenta' : cuenta,
        'numeroOrden' : numeroOrden,
        'hub' : hub,
        'tipoOferta' : tipoOferta,
        'fechaEncuesta' : fechaEncuesta,
        'nombre' : nombre,
        'telefono' : telefono
    }

    parametros = { 'id' : id }
    return update(datos, parametros)


# apiResponse = get_orden_servicio()
# info = apiResponse[0]
# status = 'Registro Pendiente'
# resultado = '-'
# ajusteCerrado(info['id'],resultado,info['fechaCaptura'],info['fechaCompletado'],status,info['cve_usuario'],ip,info['cuenta'],info['numeroOrden'], info['hub'], info['tipoOferta'], info['fechaEncuesta'], info['nombre'], info['telefono'])
# p = get_orden_servicio()
# print(p)