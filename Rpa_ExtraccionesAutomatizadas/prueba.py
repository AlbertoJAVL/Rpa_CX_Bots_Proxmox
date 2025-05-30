import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
dir = os.listdir('C:\\Users\\vix10\\Downloads')

if 'output.csv' in dir or 'output.CSV' in dir:

    print('Extraccion completa')
    print('ARCHIVO DESCARGADO')
    busquedaExtraccion = False

    ################### Conversion CSV a EXCEL

    # with open('C:\\Users\\vix10\\Downloads\\output.CSV', "rb") as f:
    #     df = pd.read_csv(f, encoding="utf_16", sep=',', low_memory=False, skip_blank_lines=True)
    #     excelWrite = pd.ExcelWriter('C:\\Users\\vix10\\Downloads\\output.xlsx', engine='xlsxwriter')
    #     df.to_excel(excelWrite, index=None)
    #     excelWrite.close()
    

    ################### Obtencion de FECHA

    fechaHRA = datetime.datetime.now()
    fechaHRA = str(fechaHRA)
    fechaHRA = fechaHRA.replace(":", "")
    nArchivo = 'Extraccion '+ tExtraccion + ' ' + fechaHRA + '.CSV'

    archivoO = 'C:\\Users\\vix10\\Downloads\\output.CSV'
    archivoNew = 'C:\\Users\\vix10\\Downloads\\' + nArchivo

    os.rename(archivoO, archivoNew)

    ################### CONFIGURACION FTP

    ftp_servidor = '192.168.50.37'
    ftp_usuario  = 'rpaback1'
    ftp_clave    = 'Cyber123'
    ftp_raiz     = '/Extracciones'

    ################## DATOS DEL FICHERO A SUBIR

    ficheroOrigen = archivoNew
    ficheroDestino = nArchivo

    ################# Conexion al FTP

    try:

        s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
        try:
            f = open(ficheroOrigen, 'rb')
            s.cwd(ftp_raiz)
            s.storbinary('STOR ' + ficheroDestino, f)
            f.close()
            s.quit()
        except:
            print("No se ha podido encontrar el fichero" + ficheroOrigen)
    
    except Exception as e:
        print("No se ha podido   con el servidor" + ftp_servidor)
        
    print('Archivo cargado a la FTP')
    if "null" not in correo:
        try: 
            print('Se hara el envio de la extraccion')
            sleep(10)
            # Parametros del correo
            remitente = 'extracciones@wincall.mx'
            # destinatario = correo
            destinatario = correo
            asunto = 'Extraccion: ' + tExtraccion
            cuerpo = 'Notificacion Extracion Exitosa   Extraccion: ' + tExtraccion
            path = 'C:\\Users\\vix10\\Downloads\\' + nArchivo
            nombreAdjunto = nArchivo

            # Creacion del objeto mensaje
            mensaje = MIMEMultipart()
            
            try:
                # Atributos del mensajs
                mensaje['From'] = remitente
                mensaje['To'] = destinatario
                mensaje['Subject'] = asunto

                # Se agrega el cuerpo del mensaje como objeto MIME de tipo texto
                mensaje.attach(MIMEText(cuerpo, 'plain'))

                # Manejo del archivo a adjuntar
                # archivoAdjunto = open(path, 'rb')
                # adjuntoMIME = MIMEBase('application', 'octet-stream')
                # adjuntoMIME.set_payload((archivoAdjunto).read())
                # encoders.encode_base64(adjuntoMIME)
                # adjuntoMIME.add_header('Content-Disposition', 'attachment; filename= %s' % nombreAdjunto)
                # mensaje.attach(adjuntoMIME)
                # archivoAdjunto.close()

                # Se genera conexion y configuracion del servidor
                try:
                    sesionSMTP = smtplib.SMTP_SSL('mail.wincall.mx', 465)
                    sesionSMTP.login('extracciones@wincall.mx', 'Fx1rOeoaf3DW')
                    texto = mensaje.as_string()
                    sesionSMTP.sendmail(remitente, destinatario, texto)
                    sesionSMTP.quit()
                except Exception as e:
                    error = 'Error Envio Correo'
                    print(error)
                    cont = 0
                    dir = os.listdir('C:\\Users\\vix10\\Downloads')
                    for x in dir:
                        if 'output.CSV' in x or 'output.csv' in x:
                            print('Archivo a eliminar: ', x)
                            os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                            cont += 1
                        elif 'Extraccion' in x:
                            print('Archivo a eliminar: ', x)
                            os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                            cont += 1
                        
                        if cont == 2:
                            break 
                    print(e)
                    sleep(1000)
                    return False, '-',

            except Exception as e:
                print(e)
                continue
                
            cont = 0
            dir = os.listdir('C:\\Users\\vix10\\Downloads')
            for x in dir:
                if 'output.CSV' in x or 'output.csv' in x:
                    print('Archivo a eliminar: ', x)
                    os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                    cont += 1
                elif 'Extraccion' in x:
                    print('Archivo a eliminar: ', x)
                    os.remove('C:\\Users\\vix10\\Downloads\\'+x)
                    cont += 1
                
                if cont == 2:
                    break 
            sleep(3)
            print('Extraccion finalizada')
            return True, nArchivo,'Completado'
        except Exception as e:
            print(e)
            sleep(1000)
