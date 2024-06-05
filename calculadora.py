import platform

class Calculadora:
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def raiz_cuadrada(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return a ** 0.5

    def potencia(self, base, exponente):
        return base ** exponente

    def logaritmo(self, a, base=10):
        import math
        if a <= 0:
            raise ValueError("No se puede calcular el logaritmo de un número no positivo")
        return math.log(a, base)
