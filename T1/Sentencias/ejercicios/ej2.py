"""
Crea un programa que:
- Crea un diccinario llamado persona con:
    -name, age, height
    -color (arrays)
    -animales (array vacio)
    -location (x,y). Es una tupla. Los valores que querais

-Pide por consola un color y lo añades a colors.
-Sustiituye el primer color de la lista por "black" o "negro"
-Pide por consola una mascota (name y type). Añadeles como diccionario a la lista.

Procurad que los f0r àra pedir informacion por consola iteren 3 veces.
Mostrar por pantalla pets y muestre: El "clave" es "valor" para cada mascota añadida.

"""
from tkinter.font import names

persona = {
    "name": "Josue",
    "age": 20,
    "height": 1.58,
    "colors": ["white", "green", "red"],
    "animales": [], # {"name": "", "type": ""}
    "location": (12, 17)
}

print(persona)
for i in range(3):
    color = input ("Introduce el color: ")
    persona["colors"].append(color)

print("Añador colores: ")
print(persona)
print()
print("Cambiar primer color de la lista por negro: ")
persona["colors"][0] = "negro"
print(persona)
print()

for i in range(2):
    name = input("Introduce el nombre de un animal: ")
    tipo = input("Introduce el tipo del animal: ")
    print()
    persona["animales"].append({
        "name": name,
        "type": tipo
    })
print(persona["animales"])

for pet in persona["animales"]:
    print(f"El {pet['name']} es {pet['type']}")

    for clave, valor in pet.items():
        print(f"El {clave} es {valor}")