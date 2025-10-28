from hotel import Reserva

val = True
huespedes = []

while val:
    print("--- HOTEL EPSUM ---")
    print("1. Añadir huésped.")
    print("2. Ver huéspedes.")
    print("3. Filtrar habitaciones.")
    print("4. Suma total del dinero pagado por los huéspedes en el hotel.")
    print("5. Salir")
    opt = int(input(">> "))

    try:
        if opt == 1:
            print("\n")
            name = input(">> >> Introduce el nombre del huésped: ")
            huesped = Reserva(name)
            huespedes.append(huesped)
        elif opt == 2:
            if len(huespedes) == 0:
                print("No hay huespedes registrados")
            else:
                for huesped in huespedes:
                    print(huesped)
        elif opt == 3:
            if len(huespedes) == 0:
                print("No hay huespedes regitrados.")
            else:
                tipo = int(input("Que tipo de habitaion quieres filtrar (individual -> 1) o (doble -> 2): "))
                habitaciones = 0

                if tipo == 1:
                        for huesped in huespedes:
                            if tipo == huesped.tipo_habitacion:
                                print(huesped)
                                habitaciones += 1
                        if habitaciones == 0:
                            print("No hay habitaciones individuales registradas")
                elif tipo == 2:
                    for huesped in huespedes:
                        if tipo == huesped.tipo_habitacion:
                            print(huesped)
                            habitaciones += 1
                    if habitaciones == 0:
                        print("No hay habitaciones dobles registradas")
                else:
                    print("Tiene que ser doble o individual")

        elif opt == 4:
            total_pagado = 0
            if len(huespedes) == 0:
                print("No hay huespedes registrados")
            else:
                for huesped in huespedes:
                    total_pagado += huesped.total_pagado
            print(f"\nTotal del dinero pagado por todos los huéspedes: {total_pagado:.2f}€")
        elif opt == 5:
            val = False
        else:
            print("Opcion no valida...")
    except ValueError as e:
        print("[ERROR]", e, sep=" => ")
