def carga_palabras():
    palabra = []

    with open("palabras.txt", "r") as archivo: 
            for linea in archivo:
                palabra = linea.strip() # Borrar los espacios en blanco
                palabras.append(palabra) # Añadimos la palabra al array

    return palabras

# Menú principal
print("==================")
print("[1] Importar palabras clave")
print("[2] Mostrar palabras clave")
print("[0] Salir")
print("==================")

palabras = []  
contador = 1 

while True:
    print("\nIntroduzca un número")
    op = input()

    if op == "1":
        palabras = carga_palabras()
        print("\nPalabras clave cargadas exitosamente.")

    elif op == "2":
        print("\nPalabras clave:\n")
        palabras.sort()
        for i in range(len(palabras) - 1):
            if palabras[i] == palabras[i + 1]:
                contador += 1
            else:
                print(f'{palabras[i]}, veces repetidas: {contador}')
                contador = 1

        # Imprimir la última palabra y su frecuencia ya que la última
        # palabra no tiene otra para compararla entonces la emprimimos directamente
        print(f'{palabras[-1]}, veces repetidas: {contador}')

    elif op == "0":
        print("\nSaliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")

print("Programa finalizado.")

