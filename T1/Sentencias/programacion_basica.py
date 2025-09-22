# Esto es un comentario

"""
Mensaje en líneas
Este es un comentario
"""

x: str = "hola"
y: str = 'hola'
n: int = 12
n_m: float = 12.2
val: bool = True
val_not = False

arr_1 = [1, 2, 3]
tpl = (1, 2, 3)

dict_1 = {}
dict_2: dict = dict

dict_3 = {  # DICCIONARIO
    "a": "Valor 1",
    "b": "Valor 2",
    "c": [1, 2, 3],
    "d": True,
    "e": False,
    "f": {
        "g": "Valor 3",
        "h": "Valor 4"
    }
}

dict_4 = '{ "a": "Valor 1", "b": "Valor 2", "c": [1, 2, 3], "d": True,}'  # JSON

print(arr_1[1])  # -> 2
print()

print(tpl[0])  # -> 1
print()

print(dict_3["d"])  # -> True
print()

valor_consola = input("Introduce el valor de la consola: ")
print(valor_consola)

edad_1 = int(input("Introduce la edad: "))
print(edad_1)




