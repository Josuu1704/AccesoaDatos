import dataclasses
import random

@dataclasses.dataclass
class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("El nombre no puede estar vacio.")
        if name.isnumeric():
            raise ValueError("El nombre no puede ser numerico")

        self.__name = name
        self.__grades = []
        self.__id = self.__autogeerate_id()
        self.add_grade()

    @staticmethod
    def __autogeerate_id():
        return random.randint(1000,9999)

    def add_grade(self):
        val = True
        while val:
            grade = float(input("Introduce la nota (-1 para salir): "))
            if grade <= -1:
                val = False
            else:
                self.__grades.append(grade)

    @property
    def media(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        return f"[ID: {self.__id}] {self.__name}: Notas: {self.__grades} / Media nota: {self.media:.2f}"