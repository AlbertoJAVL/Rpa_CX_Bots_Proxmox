import apiCyberHubOrdenes as api

datos = api.get_orden_servicio()
datos = datos[0]
api.ajusteCerrado(datos['id'], '-', datos['fechaCaptura'], datos['fechaCompletado'], 'Registro Pendiente', datos['cve_usuario'], 'Prueba', datos['cuenta'], datos['numeroOrden'])