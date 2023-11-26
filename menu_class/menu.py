from objects import tasks_lib as task


def get_variant_number() -> int:
    variant = int(input('Enter variant number: '))

    while variant < 1 or variant > 14:
        variant = int(input('between 1 and 14 pls\nEnter variant number: '))

    return variant


def get_task_number() -> int:
    task_number = int(input('Enter task number: '))

    while task_number < 1 or task_number > 2:
        task_number = int(input('Between 1 and 2 pls\nEnter task number: '))

    return task_number


class Menu:

    def __init__(self):
        self.__tasks_dict = {
            1.1: task.TasksLib().get_first_var_first_task(),
            1.2: task.TasksLib().get_first_var_second_task(),
            2.1: task.TasksLib().get_second_var_first_task(),
            2.2: task.TasksLib().get_second_var_second_task(),
            3.1: task.TasksLib().get_third_var_first_task()
        }

    def call_menu(self):
        variant = get_variant_number()
        task_number = get_task_number()
        key = variant + float(task_number / 10)

        self.__tasks_dict[key].get_result()
