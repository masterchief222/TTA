import os
import readchar
import colorama
def display_menu(selected_row: int, menu_options: dict):
    max_len = max(len(item) for item in menu_options.keys())

    for i, (task_name, _) in enumerate(menu_options.items()):
        if i == selected_row:
            print(colorama.Fore.GREEN +
                  f"  {task_name}".center(max_len + 4) + colorama.Style.RESET_ALL)
        else:
            print(f"  {task_name}".center(max_len + 4))
    print(f"\n  {'-'*max_len}\n".center(max_len + 4))


def perform_task(task: str, menu_options: dict):
    task_function = menu_options[task]
    if task_function is not None:
        if task_function == "Exit":
            return None  # Exit the current menu level
        else:
            print(colorama.Fore.BLUE +
                  f"performing {task}..." + colorama.Style.RESET_ALL)
            task_function()
    else:
        print("Invalid task selected.")
    if not task.endswith("menu"):
        return input(colorama.Fore.BLUE+"\nPress Enter to continue..."+colorama.Style.RESET_ALL)
    else:
        return 1


def show(menu: dict, menu_name=""):
    selected_row = 0

    while True:
        os.system('clear')  # Clear console
        if menu_name != "":
            print(f"------ {menu_name} ------\n")
        display_menu(selected_row, menu)
        key = readchar.readkey()

        if key == '\x1b[A':  # Up arrow
            selected_row = max(selected_row - 1, 0)
        elif key == '\x1b[B':  # Down arrow
            selected_row = min(selected_row + 1, len(menu) - 1)
        elif key == '\n' or key == '\r':
            task_name = list(menu.keys())[selected_row]
            result = perform_task(task_name, menu)
            if result is None:
                return  # Exit the current menu level

        if key == 'q' or key == 'Q':
            break


def show_delete_menu(menu: list):
    selected_row = 0

    while True:
        os.system('clear')  # Clear console
        display_delete_menu(selected_row, menu)
        key = readchar.readkey()

        if key == '\x1b[A':  # Up arrow
            selected_row = max(selected_row - 1, 0)
        elif key == '\x1b[B':  # Down arrow
            selected_row = min(selected_row + 1, len(menu) - 1)
        elif key == '\n' or key == '\r':
            if selected_row == len(menu) - 1:
                return
            while True:

                confirmation = input(
                    colorama.Fore.YELLOW + "Are you sure?(y/n)" + colorama.Style.RESET_ALL)
                if confirmation.lower() == "y":
                    return menu[selected_row]
                elif confirmation.lower() == "n":
                    break

        if key == 'q' or key == 'Q':
            break


def display_delete_menu(selected_row: int, menu_options: list):
    max_len = max(len(item) for item in menu_options)

    for i, (task_name) in enumerate(menu_options):
        if i == selected_row:
            print(colorama.Fore.GREEN +
                  f"  {task_name}".center(max_len + 4) + colorama.Style.RESET_ALL)
        else:
            print(f"  {task_name}".center(max_len + 4))
