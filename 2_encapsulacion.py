"""
Ejemplo de ENCAPSULACIÓN en POO
La encapsulación consiste en ocultar los detalles internos de un objeto
y permitir el acceso solo a través de métodos públicos.
"""

class CuentaBancaria:
    """Clase que representa una cuenta bancaria con saldo encapsulado."""
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (encapsulado)
    
    def depositar(self, cantidad):
        """Método público para depositar dinero."""
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: ${self.__saldo}")
        else:
            print("La cantidad debe ser positiva.")
    
    def retirar(self, cantidad):
        """Método público para retirar dinero."""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: ${self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")
    
    def consultar_saldo(self):
        """Método público para consultar el saldo."""
        return self.__saldo

# Uso
if __name__ == "__main__":
    cuenta = CuentaBancaria("Ana López", 1000)
    print(f"Titular: {cuenta.titular}")
    cuenta.depositar(500)
    cuenta.retirar(200)
    print(f"Saldo final: ${cuenta.consultar_saldo()}")
    # print(cuenta.__saldo)  # Esto daría error (atributo privado)