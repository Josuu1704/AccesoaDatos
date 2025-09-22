palabra = "Hola mundo"
arr_1: list = [1, 2, 3, 4, 5]

for letra in palabra:
    print(letra)

print()
for elemento in arr_1:
    print(elemento)

print()

for n in range(10):
    print(n)

print()
for j in range(10, 0, -2):
    print(j)

arr_2 = [k for k in range(10)]

arr_3 = []
for z in range(10):
    if z % 2 != 0:
        arr_3.append(z)


print(arr_2)
print(arr_3)

print()
for x in arr_2:
    if x % 2 == 0:
        print(x)

salir = False
cont = 0
# while not salir and cont < len(arr_2):
#     if arr_2[cont] == 4:
#         print("Salimos porque lo encontramos")
#         salir = True
#     cont += 1


while not salir and cont < len(arr_3):
    if arr_3[cont] % 2 == 0:
        print("Hemos encontrado un numero par")
        salir = True
    cont += 1

# En JAVA usamos el elemento.length
print("\nElementos que tiene el arr_3 usando len")
for i in range(len(arr_3)):
    print(i)


dict_1: dict = {
    "nombre": "Camilo",
    "apellido": "Quiroz Muñoz",
    "email": "juan.camilo.quiroz@profesorado.epsum.school",
}


for clave in dict_1:
    print(clave , ", ", dict_1[clave])

print()
for clave, valor in dict_1.items():
    print(clave, ": ", valor)

print()
for clave in dict_1.keys():
    print(clave , ", ", dict_1[clave])

print()
for valor in dict_1.values():
    print(valor)











