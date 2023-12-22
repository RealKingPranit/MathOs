import math #ofc we need math
import os
import time #for making them wait

def set_cmd_title(title):
    os.system(f"echo \033]0;{title}\a")

#Pythogoras Theorm
def execute_option():
    title = "Pythogoras"
    set_cmd_title(title)
    a = int(input("What will be the first value:"))
    b = int(input("What will be the second value:"))
    c = a^2 + b^2 # Pythogoras therom's formula [a^2 + b^2 = c^2]
    print('Here:',c)
    c_in_root = math.sqrt(c) #just incase if you wanted the result's Square root :D
    print('Here in roots :',c_in_root)
    from menu import menu
    time.sleep(3)#3 seconds :)
    menu()
execute_option()