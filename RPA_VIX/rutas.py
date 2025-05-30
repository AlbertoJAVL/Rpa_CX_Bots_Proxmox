import json

fechasInput = [
        '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]'
]

home = {
        'actividades': {
                'id': '',
                'name': '',
                'xpath': '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[4]',
        },
        'pantalla_unica':{
                                'id': '',
                                'name': '',
                                'xpath': '//*[@id="s_sctrl_tabScreen"]/ul/li[2]',
        },
        'home_from_sidebar': {
                'id': 'ui-id-159',
                'name': '',
                'xpath': '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[1]/a',
                
        },
        'pantalla_casos':{
                'id': '',
                'name': '',
                'xpath': '//*[@id="s_sctrl_tabScreen"]/ul/li[8]',
                },
        }
pantalla_casos_negocio = {
                        'lupa':{
                                'id':'',
                                'name':'s_2_1_13_0',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[2]'
                        },
                        'ingresar_caso':{
                                'id':'',
                                'name':'SR_Number',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/input'
                        },
                        'motivo_cliente':{
                                'id':'',
                                'name':'TT_Motivo_Cliente',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[26]/input'
                        },
                        
                        'barra_caso_negocio':{
                                'id':'',
                                'name':'SR_Number',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/input'
                        },
                        }

pantalla_unica = {
                'lupa': {
                        'id': 's_12_1_148_0_Ctrl',
                        'name': 's_12_1_148_0',
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[1]/div[3]/button[6]',
                        },      
                'lupa_caso_negocio': {
                                'id': '',
                                'name': 's_1_1_18_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/span/div/div[1]/div[2]/button[2]'
                                         
                        },
                'ingresar_cuenta':{
                        'id': '',
                        'name': 's_12_1_154_0',
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[4]/div/input',
                        },
                'saldo_pendiente': {
                        'id': '',
                        'name': 's_12_1_32_0',
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[7]/div/input',
                        'xpath2': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[7]/div/input'
                        },
                'saldo_total' : {
                        'xpath' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[7]/div/input'
                },
                'subtipo_cuenta':{
                                'id': '',
                                'name':'s_12_1_65_0',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div/input',
                                'xpath2':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div/input'
                },
                'tipo_cuenta':{
                                'id': '',
                                'name':'s_12_1_193_0',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[9]/div/input',
                                'xpath2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[9]/div/input'
                },
                'antiguedad':{
                                'id': '',
                                'name':'s_12_1_36_0', 
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[13]/td[3]/div/input'
                },
                'estado_cuenta':{

                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[9]/td[9]/div/input',
                                'xpath2':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[9]/td[9]/div/input'
                },                
                'sub_estado_cuenta':{
                                'id': '',
                                'name':'s_12_1_111_0',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[11]/td[9]/div/input'
                },
                'ingresar_caso':{
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/input'
                },
                'historial_facturas':{
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[1]'
                },
                'factura_actual':{
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a'
                },
                'detalles': {
                        'xpath':'//*[@id="a_2"]/div[1]'
                },                
                'profundiza_caso': {
                        'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a]'
                },
                'profundiza_actividades':{
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/ul/li[2]'
                },
                'profundiza_actividad_id': {
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[1]'
                },
                'estado_caso':{
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[8]/div/input'
                },
                'otrosSaldos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[7]/div/span',
                'saldo30Dias' : '/html/body/div[21]/div[2]/div/div/div/table[2]/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/span/input',
                'saldo60Dias' : '/html/body/div[21]/div[2]/div/div/div/table[2]/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[2]/span/input'
        }

pInicio = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[2]/a'

casos_negocio = {

        'columnas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
        'columnasAct' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
        'filas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]',
        'filasAct' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]',
        'inputEstado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/input',
        'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span',
        'opciones' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[{contador}]/div',
        'numeroCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a',
        'actividades' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/ul/li[2]/a',
        'casillaEstado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]/span',
        'estadoCerrado' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[12]/li[{contador}]/div',
        'motivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[5]/div/span',
        'opcionesMC' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[17]/li[{contador}]/div',
        'motivoCierre' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[5]/div/span',
        'opcionesMCC' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[18]/li[{contador}]/div'

}

pantalla_consultad = {

        'subTipo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div/input',
        'busquedaSolicitudAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[1]/div[2]/button[2]',
        'inputMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]',
        'elemBuscado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
        'elemHistorialAjustes' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]/input',
        'engraneHistorialPagos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[1]/div[2]/span[1]/span/button',
        'opcOrdenar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[34]/a',
        'ordenarPor' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input',
        'descendiente' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/input[2]',
        'btnAceptar' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[1]/button',
        'opcColumnasMostradas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[33]/a',
        'opcImportePago' : '/html/body/div[11]/div[2]/div/div/div/form/table[1]/tbody/tr[2]/td[1]/select/option[2]',
        'agregarOpc' : '/html/body/div[11]/div[2]/div/div/div/form/table[1]/tbody/tr[2]/td[2]/span[1]/span/a',
        'btnGuardar' : '/html/body/div[11]/div[2]/div/div/div/form/table[2]/tbody/tr/td/span[2]/button',
        'montoPagado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[10]',
        'saldoVencido' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[7]/div/input',
        'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[9]/td[9]/div/input',
        'crearAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[1]/div[2]/button[1]',
        'importe' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]',
        'aplicar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]',
        'motivoAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[4]/td[2]',
        'comentarios' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]',
        'fechaAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/span/input',
        'guardarAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[1]/tbody/tr/td[1]/span/div/div[3]/button[1]',
        'enviar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[2]/div[1]/button',
        'aceptar' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr/td/span/span[1]/button',
        'consultaSaldo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[1]/div[3]/button[8]',
        'busquedaCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[2]',
        'motivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[18]/input',
        'existente' :'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'fechaAjusteBusqueda' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]',
        'fechaPagoAplicado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/input',
        'numAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/span/input'
}

solicitud_ajuste = {
        
        'columnas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
        'filas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]'
        
}

historial_ajustes = {
        'fecha' :'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]'
}

paginaInicialFelcha = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]'

historial_pagos = {
        'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[1]/div[2]/button[4]',
        'lupa2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[1]/div[2]/button[3]',
        'inputFecha' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'inputFechaCa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'inputStatus' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]',
        'inputStatusCa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]',
        'inputMonto' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
        'resultado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'resultadoCa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'opcColumnas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[33]/a',
        'montoColum' : '/html/body/div[21]/div[2]/div/div/div/form/table[1]/tbody/tr[2]/td[1]/select/option[2]',
        'asiganrColumn' : '/html/body/div[21]/div[2]/div/div/div/form/table[1]/tbody/tr[2]/td[2]/span[1]/span/a',
        'guardarColumn' : '/html/body/div[21]/div[2]/div/div/div/form/table[2]/tbody/tr/td/span[2]/button',
        'cerrarColumn': '/html/body/div[21]/div[2]/div/div/div/form/table[2]/tbody/tr/td/span[3]/button',
        'pago' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a',
        'pagoCa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a'
}


actualizacionDatos = {
        'opcPenalizacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/ul/li[10]/select/option[5]',
        'resumenCunta' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/ul/li[1]/a'

}


ordenes_servicio = {

        'opcEngrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]/a',
        'columnas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
        'filas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]',
        'ordenServicio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a',
        'ordenServicio2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[3]/td[2]/a',
        'referido' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[11]/td[5]/div/span',
        'portafolios' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{contador}]/td[3]',
        'precios' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[{contador}]/td[5]',
        'menuMotivosCancelacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[9]/div/span',
        'motivosCancelacion' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[3]/li[{contador}]/div',
        'menuEstatus' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div/span',
        'estados' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[5]/li[{contador}]/div',
        'columnasProductos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
        'filasProductos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]',
        'pantallaUnica' : '/html/body/div[1]/div/div[5]/div/div[8]/div[1]/div/div[3]/ul/li[1]/span/a'
        # 'opcReferido' : '',

}

itemProductos = {

        'items' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'regresoPantallaUnica' : '/html/body/div[1]/div/div[5]/div/div[8]/div[1]/div/div[3]/ul/li[1]/span/a',
        'productos' :'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/span'

}

penalizacion = {

        'opcEngrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[2]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]/a',
        'columnas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
        'filas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[{contador}]',
        'pestañas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/ul/li[{contador}]/a'

}


 # /html/body/div[1]/div/div[5]/div/div[8]/ul[3]/li[16]/div
# prueba = {
#         'columnaCasoNegocio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div'
# }