"""
Crea un programa en Python que permita gestionar una lista de tareas pendientes utilizando
funciones y manejo de excepciones. El programa debe almacenar las tareas en una lista llamada
tasks, donde cada elemento será una cadena de texto. Se deben crear funciones para añadir,
eliminar y mostrar tareas. La función add_task(task: str, task_list: list[str]) debe añadir una
tarea a la lista, pero antes debe comprobar que el texto no esté vacío y que no sea numérico; en
caso de incumplir estas condiciones, deberá lanzar una excepción ValueError con un mensaje adecuado.
La función remove_task(task: str, task_list: list[str]) debe eliminar la tarea indicada si existe,
y lanzar un ValueError si el elemento no se encuentra en la lista. La función show_tasks(task_list: list[str])
debe mostrar todas las tareas numeradas, y si la lista está vacía, debe lanzar un ValueError indicando
que no hay tareas registradas.

En el programa principal debe implementarse un menú en bucle que permita al usuario elegir entre cuatro opciones:
    - 1. Añadir una nueva tarea,
    - 2. Eliminar una tarea existente.
    - 3. Mostrar la lista completa de tareas.
    - 4. Salir del programa.

Cada opción debe ejecutarse dentro de un bloque try/except (Si se requiere) para capturar y mostrar
los mensajes de error sin que el programa se detenga. Los mensajes deben ser claros, mostrando
confirmaciones cuando una acción se realice correctamente y avisos cuando ocurra algún error
(por ejemplo, si el usuario intenta eliminar una tarea inexistente o introduce un valor no válido).
El programa debe continuar ejecutándose hasta que el usuario elija la opción de salir.
"""

task_list = []
def comprobar_task(tarea):
    if not tarea:
        raise ValueError("Error. El task esta vacio.")
    if tarea.isnumeric():
        raise ValueError("Error el task debe ser un String")


def add_task():
        tarea = input("Introduce una tarea a realizar: ")
        comprobar_task(tarea)


def menu():
    print()
    salir = False
    while not salir:
        print("---- MENU ----")
        print("1.Añadir tarea")
        print("2.Eliminar tarea existente")
        print("3. Mostrar lsta de tareas")
        print("4. Salir")

        option = int(input("Introduce la opcion que quieras: "))
        if option == 1:
            try:
                add_task()
            except ValueError as  e:
                print(e)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            salir = True
            print("Saliendo del programa...")
        else:
            print("Opcion no valida.")

def main():
    menu()

main()