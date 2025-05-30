
#Falta matear las que se hciieron primero

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

caso_negocio = {
                    'lupa': {
                                'id': '',
                                'name': 's_1_1_19_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/span/div/div[1]/div[2]/button[1]',
                            },
                    'medio_contacto': {
                                'id': '',
                                'name': 's_13_1_4_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[3]/div/input'
                            },
                    'categoria': {
                                'id': '',
                                'name': 's_13_1_7_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[3]/div/input'
                            },
                    'motivo': {
                                'id': '',
                                'name': 's_13_1_6_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[5]/td[3]/div/input'
                            },
                    'sub_motivo': {
                                'id': '',
                                'name': 's_13_1_8_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[3]/div/input'
                            },
                    'solucion': {
                                'id': '',
                                'name': 's_13_1_10_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[7]/td[3]/div/input'
                            },
                    'numero_caso': {
                                'id': '',
                                'name': 's_13_1_11_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[6]/div/input'
                            },
                    'estado': {
                                'id': '',
                                'name': 's_13_1_12_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[4]/td[5]/div/input'
                            },
                    'motivo_cierre': {
                                'id': '',
                                'name': 's_13_1_18_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[6]/td[5]/div/input'
                            },
                    'comentarios': {
                                'id': '',
                                'name': 's_13_1_9_0',
                                'xpath': '/html/body/div[1]/div/div[5]/div/div[8]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[12]/div/textarea'
                            },



}

elementoExtraccion = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/ul/li[12]/a/span'
menuExtracciones = 's_sctrl_tabView_noop'

extraccionCuentas = {

    'cuentas':'/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[1]',
    
    'lupa' : {
        
        'xpath':'//*[@id="s_1_1_6_0_Ctrl"]',
        'id':'s_1_1_6_0_Ctrl',
        'name':'s_1_1_6_0'

    },


    ########################## ELEMENTOS DEL FRONT

    'status' : {
        
        'input' : '1_Account_Status',
        'elemento' : '1_s_1_l_Account_Status'
    },

    'tipo' : {
        
        'input' : '1_Type',
        'elemento' : '1_s_1_l_Type'
    },

    'subTipo' : {
        
        'input' : '1_CV_Account_Sub-Type',
        'elemento' : '1_s_1_l_CV_Account_Sub-Type'
    },
    'exportar':'//*[@id="s_at_m_1-menu"]/li[22]'

}

extraccionCN = {

    'cn' : '/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[4]',

    'lupa' : {
        
        'xpath':'//*[@id="s_1_1_10_0_Ctrl"]',
        'id':'s_1_1_10_0_Ctrl',
        'name':'s_1_1_10_0'

    },

    'inputCN' : '1_SR_Number',

    ########################## ELEMENTOS DEL FRONT

    'cuenta' : {
        
        'input' : '1_Account',
        'elemento' : '1_s_1_l_Account'
    },

    'estado' : {
        
        'input' : '1_Status',
        'elemento' : '1_s_1_l_Status'
    },

    'categoria' : {
        
        'input' : '1_SR_Type',
        'elemento' : '1_s_1_l_SR_Type'
    },
    
    'motivo' : {
        
        'input' : '1_Area',
        'elemento' : '1_s_1_l_Area'
    },

    'subMotivo' : {
        
        'input' : '1_Sub-Area',
        'elemento' : '1_s_1_l_Sub-Area'
    },

    'solucion' : {
        
        'input' : '1_Retention_Tools',
        'elemento' : '1_s_1_l_Retention_Tools'
    },
    'exportar':'//*[@id="s_at_m_1-menu"]/li[23]'
}

extraccionactividades = {

    'actividades' : '//*[@id="s_sctrl_tabView"]/ul/li[5]',

    'lupa' : {
        
        'xpath':'//*[@id="s_1_1_14_0_Ctrl"]',
        'id':'s_1_1_14_0_Ctrl',
        'name':'s_1_1_14_0'

    },
    

    ########################## ELEMENTOS DEL FRONT

    'estatus' : {
        
        'input' : '1_TT_Status',
        'elemento' : '1_s_1_l_TT_Status'
    },
    
    'areaCon' : {
        
        'input' : '1_TT_Backoffice_Expertise',
        'elemento' : '1_s_1_l_TT_Backoffice_Expertise'
    },
    
    'fAtencion' : {
        
        'input' : '1_TT_Assign_Date',
        'elemento' : '1_s_1_l_TT_Assign_Date'
    },
    'exportar':'//*[@id="s_at_m_1-menu"]/li[23]'

}

extraccionOS = {

    'OS' : '//*[@id="s_sctrl_tabView"]/ul/li[3]',

    'lupa' : {
        
        'xpath':'//*[@id="s_1_1_21_0_Ctrl"]',
        'id':'s_1_1_21_0_Ctrl',
        'name':'s_1_1_21_0'

    },


    ########################## ELEMENTOS DEL FRONT
    'tOrden' : {
        
        'input' : '1_Order_Type',
        'elemento' : '1_s_1_l_Order_Type'
    },

    'motivo' : {
        
        'input' : '1_CV_Order_Reason',
        'elemento' : '1_s_1_l_CV_Order_Reason'
    },

    'estado' : {
        
        'input' : '1_Status',
        'elemento' : '1_s_1_l_Status'
    },

    'fOrden' : {
        
        'input' : '1_Order_Date',
        'elemento' : '1_s_1_l_Order_Date'
    },
    'exportar':'//*[@id="s_at_m_1-menu"]/li[23]'

}