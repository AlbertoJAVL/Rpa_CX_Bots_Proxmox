home = {
        'home_from_sidebar': {
                'id': '',
                'name': '',
                'xpath': '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[1]',
            },
}

pantalla_unica = {
                    'home': {
                                'id': '',
                                'name': '',
                                'xpath': '//*[@id="s_sctrl_tabScreen"]/ul/li[2]',
                            },

                    'lupa': {
                                'id': 's_12_1_148_0_Ctrl',
                                'name': 's_12_1_148_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[1]/div[3]/button[6]',
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
                            },

                    }

nuvasRutas = {
    'exportaciones' : "/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[{contador}]/a",
    'columnasCuentas' : "/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div",
    'columnasCasosNegocio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
    'columnasCasosNegocio2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
    'columnasActividades' : '/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
    'columnasActividades2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
    'columnasOrdenesServicio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
    'columnasOrdenesServicio2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[2]/div/table/thead/tr/th[{contador}]/div',
    'opcExportarCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]',
    'opcExportarAct' : '/html/body/div[1]/div/div[5]/div/div[8]/div/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]',
    'opcExportarAct2' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]',
    'opcExportarOS' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[{contador}]'
}

casos_negocio = {

    'extraccionCN' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[8]/a',
    'selectTodosCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]',
    'opcTodosCN' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]/select/option[2]',
    'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[2]',
    'casoNegocio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]',
    'cuenta' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]',
    'categoria' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
    'motivos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]',
    'subMotivos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
    'solucion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]',
    'fechaApertura' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[14]',
    'motivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[26]',
    'medioContacto' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[35]',
    'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/button',
    'opcExportar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[23]/a',
    'todos' : '/html/body/div[22]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input[1]',
    'delimitador' : '/html/body/div[22]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input[2]',
    'btnSiguiente' : '/html/body/div[22]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[2]/button',
    'btnCerrar' : '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[3]/button'
}

actividades = {

    'extracionActividades' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[4]/a',
    'selectTodosActividades' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]',
    'opcTodosActividades' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]/select/option[2]',
    'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[3]',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[11]',
    'areaConocimiento' :  '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[17]',
    'fechaCreacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[19]/td[5]/div/input',
    'fechaAsignacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[14]',
    'vencimiento' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[13]',
    'tipo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
    'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/button',
    'opcExportar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[23]/a',
    'todos' : '/html/body/div[24]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input[1]',
    'delimitador' : '/html/body/div[24]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input[2]',
    'btnSiguiente' : '/html/body/div[24]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[2]/button',
    'btnCerrar' : '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[3]/button'
}

cuentas = {
    'extraccionCuentas' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[3]/a',
    'selectTodosCuentas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]/select',
    'opcTodosCuentas' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[1]/select/option[1]',
    'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[3]',
    'tipo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
    'subTipo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
    'canalIngreso' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[7]/div/input',
    'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/form/span/div/div[1]/div[2]/span[1]/span/button',
    'opcExportar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[22]/a',
    'todos' : '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input[1]',
    'delimitador' : '/html/body/div[25]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input[2]',
    'btnSiguiente' : '/html/body/div[25]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[2]/button',
    'btnCerrar' : '/html/body/div[25]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[3]/button'
}

ordenes_servicio = {
    'extraccionOrdenesS' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[6]/a',
    'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[3]',
    'compañia' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[13]',
    'telefonos' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[15]',
    'nOrden' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
    'tipoOrden' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]',
    'fechaOrden' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[10]',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
    'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/button',
    'opcExportar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[23]/a',
    'todos' : '/html/body/div[18]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input[1]',
    'delimitador' : '/html/body/div[18]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input[2]',
    'btnSiguiente' : '/html/body/div[18]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[2]/button',
    'btnCerrar' : '/html/body/div[11]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[3]/button'
}

fallas_generales = {
    'extraccionFallasGenerales' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[10]/a',
    'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[2]',
    'vencimiento' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]',
    'fallaGeneralAsociada' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[3]/div/input',
    'categoria' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[5]',
    'motivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[6]',
    'subMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[7]',
    'solucion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]',
    'tecnologia' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[9]',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[10]',
    'hub' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[11]',
    'rama' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[12]',
    'nodo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[13]',
    'fiberDeep' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[14]',
    'fechaInicio' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[15]',
    'nombreHub' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[16]',
    'incidente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[17]',
    'nOrden' : '',
    'engrane' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/button',
    'opcExportar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/span[1]/span/ul/li[23]/a',
    'todos' : '/html/body/div[10]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input[1]',
    'delimitador' : '/html/body/div[10]/div[2]/div/div/div/form/table/tbody/tr[1]/td/table/tbody/tr/td/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input[2]',
    'btnSiguiente' : '/html/body/div[10]/div[2]/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr/td/span[2]/button'
}

pInicial = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[1]/a'


pagos = {
    
    'extraccionPagos' : '',

}