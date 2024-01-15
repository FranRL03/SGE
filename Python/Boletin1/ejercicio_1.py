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

while True:
    print("\nIntroduzca un número")
    op = input()

    if op == "1":
        palabras = carga_palabras()
        print("\nPalabras clave cargadas exitosamente.")
    elif op == "2":
        print("\nPalabras clave:\n")
        for palabra in palabras:
            print(palabra)
    elif op == "0":
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

print("Programa finalizado.")
