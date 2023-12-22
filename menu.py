from pick import pick
import importlib
import os

def set_cmd_title(title1):
    os.system(f"echo \033]0;{title1}\a")

def menu():
    title1 = "MathOS.Main_Menu"
    set_cmd_title(title1)
    options = ['Pythogoras', 'Mensuration', 'Exit']
    title = 'Main Menu'
    selected = pick(options, title)[0]

    if selected == 'Pythogoras':
        execute_file('Pythogoras')
    elif selected == 'Mensuration':
        execute_file('Mensuration')
    elif selected == 'Exit':
        exit()

def execute_file(filename):
    try:
        module = importlib.import_module(filename)
        module.execute_option()
    except ModuleNotFoundError:
        print(f"File {filename}.py not found or does not contain the 'execute_option' function.")

# Call the initial menu
menu()
