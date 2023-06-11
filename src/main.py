import subprocess
import readchar
import os


def display_menu(selected_row, menu_options):
    for i, (task_name, _) in enumerate(menu_options.items()):
        if i == selected_row:
            print(f"> {task_name}")
        else:
            print(f"  {task_name}")


def perform_task(task, menu_options):
    task_function = menu_options[task]
    if task_function is not None:
        print(f"performing {task}...")
        task_function()
    else:
        print("Invalid task selected.")
    input("Press Enter to continue...")


def main():

    # some example for menu
    main_menu = {
        "print all file and folder in current directory": current_dir,
        "ping": ping,
        "Exit": exit
    }
    selected_row = 0

    while True:
        os.system('clear')  # Clear console
        display_menu(selected_row, main_menu)
        key = readchar.readkey()

        if key == '\x1b[A':  # Up arrow
            selected_row = max(selected_row - 1, 0)
        elif key == '\x1b[B':  # Down arrow
            selected_row = min(selected_row + 1, len(main_menu) - 1)
        elif key == '\n' or key == '\r':
            task_name = list(main_menu.keys())[selected_row]
            perform_task(task_name, main_menu)

        if key == 'q' or key == 'Q':
            break


def current_dir():
    print("getting files and folders in current directory...")
    subprocess.call(['sh', "cuDirectory.sh"])


def ping():
    ip = input("enter ip you want to ping: ")
    print(f"pinging {ip}...")
    subprocess.call(['sh', "ping.sh", ip])
    # Add your logic for Task 2 here


def task3_function():
    print("Performing Task 3...")
    # Add your logic for Task 3 here


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
