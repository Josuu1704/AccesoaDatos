persona = {
    "nombre": "Camilo",
    "apellido": "Quiroz Muñoz",
    "esEstudiante": True,
    "frutas": ["manzana", "pera"],
    "estaDeVacaciones": False,
    "animales": [{"animal1": "perro"}, {"animal2": "gato"}]
}

print(persona)
print(persona["nombre"])  # Acceder a un valor haciendo uso de su clave
print()

if persona["esEstudiante"]:
    print("Es estudiante")
else:
    print("Es profesor")

print()
for fruta in persona["frutas"]:
    print(fruta)

# print(persona.get("estaDeVacaciones", "No está definido"))
estaDeVacaciones = persona.get("estaDeVacaciones", False)  # Obtener un dato de un diccionario
print(estaDeVacaciones)

persona.pop("estaDeVacaciones")  # Borramos Clave-Valor del diccionario. Dejamos basura en memoria
print(persona)

del persona["frutas"]  # Borrar Clave-Valor pero también de la memoria
print(persona)

# persona.clear()  # Limpiamos el diccionario. Borramos todo de la memoria.
# print(persona)

persona["esEstudiante"] = False  # Podemos sobreescribir el valor de una clave
print()
for clave, valor in persona.items(): # Accedemos a la Clave-Valor de cada elemento por iteración
    print(f"La clave es {clave} y su valor es {valor}")

print()
for value in persona.values(): # Accedemos SOLO a los valores de un diccionario
    print(value)

print()
for clave in persona.keys(): # Accedemos SOLO a las claves de un diccionario
    print(clave)

print()
for elemento in persona["animales"]:
    for clave, valor in elemento.items():
        print(f"El {clave} es {valor}")

clave_consola = input("Introduce la clave: ")
valor_consola = bool(input("Introduce el valor: "))
persona[clave_consola] = valor_consola
print()
print(persona)
