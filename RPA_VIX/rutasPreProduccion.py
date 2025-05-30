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
                                'xpath': '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[2]/a',
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
                        'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[7]/div/input',
                        },
                'subtipo_cuenta':{
                                'id': '',
                                'name':'s_12_1_65_0',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div/input'
                },
                'tipo_cuenta':{
                                'id': '',
                                'name':'s_12_1_193_0',
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[9]/div/input'
                },
                'antiguedad':{
                                'id': '',
                                'name':'s_12_1_36_0', 
                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[13]/td[3]/div/input'
                },
                'estado_cuenta':{

                                'xpath':'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[9]/td[9]/div/input'
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
        #Pantalla unica consulta
        'busquedaCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[2]',
        'nuevo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[1]',
        'categoria' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[3]',
        'motivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
        'subMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]',
        'solucion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
        'motivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[18]',
        'comentarios' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[12]',
        'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]',
        'guardar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[1]/div[3]/button[1]',
        'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[2]',
        'resultadoFecha' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[11]',
        'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/span[1]/span/button',
        'opcOrdenar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[34]/a',
        'ordenarPor' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]',
        'descendiente' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td[3]/input[2]',
        'btnAceptar' : '/html/body/div[21]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[1]/button',
        'guardarCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[1]/div[3]/button[1]',

        'cnCategoria' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[3]',
        'cnMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[3]',
        'cnSubMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[3]',
        'cnSolucion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[3]',
        'cnComentario' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[12]',
        'cnMotivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[5]',
        'cnEstado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]',
        'cnMotivoCierre' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[5]',
        'numroCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[6]/div/span/div',


        #Pantalla Casos de Negocio
        'opcCN' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[8]/a',
        'busqueda' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[2]',
        'inputCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]/input',
        'profCasoNegocio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/a',
        'masInformacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/ul/li[1]/a'
}

pantalla_consultad = {

        'subTipo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div/input',
        'busquedaSolicitudAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[1]/div[2]/button[2]',
        'inputMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
        'inputEstadoAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
        'elemBuscado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'elemHistorialAjustes' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
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
        'consultaSaldo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/div/form/div/span/div[1]/div[3]/button[8]',
        'busquedaCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[2]',
        'motivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[18]/input',
        'existente' :'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
        'fechaAjusteBusqueda' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]',
        'fechaPagoAplicado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/input',
        'numAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/div/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/span/input',
        'inputBusquedaAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]'
}


solicitud_ajuste = {
        'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[1]/div[2]/button[2]',
        'motivoAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
        'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[1]/div[2]/button[2]',
        'opcOrdenar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[34]/a',
        'ordenarPor' : '/html/body/div[20]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input',
        'descendiente' : '/html/body/div[20]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/input[2]',
        'btnAceptar' : '/html/body/div[20]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[1]/button',
        'inputBusquedaAjuste' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/input',
        'aceptarEnvio' : '/html/body/div[16]/div[2]/div/div/div/form/table/tbody/tr/td/span/span[1]/button',
        'fechaAjusteValidacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]'

}

historial_ajustes = {
        'fecha' :'/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]'
}

#/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[3]/div[4]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[10]/td[6]
#