import time
import os

def set_cmd_title(title):
    os.system(f"echo \033]0;{title}\a")

def secondD():
 title = "2D"
 set_cmd_title(title)
 os.system('cls')
 def rectangle():
    print('Rectangle:')
    l = int(input("Enter length: "))
    b = int(input('Enter breadth: '))
    perimeter = 2 * (l + b)
    area = l * b
    print('Area:', area)
    print('Perimeter:', perimeter)
    time.sleep(0.5)

 def square():
    print('Square:')
    a = int(input('Enter a number: '))
    sqr_perimeter = 4 * a
    sqr_area = a ** 2
    print('Area:', sqr_area)
    print('Perimeter:', sqr_perimeter)
    time.sleep(0.5)

 def circle():
    print('Circle:')
    r = int(input('Enter the number: '))
    d = 2 * r
    pi = 3.14
    c = 2 * pi * r
    cir_area = pi * (r ** 2)
    print('Diameter:', d)
    print('Circumference:', c)
    print('Area:', cir_area)
    time.sleep(0.5)

 def plane_dimension():
    while True:
        print('Main Menu (2D)')
        print('1. Rectangle')
        print('2. Square')
        print('3. Circle')
        print('4. Exit')

        selected = input('Enter your choice (1-4): ')

        if selected == '1':
            rectangle()
        elif selected == '2':
            square()
        elif selected == '3':
            circle()
        elif selected == '4':
            print("Exiting the program...")
            execute_option()
        else:
            print('Invalid choice. Please enter a number between 1-4.')

 # Call the function to start the program
             
 plane_dimension()

def thirdD():
   title = "3D"
   set_cmd_title(title)
   os.system('cls')
   def Cube():
      print('Cube:')
      a = int(input('Enter a Number:'))
      lsa = 4*a
      tsa = 6*a
      v = a^3
      time.sleep(1.5)
      print('TSA:',tsa)
      print('LSA:',lsa)
      print('Volume',v)

   def Cilender():
      print('Cylinder:')
      pi = 3.14
      r = int(input('Enter the Radius:'))
      h = int(input('Enter Hight:'))
      csa = 2*pi*r*h
      tsa = 2*pi*r*(r+h)
      v = pi*r*r*h
      time.sleep(1.5)
      print('CSA:',csa)
      print('TSA:',tsa)
      print('Volume:',v)

   def Cuboid():
      print('Cuboid:')
      l = int(input('Enter the length:'))
      b = int(input('Enter the breadth'))
      h = int(input('Enter the Hight:'))
      lsa = 2*h*(l+b)
      tsa = 2*(l*b+b*h+l*h)
      v = l*b*h
      time.sleep(1.5)
      print('TSA:',tsa)
      print('LSA:',lsa)
      print('Volume:',v)   
   while True:
      print('Main Menu (3D)')
      print('1. Cube')
      print('2. Cilender')
      print('3. Cuboid')
      print('4. Exit')


      selected = input('Enter Your choice (1-4)')

      if selected == '1':
         Cube()
      elif selected == '2':
         Cilender()
      elif selected == '3':
         Cuboid()
      elif selected == '4':
         execute_option()
         break
      else:
           print('Invalid choice. Please enter a number between 1-4.')          
      

def set_cmd_title1(title1):
    os.system(f"echo \033]0;{title1}\a")

from pick import pick
def execute_option():
   title1 = "Mensuration"
   set_cmd_title1(title1) 
   options = ['3D', '2D', 'Exit']
   title = 'Main Menu'
   selected = pick(options, title)[0]
   if selected == '3D':
        thirdD()
   elif selected == '2D':
        secondD()
   else:
        from menu import menu
        menu()
execute_option()