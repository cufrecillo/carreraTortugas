class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
        
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
    def propiedadPrivada(self, valor):
        if valor == None:
            #actua como getter
            return self.__propiedad_privada
        else:
            #actua como setter
            self.__propiedad_privada = valor
            
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada"
    
if __name__ == '__main__':
    c = ClaseConGetterySetter()