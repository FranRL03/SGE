print("Hola Mundo")

saludo = "Miarma que cosa más grande er Python"

def saludar():
    # esta variable edita el valor de la variable en todos lados,
    # sin el "global" solo afectaria a la variable del metodo
    global saludo
    saludo = "Hola a todos"
    # print(msg)
    print(saludo)

saludar()

print(saludo)

def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))

dibujar_tabla_del_5()

def coord(ciudad):

    if ciudad == 'Sevilla':
        return 38.1234,-6.4567
    else:
        return 0,0

lat, long = coord('Sevilla')

def suma(a,b):
    return a+b

print(lat)
print(long)

print(suma(b=30, a=10))

# ARGUMENTOS INDETERMINADOS

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",[1,2,3,4,5])

def indeterminados_nombre(**kwargs):
    print("Mira tu:", kwargs["n"])
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])