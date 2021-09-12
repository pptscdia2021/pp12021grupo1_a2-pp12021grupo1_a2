# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# indicar la ruta



def generar_tabla(url,tipo,att_nom,att_val):
        
    page = requests.get(url).text 
    soup = BeautifulSoup(page, "lxml")
    tabla = soup.find(tipo, attrs={att_nom: att_val})
    tabla
    return tabla
    
    
    
def limpiar_tabla(tabla,nombre,precio,cambio_porc,volumen):
    ''' Nombre corresponde a el numero de celda donde esta el nombre identificador de la accion. Precio corresponde al valor de la accion al momento de la consulta, cambio_porc es la variacion porcentual con el ultimo cierre, volumen es la cantidad de acciones        '''
        
    name=""
    price=""
    cambio=""
    volumen_num=""
    time_stamp=datetime.now()
    nroFila=0
    
    for fila in tabla.find_all("tr"):
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==nombre:
                name=celda.text
                print("Indice:", name)
            if nroCelda==precio:
                price=celda.text
                print("Valor:", price)
            if nroCelda==cambio_porc:
                cambio=celda.text
                print("Variacion %:", cambio)
            if nroCelda==volumen:
                volumen_num=celda.text
                print("Volumen:", volumen_num)
            nroCelda=nroCelda+1
        nroFila=nroFila+1

        with open('bolsa_ibex35'+time_stamp.strftime("%Y%m%d%H%M")+'.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name, price,cambio,volumen_num, time_stamp])

tabla= generar_tabla('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','table','id','ctl00_Contenido_tblAcciones')
     
nombre=0
precio=1
cambio_porc=2
volumen=5


limpiar_tabla(tabla,nombre,precio,cambio_porc,volumen)