class Converciones:
    def __init__(self,cantidad):
        self.__cantidad=cantidad
        
    def PesosAdolares(self):
        dolar=self.__cantidad/22.17
        return dolar
    
    
    def PesosAEuros(self):
        euros=self.__cantidad/24.62
        return euros
    
    def DolarAPesos(self):
        pesos=self.__cantidad*22.17
        return pesos
    
    def DolarAEuros(self):
        euros=self.__cantidad*0.90
        return euros
    
    def EurosADolar(self):
        dolar=self.__cantidad*1.11
        return dolar

    def EurosAPesos(self):
        Pesos=self.__cantidad*24.62
        return Pesos