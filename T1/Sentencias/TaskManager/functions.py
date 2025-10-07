def add_task(task, task_list):
    pass

def remove_task():
    pass

def show_task(task_list):
    if len(task_list) == 0:
        print("No hay tareas disponibles")
    else:
        for i in range(len(task_list)):
            print(f"{i} --> {task_list[i]}")
