palabra = "Python"
print(palabra[0:2])
print(str(5))

lista1 = [1,2,3,4,5]
lista2 = list([1,2,3,4,5])

print(lista1[-2:])

listaMixta = ["Pi", 3.14, None, -15]

print(lista1 + listaMixta)

n = 1

if(n > 0):
    print("Mayor")
else:
    print("menor")
    print(n)

# Una tupla no se puede modificar, para añadir un elemento se puede hacer:

print("Añadimos elemento a la tupla")

t = (1,2,3)
t2 = (1,2,3) + (4,)

print(t2)
