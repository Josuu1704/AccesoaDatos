import random
import secrets


class Reserva:
    def __init__(self,name):
        self.__is_valid_name(name)

        self.__name = name
        self.__noches = random.randint(1,7)
        self.__tipo_habitacion = random.randint(1,2)
        self.__tarifa = random.uniform(30,60)
        self.__descuento = random.uniform(1,100)

    @property
    def __autogenerateCode(self):
        return secrets.token_hex(16)

    @staticmethod
    def __is_valid_name (name):
        if not name:
            raise ValueError ("El nombre no puede estar vacío.")
        if name.isnumeric():
            raise ValueError ("El nombre no puede ser un numero.")

    @staticmethod
    def __is_valid_room(room):
        if room > 2:
            raise ValueError ("Las habitaciones tienen que ser dobles o individuales")
        elif room < 1:
            raise ValueError ("Las habitaciones tienen que ser dobles o individules.")

    @property
    def tipo_habitacion(self):
        return self.__tipo_habitacion

    @property
    def total_pagado(self):
        return self.aplicar_descuento * self.__noches

    @property
    def aplicar_descuento(self):
        return self.__tarifa * (1-self.__descuento / 100)

    def __str__(self):
        return f"[{self.__autogenerateCode}] {self.__name}: {self.__tipo_habitacion} -> [{self.__noches} noches x {self.aplicar_descuento:.2f}€ con descuento:"
