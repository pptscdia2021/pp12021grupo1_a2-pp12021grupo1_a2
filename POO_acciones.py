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
           