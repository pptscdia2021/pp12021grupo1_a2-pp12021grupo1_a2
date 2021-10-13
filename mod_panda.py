# Diccionario de acciones para compensar diferencias de denominación entre la bolsa de madrid y la api INVESTPY
def evaluar_diferencias(cv_madrid,csv_investpy):
    '''La funcion toma dos archivos CSV de distintas fuentes y compara las variaciones entre ambas fuentes accion por accion'''
    import pandas as pd
    relacion_acciones= dict()
    relacion_acciones= {'ACCIONA' : 'Acciona' , 'ACERINOX' : 'Acerinox' , 'ACS' : 'ACS' , 'AENA' : 'Aena' , 'ALMIRALL' : 'Almirall' , 'AMADEUS' : 'Amadeus' , 'ARCELORMIT.' : 'ArcelorMittal' , 'B.SANTANDER' : 'Santander' , 'BA.SABADELL' : 'B. Sabadell' , 'BANKINTER' : 'Bankinter' , 'BBVA' : 'BBVA' , 'CAIXABANK' : 'Caixabank' , 'CELLNEX' : 'Cellnex Telecom' , 'CIE AUTOMOT.' : 'Cie Automotive' , 'ENAGAS' : 'Enagas' , 'ENDESA' : 'Endesa' , 'FERROVIAL' : 'Ferrovial' , 'FLUIDRA' : 'Fluidra' , 'GRIFOLS CL.A' : 'Grifols' , 'IAG' : 'IAG' , 'IBERDROLA' : 'Iberdrola' , 'INDITEX' : 'Inditex' , 'INDRA A' : 'Indra A' , 'INM.COLONIAL' : 'Inmobiliaria Colonial' , 'MAPFRE' : 'Mapfre' , 'MELIA HOTELS' : 'Melia Hotels' , 'MERLIN' : 'Merlin Properties SA' , 'NATURGY' : 'Naturgy Energy' , 'PHARMA MAR' : 'Pharma Mar' , 'REPSOL' : 'Repsol' , 'SOLARIA' : 'Solaria' , 'TELEFONICA' : 'Telefonica' , 'VISCOFAN' : 'Viscofan' }

    # Valores de cada csv en comparanción       
    df = pd.read_csv(cv_madrid)
    df2 = pd.read_csv(csv_investpy)

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
            except KeyError:
                pass
    
        print("NOMBRE1:"+str(nombre)+" NOMBRE2: "+str(nuevo_nombre)+" VAL1: "+str(val1)+" VAL2: "+str(val2)+" VAR1: "+str(var1)+" VAR2: "+str(var2)+" VOL1: "+str(vol1)+" VOL2: "+str(vol2))
        print("NOMBRE1:"+str(nombre)+" DIFERENCIA DE VALOR: "+str(val2-val1)+" DIFERENCIA DE VARIACION: "+str(abs(var2)-abs(var1))+" DIFERENCIA DE VOLUMEN: "+str(vol2-vol1))





def maximoyminimo(archivo):
    '''LA FUNCION TOMA COMO PARAMETRO UN ARCHIVO Y ANALIZA CON PANDAS CUAL ES LA ACCION CON MAYOR INDICE DE PERDIDA Y CUAL CON MAYOR DE GANANCIA'''
    import pandas as pd
    df = pd.read_csv(archivo)

    maximo=df.iloc[:,2].argmax()
    minimo=df.iloc[:,2].argmin()
    return df.loc[[maximo]], df.loc[[minimo]]

# INICIO DE PRUEBAS Y EJECUCION


cv_madrid="bolsa_ibex35.csv"
csv_investpy="bolsa_investpy.csv"
evaluar_diferencias(cv_madrid,csv_investpy)


maximo,minimo=maximoyminimo("bolsa_ibex35.csv")
print("valormaximo:")
print(maximo)
print("-----")
print("valorminimo:")
print(minimo)