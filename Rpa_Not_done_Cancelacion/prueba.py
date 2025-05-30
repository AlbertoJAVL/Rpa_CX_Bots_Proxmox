import os
import datetime 
import ftplib
import pandas as pd
from extraccion import *
import Services.ApiCyberHubOrdenes as api


# # datos = "estado":"Abierta","tipoOrden":"((( = "Trouble Call Cablemodem" OR = "Trouble Call Video") OR = "Trouble Call Telefonia"))

# # datos = '[{"estado":"Abierta","tipoOrden":"((( = "Trouble Call Cablemodem" OR = "Trouble Call Video") OR = "Trouble Call Telefonia"))","motivo":"Normal","areaConocimiento":"","fechaAsignacion":">=\'04/04/2023 06:00:00\' AND <= \'04/04/2023 11:00:00\'"}]'
# datos = '[{"estado":"Abierta","areaConocimiento":"","fechaAsignacion":">=\'04/04/2023 06:00:00\' AND <= \'04/04/2023 11:00:00\'"}]'
# # # datos = '[{"estado":"Abierta","tipo":"","subTipo":">=\'04/04/2023 06:00:00\' AND <= \'04/04/2023 11:00:00\'"}]'
# # datos = '[{"estado":"Abierta","numCaso":"12234","cuenta":"12345","categoria":"cat","motivo":"mot","subMotivo":"sub","solucion":"sol"}]'
# tExtraccion = 'Actividades'
# datosF = separacionParametrosExtraccion(datos, tExtraccion)
# print('Estado: ' + datosF['estado'])
# # # print('tipoOrden: ' + datosF['tipoOrden'])
# # # print('motivo: ' + datosF['motivo'])
# print('areaConocimiento: ' + datosF['areaConocimiento'])
# print('fechaAsignacion: ' + datosF['fechaAsignacion'])
# # print('areaConocimiento: ' + datosF['numCaso'])
# print('fechaAsignacion: ' + datosF['cuenta'])
# print('areaConocimiento: ' + datosF['categoria'])
# print('fechaAsignacion: ' + datosF['motivo'])
# print('areaConocimiento: ' + datosF['subMotivo'])
# print('fechaAsignacion: ' + datosF['solucion'])

apiresponse = api.get_extraccion()             
info = apiresponse[0]
tExtraccion = info['tipoExtraccion']
print(tExtraccion)
datosSR = info['parametrosExtraccion']
print(datosSR)
datos = separacionParametrosExtraccion(datosSR, tExtraccion)
print(datos)
# print(datos)