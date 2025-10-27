from ej2 import Book

val = True
biblioteca = []

while val:
    print("1. Crear libros")
    print("2. Ver mis libros")
    print("1. Salir")
    opt = int(input(">> "))

    try:
        if opt == 1:
            print("\n")
            title = input(">> >> Titulo: ")
            author = input(">> >> Autor: ")
            price = int(input(">> >> Price: "))
            book = Book(title, author, price)
            biblioteca.append(book)
        elif opt == 2:
            for book in biblioteca:
                print(book)
        elif opt == 3:
            val = False
        else:
            print("Opcion no valida")
    except ValueError as e:
        print("[Error]", e, sep="=>")
