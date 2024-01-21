# EJERCICIO 1

# Realiza una función llamada area_rectangulo(base, altura) que devuelva el área
# del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo
# de 15 de base y 10 de altura:

def area_rectangulo():
    base = 15
    altura = 10

    area = 15*10

    print("El área del rectángulo es: ", area)

print("EJERCICIO 1")
area_rectangulo()

print("==================================================")


# EJERCICIO 3
#
# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
#
# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

def relacion(a, b):

    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


print("EJERCICIO 3")
a = input("introduce un número: ")
b = input("introduce otro número: ")

print(relacion(a, b))

print("==================================================")

# EJERCICIO 6
#
# Realiza una función separar(lista) que tome una lista de números enteros
# y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

def separar(lista):

    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

print("EJERCICIO 6")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar(lista)

print("Los número pares son: ", pares)
print("Los número impares son: ", impares)

print("==================================================")



