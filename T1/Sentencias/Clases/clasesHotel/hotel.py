import random
import secrets


class Reserva:
    def __init__(self,name):
        self.__name = name
        self.__noches = random.randint(1,7)

    @property
    def __autogenerateCode(self):
        return secrets.token_hex(16)
