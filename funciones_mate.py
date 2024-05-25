from os import system


def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")


def suma(a, b):
    """Calcula la suma de dos números."""
    return a + b

def resta(a, b):
    """Calcula la resta de dos números."""
    return a - b

def division(a, b):
    """Calcula la división de dos números. Maneja división por cero."""
    if b == 0:
        return "No es posible dividir por cero"
    return a / b

def multiplicacion(a, b):
    """Calcula la multiplicación de dos números."""
    return a * b

def factorial(n):
    """Calcula el factorial de un número no negativo."""
    if n < 0:
        return "Factorial no está definido para números negativos"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result