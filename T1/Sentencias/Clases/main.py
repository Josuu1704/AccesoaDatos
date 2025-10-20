import random


class Persona:
# 1 _ es protegido, 2 __ es privado
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__id = self.__generate_id()

    def __generate_id(self):
        return random.randint(10000,999999)

    def get_nombre(self):
        return  self.__nombre

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"{self.__nombre} y el id es {self.get_id()}"


persona = Persona("Josue")

print(persona.get_nombre())
print(persona.get_id())
print(persona)

class Producto:
    def __init__(self,nombre,cantidad,precio):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    def get_total(self):
        return  self.__cantidad * self.__precio

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def descuento(self,desscuento):
        self.__precio -= desscuento
    def __str__(self):
        return f"[Nombre: {self.__nombre}, Cantidad:{self.__cantidad}, Precio: {self.__precio}]"

presupuesto = 2200
p1 = Producto("TV", 3, 350)
p2 = Producto("PC", 1, 1900)

print(p1)
