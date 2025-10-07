def ask_number(task_list, option):
    task = input("Introduce una tarea: ")
    if option == 1:
        if task in task_list:
            raise ValueError("La tarea ya existe")
    elif option == 2:
        if task not in task_list:
            raise ValueError("La tarea no exite")
    if not task:
        raise ValueError("La tarea no puede ser vacia")
