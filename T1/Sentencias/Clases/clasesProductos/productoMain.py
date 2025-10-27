from Producto import Product

lista = []
val = True

while val:
    print("1. Añadir producto.")
    print("2. Mostrar producto/s.")
    print("3. Ver si los productos estan activos.")
    print("4. Salir.")
    opt  = int(input(">> "))
    
    try:
        if opt == 1:
            print("\n")
            name = input("Introduce el nombre del producto: ")
            price = float(input("Introduce el precio del producto: "))
            producto = Product(name,price)
            lista.append(producto)
        elif opt == 2:
            if len(lista) == 0:
                print("No hay productos en el carrito")
            else:
                for producto in lista:
                    print(producto)
        elif opt == 3:
            if len(lista) == 0:
                print("No productos en el carrito.")
            else:
                for producto in lista:
                    print(producto, producto.isActve, sep="\t\t")
        elif opt == 4:
            val = False
        else:
            print("Opcion no valida")
    except ValueError as e:
        print("[Error]", e, sep="=>")
