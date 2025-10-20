"""Vamos a modelar una clase Student que represente a un alumno.

- Crearemos un array que gestionará varios alumnos.
- Cada alumno tendra atributos name, grades (lista de notas de 0 a 10), id que será un código de identificación única (autogenerado). Estos atributos son privados.

Los requisitos de la clase son los siguientes:
    - El nombre se asigna en el constructor y debe validarse. (No puede ser numérico ni estar vacío). Si no es válido debe de lanzar un error ValueError.
    - Las notas comienzan con una lista privada vacía. Pero se podrán añadir mediante un método add_grade(nota) o add_grade() (si pedis las notas fuera de esta clase).,
    - Implementa una propiedad llamada media, que devolverá el promedio de las notas. (Si no hay notas, retorna 0).
    - getters y setters para name.
    - Implementa el método __str__ para mostrar:
        - [ID: valor] Nombre -> Notas: [n1, n2, n3,...] | Media: nota"""
import random


class Student:
    alumnos = []

    def __init__(self, name):
        if not name or name.isnumeric():
            raise ValueError("El nombre no pued estar vacio ni ser un numero")
        self.__name = name
        self.__grade = []
        self.__id = self.__generate_id()

    def __generate_id(self):
        return random.randint(1000, 9999)

    def get_name(self):
        return self.__name

    def __set_name__(self, name):
        self.__name = name
        if len(name) == 0:
            raise ValueError("El nombre no puede estar vacio")
        if name.isNumeric():
            raise ValueError("La tarea no puede estar vacia")

    def add_grade(self, grade):
        self.__grade.append(grade)

    @property
    def media(self):
        if not self.__grade:
            return 0
        return sum(self.__grade) / len(self.__grade)


    def __str__(self):
        return f"[ID: {self.__id}] {self.__name}: Notas: [{self.__grade}] / Media nota: {self.media}"

a1 = Student("JOsue")

a1.add_grade(8)
a1.add_grade(7)

print(a1)
