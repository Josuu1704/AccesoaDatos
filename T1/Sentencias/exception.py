try:
    # Intenta hacer algo, perso si te ecnuetras con un error paras completamente y pasas al except
    pass
except:
    #si hay un error en el try, accedemos aqui
    pass


def error_division(numero, div):
    try:
        print(numero/div)
    except ZeroDivisionError:
        print("no se puded dividir entre cero")

def imprimer_valor_string(numero):
    try:
        print("El numero es: ", int(numero))
    except ValueError:
        print("El valor debe ser numerico")
    finally:
        print("Este es el mensaje de finally")


error_division(1,0)
error_division(1,2)
