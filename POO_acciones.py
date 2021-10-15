class Accion:
    # origen es el origen de los datos - ex: investpy_spain,investpy_usa,bolsa_madrid
    # nombre es el nombre de la accion para el origen dado
    # valor es el valor de la accion
    # volumen es el volumen de las acciones
    # variacion es la variacion de las acciones con respecto al dia anterior (en caso de ser habil)
    # fecha es la fecha a la cual corresponden los valores anteriores obtenidos
    
    def __init__(self,origen,nombre,valor,volumen,variacion,fecha):
        self.origen = origen
        self.nombre = nombre
        self.valor = valor
        self.volumen = volumen
        self.variacion = variacion
        self.fecha = fecha
        
    def __guardar__(self,origen,nombre,valor,volumen,variacion,fecha):
        '''Guarda el registro de la accion en un csv'''
        pass
    
    
    def __leer__(self,origen,nombre,valor,volumen,variacion,fecha):
        '''Lee el registro de la accion de un csv'''
        pass
    
    def __imprimir__(self,origen,nombre,fecha):
        '''Imprime la informacion de la accion'''
        pass

    def __historico__(self,origen,nombre):
        '''Retorna los valores historicos de la accion'''
        pass

    def __maximo__(self,origen,fecha):
        '''Retorna la accion con mayor ganancia'''
        pass

    def __minimo__(self,origen,fecha):
        '''Retorna la accion con mayor perdida'''
        pass
