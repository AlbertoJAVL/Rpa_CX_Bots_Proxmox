# cyber-depuracion

Ese bot de depuración utiliza Python en su versión:
 - Python 3.10.10

Es necesario copiar la carpata *driver_chrome* en la raiz del sico C, esta carpeta contiene el controlador del webdriver de Chrome (ChromeDriver 110.0.5481.77).

## IMPORTANTE
Para tener acceso a las librerias actuales ejecutar el siguiente comando:

"pip install -r requirements.txt"

Si y solo si se tiene la versión de python utilizada para este bot, o bien, hacerlo desde un entorno virtual (virtualenv).

## SELENIUM

Para más información respecto a los comando utilizados revisar la documenatación oficial de Selenium en:
 https://selenium-python.readthedocs.io/installation.html

## ERRORES

01. 
02. 
03. 
04. 
05. ERROR en el llenado de los campos de la orden de servicio.
06. ERROR en la localizacion de lagun elemento en pantalla.  
    - Solucion: La solucion no es modificar la funcion, se debe volver a mapear el elemento en pantalla.
07.  

## NOTAS

1. En la funcion rellena_campos_orden_servicio se comento el llenado del estado "CANCELADO" porque este SIEBEL ya no permite simular el rellenado de campos par mas pruebas, es decir, las cuentas solo nos sirvem apra una prueba si se cancelan.

2. No se ha encontrado la alerta de error cuando no se pudo cancelar bien una cuenta en la funcion: cerrar_orden_servicio

3. Los casos de negocio no aparecen en la cuenta, por lo que no se pueden valdiar si se cierran bien. 

4. Cuando una cuenta ya está cancelada se cierra el DRIVER pero no cuenta como error.

