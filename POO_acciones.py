import csv
import pandas as pd
from datetime import datetime
import requests
import investpy
from bs4 import BeautifulSoup
from datetime import date, timedelta

class Accion:
   
   
    # origen es el origen de los datos - ex: investpy_spain,investpy_usa,bolsa_madrid
    # nombre es el nombre de la accion para el origen dado
    # valor es el valor de la accion
    # volumen es el volumen de las acciones
    # variacion es la variacion de las acciones con respecto al dia anterior (en caso de ser habil)
    # fecha es la fecha a la cual corresponden los valores anteriores obtenidos

   
   
    def __init__(self,origen,nombre=None,valor=None,volumen=None,variacion=None,fecha=None):
        self.origen = origen
        self.nombre = nombre
        self.valor = valor
        self.volumen = volumen
        self.variacion = variacion
        self.fecha = fecha
       
    #def __guardar__(self,origen,nombre,valor,volumen,variacion,fecha):
    def __guardar__(self):
        '''Guarda el registro de la accion en un csv'''
        if self.valor == None or self.volumen == None or self.variacion == None or self.nombre == None or self.fecha == None or self.origen == "":
            print("EL METODO __guardar__ requiere que se carguen todos los argumentos")
           
        else:    
            with open('bolsa_'+str(self.origen)+'.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([self.nombre, self.valor,self.variacion,self.volumen, self.fecha])
                print("Se guardo correctamente el registro "+self.nombre+" en el archivo: "+'bolsa_'+str(self.origen)+'.csv')

       
   
   
    #def __leer__(self,origen,nombre,valor,volumen,variacion,fecha):
    def __leer__(self):
        '''Lee el registro de la accion de un csv'''
           
        try:
            if self.origen == "" and self.nombre == None and self.fecha == None :
                print("EL METODO __leer__ requiere que se carguen los arguentos ORIGEN,NOMBRE,FECHA")
                return
            elif self.origen == "":
                print("EL METODO __leer__ requiere que se cargue el argumento ORIGEN")
                return
            elif self.nombre == None and self.fecha == None:
                array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
                lista_acciones=array_acciones.loc[(array_acciones['Nombre'] != "") & (array_acciones['Fecha'] != "")]
           
                print(lista_acciones)
                return
            elif  self.fecha == None:
                array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
                lista_acciones=array_acciones.loc[(array_acciones['Nombre'] == self.nombre) & (array_acciones['Fecha'] != "")]
                print(self.nombre)
                print(lista_acciones)
                return
            elif  self.nombre == None:
                array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
                lista_acciones=array_acciones.loc[(array_acciones['Nombre'] != "") & (array_acciones['Fecha'] == self.fecha)]
                print(self.fecha)
                print(lista_acciones)
                return
            else  :
                array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
                lista_acciones=array_acciones.loc[(array_acciones['Nombre'] == self.nombre) & (array_acciones['Fecha'] == self.fecha)]
                print(lista_acciones)
                return
               
               
        except FileNotFoundError:
            print("EL ARCHIVO DE ORIGEN NO EXISTE")
           
   
   
       
   
    def __imprimir__(self):
        '''Imprime la informacion del objeto'''
        print("-------------------------")
        print("ACCION: "+str(self.nombre))
        print("VALOR: "+str(self.valor))
        print("VARIACION: "+str(self.variacion))
        print("VOLUMEN: "+str(self.volumen))
        print("FECHA: "+str(self.fecha))
        print("ORIGEN DE LOS DATOS: "+str(self.origen))
        print("-------------------------")

    def __historico__(self,fecha_inicio):
        '''Retorna los valores historicos de la accion'''
        if self.origen == "" or self.nombre == None  :
            print("EL METODO __histrico__ requiere que se carguen los arguentos ORIGEN y NOMBRE")
            return
        else :
            array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
            lista_acciones=array_acciones.loc[(array_acciones['Nombre'] == self.nombre) & (array_acciones['Fecha'] >= fecha_inicio)]
           
            print(lista_acciones)
            return

       

    def __maximo__(self):
        '''Retorna la accion con mayor ganancia'''
        if self.origen == "" or self.fecha == None  :
            print("EL METODO __maximo__ requiere que se carguen los arguentos ORIGEN y FECHA")
            return
        else :
           
            array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
            lista_acciones=array_acciones.loc[(array_acciones['Fecha'] == self.fecha)]
           
       
            try:
                maxima =  lista_acciones.loc[lista_acciones["Variacion"].idxmax()]
                print(maxima)
                return maxima
            except ValueError:
                print("SIN REGISTROS PARA LA FECHA")
           
           
           
           
           
           
       
       
       

    def __minimo__(self):
        '''Retorna la accion con mayor perdida'''
        if self.origen == "" or self.fecha == None  :
            print("EL METODO __minimo__ requiere que se carguen los arguentos ORIGEN y FECHA")
            return
        else :
            array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
            lista_acciones=array_acciones.loc[(array_acciones['Fecha'] == self.fecha)]
           
            try:
                minima =  lista_acciones.loc[lista_acciones["Variacion"].idxmin()]
                print(minima)
                return minima
            except ValueError:
                print("SIN REGISTROS PARA LA FECHA")

               

   
           
    def __graficar__(self,tipo):
        import matplotlib.pyplot as plt

        array_acciones= pd.read_csv('bolsa_'+str(self.origen)+'.csv',names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
        lista_acciones=array_acciones.loc[(array_acciones['Nombre'] == self.nombre)]
   
        if tipo == "Variacion":
            plt.plot(lista_acciones['Fecha'],lista_acciones['Variacion'])
        elif tipo == "Valor":
            plt.plot(lista_acciones['Fecha'],lista_acciones['Valor'])
        elif tipo == "Volumen":
            plt.plot(lista_acciones['Fecha'],lista_acciones['Volumen'])
        else:
            print("ENTRADA NO VALIDA - SELECCION (Variacion) - (Volumen) - (Valor) ")
       
               
# --------------------- PONER EN UN SEGUNDO ARCHIVO: --------------------                
               
               
               
               
def generar_tabla(url,tipo,att_nom,att_val):
    '''Se genera un arreglo de informacion (tabla) a partir de la informacion obtenida dentro de la etiqueta de tipo (tipo) identificada con los atributos (att_nom) y (att_val) dentro de la (url) '''    
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    tabla = soup.find(tipo, attrs={att_nom: att_val})
    tabla
    return tabla

def limpiar_tabla(tabla,nombre,precio,cambio_porc,volumen):
    '''La funcion genera un archivo csv con la fecha de ejecucion y una copia del mismo con un nombre generico a partir de la tabla obtenida en la funcion generar_tabla. Nombre corresponde a el numero de celda donde esta el nombre identificador de la accion. Precio corresponde al valor de la accion al momento de la consulta, cambio_porc es la variacion porcentual con el ultimo cierre, volumen es la cantidad de acciones        '''
    origen="pag_yahoo"  
    name=""
    price=""
    cambio=""
    volumen_num=""
    time_stamp=datetime.now()
    time_stamp.strftime("%Y%m%d%H")
   
    nroFila=0
    acciones=[]
   
   
   
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
        accion=Accion(origen,name,precio,volumen_num,cambio,time_stamp.strftime('%d/%m/%Y'))
        acciones.append(accion)
    return acciones


def devolver_inverstpy(accion,fecha,pais):
    '''Se obtiene un dataframe con la informacion entregada por la api INVESTPY con datos de la accion consultada en la fecha y el pais de interes'''
   
   
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
    '''Obtiene a partir de la API investpy la lista de acciones disponibles para un determinado (pais) en una determinada (fecha). A partir de esta lista vamos a llamar a la funcion devolver_investpy. Los resultados los guardara en un csv con la fecha y una copia con un nombre generico'''
    origen="investpy_"+pais
    time_stamp=datetime.now()
    diccionario=investpy.stocks.get_stocks_dict(country=pais,columns=None,as_json=False)
    acciones_pais=[]
    acciones=[]
    for nombre in diccionario:
        acciones_pais.append(nombre["name"])
        #COMIENZO LAS LLAMADAS PARA OBTENER LOS DATAFRAME CON LOS DATOS DE LAS ACCIONES EN DICCIONARIO
        try:
            valor,accion=devolver_inverstpy(nombre["name"],fecha,pais)
            if isinstance(valor,str):
                pass
            else:
                lista_valores=valor.values.tolist()
                lista_valores[0].insert(0,accion)
                print(lista_valores[0])
            print("LOS ARGUMENTOS SON:")
            print(origen,lista_valores[0][0], lista_valores[0][1],lista_valores[0][5],lista_valores[0][6], fecha)
            accion=Accion(origen,lista_valores[0][0], lista_valores[0][1],lista_valores[0][5],lista_valores[0][6], fecha)
            acciones.append(accion)    
       
       
       
        except:
            print("NO HAY REGISTROS PARA LA FECHA")
            return
    return acciones
           
   


# Diccionario de acciones para compensar diferencias de denominación entre la bolsa de madrid y la api INVESTPY
def evaluar_diferencias(cv_madrid,csv_investpy,fecha):
    '''La funcion toma dos archivos CSV de distintas fuentes y compara las variaciones entre ambas fuentes accion por accion'''
    import pandas as pd
    relacion_acciones= dict()
    relacion_acciones= {'ACCIONA' : 'Acciona' , 'ACERINOX' : 'Acerinox' , 'ACS' : 'ACS' , 'AENA' : 'Aena' , 'ALMIRALL' : 'Almirall' , 'AMADEUS' : 'Amadeus' , 'ARCELORMIT.' : 'ArcelorMittal' , 'B.SANTANDER' : 'Santander' , 'BA.SABADELL' : 'B. Sabadell' , 'BANKINTER' : 'Bankinter' , 'BBVA' : 'BBVA' , 'CAIXABANK' : 'Caixabank' , 'CELLNEX' : 'Cellnex Telecom' , 'CIE AUTOMOT.' : 'Cie Automotive' , 'ENAGAS' : 'Enagas' , 'ENDESA' : 'Endesa' , 'FERROVIAL' : 'Ferrovial' , 'FLUIDRA' : 'Fluidra' , 'GRIFOLS CL.A' : 'Grifols' , 'IAG' : 'IAG' , 'IBERDROLA' : 'Iberdrola' , 'INDITEX' : 'Inditex' , 'INDRA A' : 'Indra A' , 'INM.COLONIAL' : 'Inmobiliaria Colonial' , 'MAPFRE' : 'Mapfre' , 'MELIA HOTELS' : 'Melia Hotels' , 'MERLIN' : 'Merlin Properties SA' , 'NATURGY' : 'Naturgy Energy' , 'PHARMA MAR' : 'Pharma Mar' , 'REPSOL' : 'Repsol' , 'SOLARIA' : 'Solaria' , 'TELEFONICA' : 'Telefonica' , 'VISCOFAN' : 'Viscofan' }

    # Valores de cada csv en comparanción      
    df = pd.read_csv(cv_madrid,names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])
    df2 = pd.read_csv(csv_investpy,names=["Nombre", "Valor", "Variacion", "Volumen", "Fecha"])

   
    df = df[(df['Fecha'] == fecha)]
    df2 = df2[(df2['Fecha'] == fecha)]
    df = df.values.tolist()
    df2 = df2.values.tolist()
    for N in df:
        nombre=N[0]
       
     
       
        val1=N[1]
        var1=N[2]
        vol1=N[3]
        for M in df2:
            try:
               
                if M[0]==relacion_acciones[nombre]:
                   
                    nuevo_nombre=relacion_acciones[nombre]
                    val2=M[1]
                    var2=M[2]
                    vol2=M[3]
                    difval=float(val2)-float(val1)
                    difvar=abs(float(var2))-abs(float(var1))
                    difvol=float(vol2)-float(vol1)
            except KeyError:
                pass
   
        print("NOMBRE1:"+str(nombre)+" NOMBRE2: "+str(nuevo_nombre)+" VAL1: "+str(val1)+" VAL2: "+str(val2)+" VAR1: "+str(var1)+" VAR2: "+str(var2)+" VOL1: "+str(vol1)+" VOL2: "+str(vol2))
       
#        print("NOMBRE1:"+str(nombre)+" DIFERENCIA DE VALOR: "+str(val2-val1)+" DIFERENCIA DE VARIACION: "+str(abs(var2)-abs(var1))+" DIFERENCIA DE VOLUMEN: "+str(vol2-vol1))
        print("NOMBRE1:"+str(nombre)+" DIFERENCIA DE VALOR: "+str(difval)+" DIFERENCIA DE VARIACION: "+str(difvar)+" DIFERENCIA DE VOLUMEN: "+str(difvol))






'''
tabla= generar_tabla('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','table','id','ctl00_Contenido_tblAcciones')

#LAS SIGUIENTES VARIABLES DEFINEN LA POSICION EN LA TABLA DE LA INFORMACION REQUERIDA, DE EXISTIR UNA MODIFICACION EN LA URL DESTINO SE DEBERAN REDEFINIR ESTOS VALORES    
nombre=0
precio=1
cambio_porc=2
volumen=5

#GENERO UNA LISTA DE OBJETOS ACCIONES OBTENIDAS POR WEB SCRAPPING CONTRA LA PAGINA DE YAHOO
acciones=limpiar_tabla(tabla,nombre,precio,cambio_porc,volumen)


pais='Spain'
fecha='18/09/2021'

#GENERO UNA LISTA DE OBJETOS ACCIONES OBTENIDAS POR INVESTPY
acciones2=listado_acciones(pais,fecha)

#EVALUO LA DIFERENCIAS ENTRE LOS VALORES OBTENIDOS POR LOS DISTINTOS SISTEMAS
evaluar_diferencias("bolsa_pag_yahoo.csv","bolsa_investpy_Spain.csv")

# GENERA GRAFICO DEL TIPO DE DATO QUE QUERRAMOS SOBRE UNA ACCION DADA
comparar=Accion("investpy_Spain","Almagro Capital","","","","")
comparar.__graficar__("Volumen")

'''