import random
import secrets


class Product:
    def __init__(self, name, price):
         self.__comprobarName(name)
         self.__comprobarPrice(price)

         self.__name = name
         self.__price = price
         self.__stock = self.__autogenerateStock()

    def __autogenerateStock(self):
        return random.randint(0, 1)

    @property
    def __code(self):
        return secrets.token_hex(16)

    @property
    def isActive(self):
        return self.__stock > 0

    @staticmethod
    def __comprobarName(name):
        if len(name) == "":
            raise ValueError ("El nombre no puede estar vacío.")
        if len(name) < 3:
            raise ValueError ("El nombre tiene que tener mas de 3 caracteres.")

    @staticmethod
    def __comprobarPrice(price):
        if price < 0:
            raise ValueError ("El precio no puede ser menor a cero.")

    def __str__(self):
        return f"[{self.__code}] '{self.__name}' --> Precio '{self.__stock}[{self.__price}€]'"