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
                                'xpath': '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[2]/a', 
                            },

                    'lupa': {
                                'id': 's_12_1_148_0_Ctrl',
                                'name': 's_12_1_148_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[1]/div[3]/button[6]',
                            },
                    'ingresar_cuenta':{
                                'id': '',
                                'name': 's_12_1_154_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[4]/div',
                            },
                    'saldo_pendiente': {
                                'id': '',
                                'name': 's_12_1_32_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[7]/div/input',
                            },

                    }

ordenes_servicio = {
    'OS' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[6]/a',
    'lupa' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[1]/div[2]/button[3]',
    'nOrden' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/input',
    'enlaceOrden' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/span/div/div[3]/div/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/a',
    'fechaSolicitada' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[12]/div/input',
    'tipo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[8]/div/input',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[9]/div',
    'motivoCancelacion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[9]/div',
    'subEstado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[9]/td[9]/div',
    'comentario' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[1]/div/form/div/span/div[3]/div/div/table/tbody/tr[11]/td[7]/div'
}

caso_negocio = {
    'crear' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[1]',
    'categoria' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[3]/div',
    'motivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[3]/div',
    'subMotivo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[3]/div',
    'solucion' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[3]/div',
    'motivoCliente' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[5]/div',
    'motivoCierre' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[5]/div',
    'comentario' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[12]/div',
    'estado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div',
    'menuEstado' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/span',
    'opcCerrado' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[7]/div',
    'opcAbierto' : '/html/body/div[1]/div/div[5]/div/div[8]/ul[16]/li[1]/div',
    'guardar' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[1]/div[3]/button[1]',
    'cnNuevo' : '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[6]/div/input'
}