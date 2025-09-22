n: int = 12
arr_1 = [1, 2, 3]

if n > 6:
    if 2 in arr_1:
        print("Si está 2")
    else:
        print("No está 2")
else:
    print("No es 12")

if n == 6:
    print("Es 6")
elif n == 12:
    print("Es 12")
else:
    print("No es ninguno de los anteriores [6, 12]")


nombre: str = "Camilo"
mi_edad: int = 27
edad_usuario: int = 30
altura: float = 180
colores: list[str] = ["Blanco", "Azul", "Rojo"]

if mi_edad > edad_usuario:
    print("Soy mayor que el usuario")
elif mi_edad == edad_usuario:
    print("Tenemos la misma edad")
else:
    print("Soy menor que el usuario")
