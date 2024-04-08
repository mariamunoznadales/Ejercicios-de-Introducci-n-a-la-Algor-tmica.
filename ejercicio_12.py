class Cuenta:
    def __init__(self, saldo_inicial):
        #Inicializa una nueva cuenta con un saldo inicial.
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        #Permite depositar una cantidad en la cuenta.
        self.saldo += cantidad

    def retirar(self, cantidad):
        
        #Permite retirar una cantidad de la cuenta, siempre y cuando no resulte en un saldo negativo.
        #Devuelve True si la retirada fue exitosa, False en caso contrario.
        
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        else:
            return False

    def obtener_saldo(self):
        #Obtiene el saldo actual de la cuenta.
        return self.saldo

class CuentaConDescubierto(Cuenta):
    def __init__(self, saldo_inicial, descubierto_autorizado):
    #Inicializa una nueva cuenta con un saldo inicial y un descubierto autorizado.
        super().__init__(saldo_inicial)
        self.descubierto_autorizado = descubierto_autorizado

    def retirar(self, cantidad):
        
        #Permite retirar una cantidad de la cuenta, considerando el descubierto autorizado si es necesario.
        #Devuelve True si la retirada fue exitosa, False en caso contrario.
        
        if self.saldo + self.descubierto_autorizado >= cantidad:
            self.saldo -= cantidad
            return True
        else:
            return False
