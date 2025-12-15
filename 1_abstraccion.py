"""
Ejemplo de ABSTRACCIÓN en POO
La abstracción consiste en ocultar detalles complejos y mostrar solo lo esencial.
Aquí, la clase 'Vehiculo' define una interfaz común sin implementar todos los métodos.
"""

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """Clase abstracta que representa un vehículo genérico."""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def mover(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass
    
    def describir(self):
        """Método concreto que puede ser usado por todas las subclases."""
        return f"{self.marca} {self.modelo}"

# Clase concreta que implementa la abstracción
class Coche(Vehiculo):
    def mover(self):
        return "El coche se mueve por la carretera."

# Uso
if __name__ == "__main__":
    mi_coche = Coche("Toyota", "Corolla")
    print(f"Vehículo: {mi_coche.describir()}")
    print(f"Acción: {mi_coche.mover()}")