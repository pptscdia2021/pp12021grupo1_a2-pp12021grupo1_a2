# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# indicar la ruta
url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
# tarda 480 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")
# Obtenemos la tabla por un ID específico
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
tabla
name=""
price=""
cambio=""
volumen_num=""
nroFila=0
for fila in tabla.find_all("tr"):
    #for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Acción: ", name)
        if nroCelda==1:
            price=celda.text
            print("Valor: ", price)
        if nroCelda==2:
            cambio=celda.text
            print("Variación %:", cambio)
        if nroCelda==5:
            volumen_num=celda.text
            print("Valumen: ", volumen_num)
        nroCelda=nroCelda+1
    nroFila=nroFila+1
    # Abrimos el csv con append para que pueda agregar contenidos al final del archivo
    with open('bolsa_ibex35.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price, cambio, volumen_num, datetime.now()])
