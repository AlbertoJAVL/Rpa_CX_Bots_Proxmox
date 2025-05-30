import os
import datetime 
import ftplib
import pandas as pd
from extraccion import *
import Services.ApiCyberHubOrdenes as api
from datetime import datetime, time, date


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

# apiresponse = api.get_extraccion()             
# info = apiresponse[0]
# tExtraccion = info['tipoExtraccion']
# print(tExtraccion)
# datosSR = info['parametrosExtraccion']
# print(datosSR)
# datos = separacionParametrosExtraccion(datosSR, tExtraccion)
# print(datos)
# # print(datos)

horaInicio = time(6,0,0)
horaFin = time(5,0,0)


fechaCaptura = '2023-08-08T08:04:22'
fechaCaptura = fechaCaptura.replace("T", " ")
fechaCaptura = datetime.strptime(fechaCaptura, "%Y-%m-%d %H:%M:%S")


fechaInicioRango = datetime.combine(fechaCaptura.date(), horaInicio)
fechaFinRango = datetime.combine((fechaCaptura + timedelta(days=1)).date(), horaFin)
print('Fecha inicio rango: ', str(fechaInicioRango))
print('Fecha fin rango: ', str(fechaFinRango))

if fechaInicioRango <= fechaCaptura <= fechaFinRango:
    print('ORden Dentro de horario')