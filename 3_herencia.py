"""
Ejemplo de HERENCIA en POO
La herencia permite crear una nueva clase basada en una clase existente,
heredando sus atributos y métodos.
"""

class Animal:
    """Clase base (padre) que representa un animal genérico."""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        return f"{self.nombre} está comiendo."
    
    def hacer_sonido(self):
        return "Sonido genérico de animal."

class Perro(Animal):
    """Clase derivada (hija) que hereda de Animal."""
    
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.raza = raza
    
    def hacer_sonido(self):
        """Sobrescribe el método de la clase base."""
        return "¡Guau guau!"
    
    def buscar(self):
        """Método adicional específico de Perro."""
        return f"{self.nombre} está buscando la pelota."

class Gato(Animal):
    """Otra clase derivada de Animal."""
    
    def hacer_sonido(self):
        return "¡Miau miau!"
    
    def ronronear(self):
        return f"{self.nombre} está ronroneando."

# Uso
if __name__ == "__main__":
    perro = Perro("Rex", 5, "Labrador")
    gato = Gato("Michi", 3)
    
    print(f"Perro: {perro.nombre}, Raza: {perro.raza}")
    print(perro.hacer_sonido())
    print(perro.buscar())
    
    print(f"\nGato: {gato.nombre}, Edad: {gato.edad}")
    print(gato.hacer_sonido())
    print(gato.ronronear())