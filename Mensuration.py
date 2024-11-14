import time
import os

def set_cmd_title(title):
    os.system(f"echo \033]0;{title}\a")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def secondD():
    title = "2D"
    set_cmd_title(title)

    def rectangle():
        clear_screen()
        print('Rectangle:')
        try:
            l = float(input("Enter length: "))
            b = float(input('Enter breadth: '))
            perimeter = 2 * (l + b)
            area = l * b
            print('Area:', area)
            print('Perimeter:', perimeter)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        time.sleep(1.5)

    def square():
        clear_screen()
        print('Square:')
        try:
            a = float(input('Enter side length: '))
            perimeter = 4 * a
            area = a ** 2
            print('Area:', area)
            print('Perimeter:', perimeter)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        time.sleep(1.5)

    def circle():
        clear_screen()
        print('Circle:')
        try:
            r = float(input('Enter the radius: '))
            diameter = 2 * r
            pi = 3.14
            circumference = 2 * pi * r
            area = pi * (r ** 2)
            print('Diameter:', diameter)
            print('Circumference:', circumference)
            print('Area:', area)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        time.sleep(1.5)

    def triangle():
        clear_screen()
        print('Triangle:')
        try:
            b = float(input('Enter base length: '))
            h = float(input('Enter height: '))
            area = 0.5 * b * h
            print('Area:', area)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        time.sleep(1.5)

    def trapezoid():
        clear_screen()
        print('Trapezoid:')
        try:
            a = float(input('Enter length of side a: '))
            b = float(input('Enter length of side b: '))
            h = float(input('Enter height: '))
            area = 0.5 * (a + b) * h
            print('Area:', area)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        time.sleep(1.5)

    while True:
        clear_screen()
        print('Main Menu (2D)')
        print('1. Rectangle')
        print('2. Square')
        print('3. Circle')
        print('4. Triangle')
        print('5. Trapezoid')
        print('6. Exit')

        selected = input('Enter your choice (1-6): ')

        if selected == '1':
            rectangle()
        elif selected == '2':
            square()
        elif selected == '3':
            circle()
        elif selected == '4':
            triangle()
        elif selected == '5':
            trapezoid()
        elif selected == '6':
            print("Exiting to main menu...")
            return
        else:
            print('Invalid choice. Please enter a number between 1-6.')

def thirdD():
    title = "3D"
    set_cmd_title(title)

    def cube():
        clear_screen()
        print('Cube:')
        try:
            a = float(input('Enter side length: '))
            lsa = 4 * a**2
            tsa = 6 * a**2
            v = a**3
            print('TSA:', tsa)
            print('LSA:', lsa)
            print('Volume:', v)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        time.sleep(1.5)

    def cylinder():
        clear_screen()
        print('Cylinder:')
        pi = 3.14
        try:
            r = float(input('Enter the radius: '))
            h = float(input('Enter height: '))
            csa = 2 * pi * r * h
            tsa = 2 * pi * r * (r + h)
            v = pi * r**2 * h
            print('CSA:', csa)
            print('TSA:', tsa)
            print('Volume:', v)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        time.sleep(1.5)

    def cuboid():
        clear_screen()
        print('Cuboid:')
        try:
            l = float(input('Enter length: '))
            b = float(input('Enter breadth: '))
            h = float(input('Enter height: '))
            lsa = 2 * h * (l + b)
            tsa = 2 * (l * b + b * h + l * h)
            v = l * b * h
            print('TSA:', tsa)
            print('LSA:', lsa)
            print('Volume:', v)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        time.sleep(1.5)

    def sphere():
        clear_screen()
        print('Sphere:')
        pi = 3.14
        try:
            r = float(input('Enter radius: '))
            surface_area = 4 * pi * r**2
            volume = (4/3) * pi * r**3
            print('Surface Area:', surface_area)
            print('Volume:', volume)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        time.sleep(1.5)

    def cone():
        clear_screen()
        print('Cone:')
        pi = 3.14
        try:
            r = float(input('Enter radius: '))
            h = float(input('Enter height: '))
            slant_height = (r**2 + h**2)**0.5
            surface_area = pi * r * (r + slant_height)
            volume = (1/3) * pi * r**2 * h
            print('Surface Area:', surface_area)
            print('Volume:', volume)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        time.sleep(1.5)

    while True:
        clear_screen()
        print('Main Menu (3D)')
        print('1. Cube')
        print('2. Cylinder')
        print('3. Cuboid')
        print('4. Sphere')
        print('5. Cone')
        print('6. Exit')

        selected = input('Enter your choice (1-6): ')

        if selected == '1':
            cube()
        elif selected == '2':
            cylinder()
        elif selected == '3':
            cuboid()
        elif selected == '4':
            sphere()
        elif selected == '5':
            cone()
        elif selected == '6':
            print("Exiting to main menu...")
            return
        else:
            print('Invalid choice. Please enter a number between 1-6.')

def execute_option():
    title = "Mensuration"
    set_cmd_title(title) 
    options = ['3D', '2D', 'Exit']
    from pick import pick
    selected = pick(options, 'Main Menu')[0]

    if selected == '3D':
        thirdD()
    elif selected == '2D':
        secondD()
    else:
        print("Exiting the program...")

# Start the program
execute_option()
