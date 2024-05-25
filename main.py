
from funciones_mate import *


a = None
b = None

while True:
    limpiar_pantalla()
    print("\nCalculadora")
    print(f"1..Para igresar el primer num A: {a}")
    print(f"2..Para ingresar el segundo num B: {b}")
    print("3..Calcular todas las operaciones")
    print("4..Salir")

    opcion=input("Elija una opcion: ")


    match opcion:
        case "1":
            try:
                a =int(input("ingrese el primer operando(A): "))
            except ValueError:
                print("Error,Ingrese un numero Valido.")
        case "2":
            try:
                b =int(input("Ingrese el segundo operador(B): "))
            except ValueError:
                print("Error,Ingrese un numero Valido.")
        case "3":
                if a is None or b is None:
                    print("Debe ingresar ambos operandos antes de calcular.")
                else:
                    try:
                        print(f"el resutaldo de A+B es : {suma(a,b)}")
                        print(f"el resultado de A-B es : {resta(a,b)}")
                        resultado_div = division(a,b)
                        if resultado_div == "No es posible dividir por cero":
                            print(resultado_div)
                        else:
                            print(f"El resultado de A/B: {resultado_div}")
                        print(f"El factorial de A es {factorial(a)} y el de B {factorial(b)}")   
                    except TypeError:
                        print("Problema de tipo")   
        case "4":
            print("No vemos me voy,chau chau")
            break
        case _:
            print("Opciones no validas, intenta denueveo")
    pausar()

    
    


    
        
