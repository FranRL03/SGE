class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# CREACION DE CLIENTE

c = Cliente('12345678A', 'Francisco Javier', 'Ruiz Lebron')
print(c)
print(c.nombre)

# la clase no tiene el atributo email pero c si lo tiene porque se lo hemos establecido
# en cambio si creamos un Cliente c2, este no tendria el atributo email

c.email = 'fran@gmail.com'
print(c.email)