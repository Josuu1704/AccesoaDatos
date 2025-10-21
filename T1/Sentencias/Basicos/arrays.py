arr_1: list = [10, 20, 30]
frutas: list[str] = ["manzana", "pera", "uva"]

for elemento in arr_1:
    print(elemento)

print()
for fruta in frutas:
    print(fruta)

frutas.append("mango")  # Añadir un elemento al final de la lista
print()
for fruta in frutas:
    print(fruta)

# pop() Eliminamos el último elemento de la lista. Si le ponemos un index/posición borramos es el elemento de esa posición
frutas.pop(0) # Borramos manzana
print()
for fruta in frutas:
    print(fruta)

frutas.insert(0, "banana")
frutas.insert(2, "sandia")
print()
for fruta in frutas:
    print(fruta)

print()
print(frutas[1])

# Si el valor no existe da un error de tipo ValueError
frutas.remove("uva") # Borrar un elemento con un valor específico
print()
for fruta in frutas:
    print(fruta)

frutas.sort() # Ordenar de forma alfabética el arrayList
print()
for fruta in frutas:
    print(fruta)

print()
frutas.append("banana")
print(frutas.count("banana")) # Cuenta cuantos elementos hay de ese tipo en el array

print(f"Hay {frutas.count("banana")} banana dentro de frutas")
