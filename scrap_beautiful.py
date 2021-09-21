#requerido: pip install investpy


# import libraries
import requests
import csv
import investpy
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date, timedelta


#DEFINICION DE FUCNIONES

def respaldo_csv(nombre,nuevonombre):
    import pandas as pd
    df=pd.read_csv(nombre)
    df.to_csv(nuevonombre)

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
    nuevonombre='bolsa_ibex35'+time_stamp.strftime("%Y%m%d%H")+'.csv'
    for fila in tabla.find_all("tr"):
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==nombre:
                name=celda.text
                print("Indice:", name)
            if nroCelda==precio:
                price=celda.text
                price=price.replace(".","")
                price=price.replace(",",".")
                print("Valor:", price)
            if nroCelda==cambio_porc:
                cambio=celda.text
                cambio=cambio.replace(".","")
                cambio=cambio.replace(",",".")

                print("Variacion %:", cambio)
            if nroCelda==volumen:
                volumen_num=celda.text
                volumen_num=volumen_num.replace(".","")
                volumen_num=volumen_num.replace(",",".")
                
                
                print("Volumen:", volumen_num)
            nroCelda=nroCelda+1
        nroFila=nroFila+1

        with open('bolsa_ibex35.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name, price,cambio,volumen_num, time_stamp])
    respaldo_csv('bolsa_ibex35.csv',nuevonombre)

            
def devolver_inverstpy(accion,fecha,pais):

    fecha_datetime=datetime.strptime(fecha, '%d/%m/%Y')
    yesterday = fecha_datetime - timedelta(days=1)
    ayer=yesterday.strftime('%d/%m/%Y') 
    try:
        search_result= investpy.search_quotes(text=accion,products=['stocks'],countries=[pais],n_results=1)
        historical_data = search_result.retrieve_historical_data(from_date=ayer, to_date=fecha)
        valor= historical_data.head()
    except :
        valor="NO ABRIO LA BOLSA"
    return valor,accion



def listado_acciones(pais,fecha):
    time_stamp=datetime.now()
    diccionario=investpy.stocks.get_stocks_dict(country=pais,columns=None,as_json=False)
    acciones_pais=[]
    nuevonombre='bolsa_'+pais+'_investpy'+time_stamp.strftime("%Y%m%d%H")+'.csv'
    for nombre in diccionario:
        acciones_pais.append(nombre["name"])
        valor,accion=devolver_inverstpy(nombre["name"],fecha,pais)
    
        if isinstance(valor,str):
            pass
        else:
            lista_valores=valor.values.tolist()
            lista_valores[0].insert(0,accion)
            print(lista_valores[0])
            
            with open('bolsa_investpy.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([lista_valores[0][0], lista_valores[0][1],lista_valores[0][6],lista_valores[0][5], fecha])
    respaldo_csv('bolsa_investpy.csv',nuevonombre)
            
    return lista_valores[0]
            
#PRUEBA Y EJECUCION
    
tabla= generar_tabla('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','table','id','ctl00_Contenido_tblAcciones')
     
nombre=0
precio=1
cambio_porc=2
volumen=5


limpiar_tabla(tabla,nombre,precio,cambio_porc,volumen)
   






pais='Spain'
fecha='18/09/2021'
listado_acciones(pais,fecha)