"""
Ejemplo de POLIMORFISMO en POO
El polimorfismo permite que objetos de diferentes clases
respondan al mismo mensaje (método) de manera diferente.
"""

class Figura:
    """Clase base para figuras geométricas."""
    
    def area(self):
        """Método que será sobrescrito por las subclases."""
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def __str__(self):
        return f"Rectángulo {self.ancho}x{self.alto}"

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.1416 * (self.radio ** 2)
    
    def __str__(self):
        return f"Círculo de radio {self.radio}"

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def __str__(self):
        return f"Triángulo base {self.base}, altura {self.altura}"

# Función polimórfica
def mostrar_area(figura):
    """Acepta cualquier objeto que sea una Figura (polimorfismo)."""
    print(f"{figura} -> Área: {figura.area():.2f}")

# Uso
if __name__ == "__main__":
    figuras = [
        Rectangulo(5, 3),
        Circulo(4),
        Triangulo(6, 2)
    ]
    
    print("Cálculo de áreas (Polimorfismo):")
    for figura in figuras:
        mostrar_area(figura)