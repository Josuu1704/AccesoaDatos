try:
    # Intenta hacer algo, pero si te encuentras con un error paras completamente y pasas al except
    pass
except:
    # Si hay un error en el try, accedemos aquí
    pass


def error_division(numero, div):
    try:
        print(numero / div)
    except TypeError:
        print("Un valor no es un numero")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")


def imprime_valor_number(numero):
    try:
        print("El numero es:", int(numero))
    except ValueError:
        print("El valor debe de ser numérico")
    finally:
        print("Este es el mensaje de finally")


def set_rating(value):
    try:
        if not (0 <= value <= 10):
            raise ValueError("Rating debe de estar entre 0 y 10")
        print(value)
    except TypeError:
        print("El valor solo puede ser un numero")


error_division(1, 0)
print()
error_division(1, "0")
print()
error_division(1, 2)
print()
imprime_valor_number("hola")
print()

try:
    set_rating(11)
except ValueError as e:
    print(e)