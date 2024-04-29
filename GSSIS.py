from Function_Grocery import *

while (True):
    print("- - - - - Welcome to Login Page - - - - -")
    print("")
    print("(1) Login Account\n(2) Sign Up (create new account)\n(3) Exit")
    re = int(input(">>> "))
    if re == 1:
        LOGIN()
    elif re == 2:
        CREATE_ACCOUNT()
    elif re == 3:
        print("Thank You :D")
        break
    else:
        print("Invalid Value")