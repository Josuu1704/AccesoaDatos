## Biblioteca
"""Creemos un programa que gestione una pequeña colección de libros en una biblioteca usando una clase llamada Book (Intentemos crear códigos en archivos diferentes).

- Cada libro debe de tener los siguientes atributos privados:
  - __title: Título del libro (No puede estar vacío ni numérico además, el tamaño del título debe de ser de más de 5 caracteres).
  - __author: Nombre del autor que escribió el libro (No puede estar vacío ni numérico).
  - __price: Precio en euros (solo números positivos).
  - __isbn: Código de identificación único (Igual que el ID que creamos en el anterior, pero la cantidad de caracteres aquí serán de 25).

- El programa debe de validar con ValueError los errores mencionados anteriormente.
- Implementa una propiedad de descuento. Será True si vale más de 25.00/False si no lo hace. Además, antes de retornar, descontará al precio original 10€ en caso de ser True.
- Implementa el método __str__ para mostrar:
  - [ISBN: numero] "Nombre del libro" de "Nombre de autor" -> Precio€ """
import random


class Book():
    def __init__(self, title, author, price, isbn):
        if not title and not author:
            raise ValueError("El titulo/autor no puede estar vacio")
        if title.isnumeric and author.isnumeric():
            raise ValueError("El titulo/autor no puede ser un numero")
        if len(title) > 5:
            raise ValueError("El titulo debe contener mas de 5 caracteres")
        if price < 0:
            raise ValueError("El precio no puede ser negativo")

        self.__title = title
        self.__author = author
        self.__price = price
        self._isbn = self.__autogenerate_isbn()

    @staticmethod
    def __autogenerate_isbn():
        return random.randint(0,25)

    def __str__(self):
        return f"[ISBN: {self._isbn}] {self.__title} de {self.__author} -> Precio: {self.__price}€"
