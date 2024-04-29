import os
# INSERT NEW ITEM
def INSERT_NEW_ITEM():
    with open("inventory.txt","a")as write_file:
        with open("inventory.txt","r")as read_file:
            Co = int(input("Enter the Code of item: "))
            D = input("Enter the Description of item: ").upper()
            C = input("Enter the Category of item: ").upper()
            U = input("Enter the Unit of item: ").upper()
            P = float(input("Enter the Price of item: "))
            Q = int(input("Enter the Quantity of item: "))
            M = int(input("Minimum of item (Avoid item out of stock!): "))
            flag = 0
            lines = read_file.readlines()
            for line in lines:
                value = line.split(",")
                if Co == int(value[0]) or D == value[1]:
                    flag = 1
            if flag == 1:
                print("-"*50)
                print("Unfortunately, You cannot repeat input the information to Inventory txt")
                print("-"*50)
            else:
                sentence = str(Co)+','+D+','+C+','+U+','+str(P)+','+str(Q)+','+str(M)
                write_file.write(sentence)
                write_file.write('\n')
                print("-"*50)
                print("Insert New Item Successfully !")
                print("-"*50)

# UPDATE ITEM
def UPDATE_ITEM():
    with open('inventory.txt','r')as read_file:
        with open('inventory_copy.txt','w')as write_file:
            Co = int(input("Enter the Code of item: "))
            flag = 0
            lines = read_file.readlines()
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if int(value[0]) == Co:
                        print("-"*50)
                        print("\t\tItem Found It !")
                        print("-"*50)
                        print("Description \t: ",value[1])
                        print("Category \t: ",value[2])
                        print("Unit \t\t: ",value[3])
                        print("Price \t\t: ",value[4])
                        print("Quantity \t: ",value[5])
                        print("Minimum \t: ",value[6])
                        print("-"*50)
                        ans = input("You want update this item or not? [Yes/No]: ").lower()
                        if ans == "yes":
                            flag = 1
                            print("-"*50)
                            print("\t\tUpdate Item !")
                            print("-"*50)
                            value[1] = input("Enter the Description of item: ").upper()
                            value[2] = input("Enter the Category of item: ").upper()
                            value[3] = input("Enter the Unit of item: ").upper()
                            value[4] = float(input("Enter the Price of item: "))
                            value[5] = int(input("Enter the Quantity of item: "))
                            value[6] = int(input("Minimum of item (Avoid item out of stock!): "))
                            sentence = value[0]+','+value[1]+','+value[2]+','+value[3]+','+str(value[4])+','+str(value[5])+','+str(value[6])
                            write_file.write(sentence)
                            write_file.write('\n')
                        else:
                            flag = 2
                            write_file.write(line)
                    else:
                        write_file.write(line)
                    
            if flag == 0:
                print("-"*50)
                print("\t\tItem Not Exist !")
                print("-"*50)
            elif flag == 1:
                print("-"*50)
                print("\t\tItem Updated Successfully !")
                print("-"*50)
            elif flag == 2:
                print("-"*50)
                print("\t\tYou Cancel to Update Item !")
                print("-"*50)
    os.remove('inventory.txt')
    os.rename('inventory_copy.txt','inventory.txt')

# DELETE ITEM
def DELETE_ITEM():
    with open('inventory.txt','r')as read_file:
        with open('inventory_copy.txt','w')as write_file:
            Co = int(input("Enter the Code of item: "))
            flag = 0
            lines = read_file.readlines()
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if int(value[0]) == Co:
                        print("-"*50)
                        print("\t\tItem Found It !")
                        print("-"*50)
                        print("Description \t: ",value[1])
                        print("Category \t: ",value[2])
                        print("Unit \t\t: ",value[3])
                        print("Price \t\t: ",value[4])
                        print("Quantity \t: ",value[5])
                        print("Minimum \t: ",value[6])
                        print("-"*50)
                        ans = input("You want delete this item or not? [Yes/No]: ").lower()
                        if ans == "yes":
                            flag = 1
                            continue
                        else:
                            flag = 2
                            write_file.write(line)
                    else:
                        write_file.write(line)
            if flag == 0:
                print("-"*50)
                print("\t\tItem Not Exist !")
                print("-"*50)
            elif flag == 1:
                print("-"*50)
                print("\t\tItem Deleted Successfully !")
                print("-"*50)
            elif flag == 2:
                print("-"*50)
                print("\t\tYou Cancel to Delete Item !")
                print("-"*50)
    os.remove('inventory.txt')
    os.rename('inventory_copy.txt','inventory.txt')

# STOCK TAKING
def STOCK_TAKING():
    with open('inventory.txt','r')as read_file:
        with open('inventory_copy.txt','w')as write_file:
            Co = int(input("Enter the Code of item: "))
            flag = 0
            lines = read_file.readlines()
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if int(value[0]) == Co:
                        print("-"*50)
                        print("\t\tItem Found It !")
                        print("-"*50)
                        print("Description \t: ",value[1])
                        print("Quantity \t: ",value[5])
                        print("-"*50)
                        ans = input("Confirm the Quantity of Item is correct or not? [Yes/No]: ").lower()
                        if ans == "yes":
                            flag = 1
                            write_file.write(line)
                        else:
                            flag = 2
                            print("-"*50)
                            print("\t\tUpdate Quantity of Item !")
                            print("-"*50)
                            value[5] = int(input("Enter the Quantity of item: "))
                            sentence = value[0]+','+value[1]+','+value[2]+','+value[3]+','+str(value[4])+','+str(value[5])+','+str(value[6])
                            write_file.write(sentence)
                            write_file.write('\n')
                    else:
                        write_file.write(line)
            if flag == 0:
                print("-"*50)
                print("\t\tItem Not Exist !")
                print("-"*50)
            elif flag == 1:
                print("-"*50)
                print("\t\t Quantity is Correct !")
                print("-"*50)
            elif flag == 2:
                print("-"*50)
                print("\t\t Quantity Updated Successfully !")
                print("-"*50)
    os.remove('inventory.txt')
    os.rename('inventory_copy.txt','inventory.txt')

# VIEW REPLENISH LIST
def VIEW_REPLENISH_LIST():
    with open('inventory.txt','r')as read_file:
        lines = read_file.readlines()
        count = 1
        for line in lines:
            value = line.split(',')
            if len(value) > 1:
                if int(value[5]) < int(value[6]):
                    print("-"*50)
                    print(f"\t ({count}) View Replenish Items!")
                    print("-"*50)
                    print("Description \t: ",value[1])
                    print("Quantity \t: ",value[5])
                    print("Minimum \t: ",value[6])
                    count += 1

# STOCK REPLENISHMENT
def STOCK_REPLENISHMENT():
    with open('inventory.txt','r')as read_file:
        with open('inventory_copy.txt','w')as write_file:
            Co = int(input("Enter the Code of item: "))
            flag = 0
            lines = read_file.readlines()
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if int(value[0]) == Co:
                        print("-"*50)
                        print("\t\tItem Found It !")
                        print("-"*50)
                        print("Description \t: ",value[1])
                        print("Quantity \t: ",value[5])
                        print("-"*50)
                        ans = input("Add the New Quantity to Item? [Yes/No]: ").lower()
                        if ans == "yes":
                            flag = 1
                            print("Quantity \t: "+str(value[5])+" + ___")
                            quan = int(input("Enter the Quantity to add: "))
                            value[5] = int(value[5]) + quan
                            sentence = value[0]+','+value[1]+','+value[2]+','+value[3]+','+str(value[4])+','+str(value[5])+','+str(value[6])
                            write_file.write(sentence)
                            write_file.write('\n')
                        else:
                            flag = 2
                            write_file.write(line)
                    else:
                        write_file.write(line)
            if flag == 0:
                print("-"*50)
                print("\t\tItem Not Exist !")
                print("-"*50)
            elif flag == 1:
                print("-"*50)
                print("\t\t Quantity Add Successfully !")
                print("-"*50)
            elif flag == 2:
                print("-"*50)
                print("\t\t You Cancel to add new Quantity !")
                print("-"*50)
    os.remove('inventory.txt')
    os.rename('inventory_copy.txt','inventory.txt')

# SEARCH ITEMS
def SEARCH_ITEMS():
    with open('inventory.txt','r')as read_file:
        lines = read_file.readlines()
        print("(A) Search Item (Description)\n(B) Search Item (Code Range)\n(C) Search Item (Category)\n(D) Search Item(Price Range)")
        method = input(">>> ").upper()
        if method == "A":
            print("-"*50)
            print(" DESCRIPTION SEARCHING METHOD")
            print("-"*50)
            D = input("Enter the Description of Item: ").upper()
            flag = 0
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if value[1] == D:
                        flag = 1
                        print("-"*50)
                        print(" Item Found it !")
                        print("-"*50)
                        print("Code \t\t: ",value[0])
                        print("Description \t: ",value[1])
                        print("Category \t: ",value[2])
                        print("Unit \t\t: ",value[3])
                        print("Price \t\t: ",value[4])
                        print("Quantity \t: ",value[5])
                        print("Minimum \t: ",value[6])
                        print("-"*50)
            if flag == 0:
                print("-"*50)
                print(" Items not Exist !")
                print("-"*50)
        elif method == "B":
            print("-"*50)
            print(" CODE SEARCHING METHOD")
            print("-"*50)
            Co1 = int(input("Enter the Head of Code Range: "))
            Co2 = int(input("Enter the Last of Code Range: "))
            flag = 0
            count = 1
            for line in lines:
                value = line.split(",")
                if len(value) > 1:
                    if int(value[0]) >= Co1 and int(value[0]) <= Co2:
                        flag = 1
                        print("-"*50)
                        print(f" ({count}) Item Found it !")
                        print("-"*50)
                        print("Code \t\t: ",value[0])
                        print("Description \t: ",value[1])
                        print("Category \t: ",value[2])
                        print("Unit \t\t: ",value[3])
                        print("Price \t\t: ",value[4])
                        print("Quantity \t: ",value[5])
                        print("Minimum \t: ",value[6])
                        print("-"*50)
                        count += 1
            if flag == 0:
                print("-"*50)
                print(" Items not Exist !")
                print("-"*50)
        elif method == "C":
            print("-"*50)
            print(" CATEGORY SEARCHING METHOD")
            print("-"*50)
            C = input("Enter the Category of Items: ").upper()
            flag = 0
            count = 1
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if value[2] == C:
                        flag = 1
                        print("-"*50)
                        print(f" ({count}) Item Found it !")
                        print("-"*50)
                        print("Code \t\t: ",value[0])
                        print("Description \t: ",value[1])
                        print("Category \t: ",value[2])
                        print("Unit \t\t: ",value[3])
                        print("Price \t\t: ",value[4])
                        print("Quantity \t: ",value[5])
                        print("Minimum \t: ",value[6])
                        print("-"*50)
                        count += 1
            if flag == 0:
                print("-"*50)
                print(" Items not Exist !")
                print("-"*50)
        elif method == "D":
            print("-"*50)
            print(" PRICE SEARCHING METHOD")
            print("-"*50)
            P1 = float(input("Enter the First Range of Price: "))
            P2 = float(input("Enter the Last Range of Price: "))
            flag = 0
            count = 1
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if float(value[4]) >= P1 and float(value[4]) <= P2:
                        flag = 1
                        print("-"*50)
                        print(f" ({count}) Item Found it !")
                        print("-"*50)
                        print("Code \t\t: ",value[0])
                        print("Description \t: ",value[1])
                        print("Category \t: ",value[2])
                        print("Unit \t\t: ",value[3])
                        print("Price \t\t: ",value[4])
                        print("Quantity \t: ",value[5])
                        print("Minimum \t: ",value[6])
                        print("-"*50)
                        count += 1
            if flag == 0:
                print("-"*50)
                print(" Items not Exist !")
                print("-"*50)
        else:
            print("Invalid Value")

# COMMAND REPEAT
def COMMAND_REPEAT(function):
    while (True):
        function()
        print("Do you want Continue this command?[Y/N]")
        re = input(">>> ").upper()
        if re == "Y":
            pass
        elif re == "N":
            print("You stop this command !")
            break
        else:
            print("Invalid Value")
            break

# ADMIN ACCESS CONTROL
def ADMIN():
    while (True):
        print("- - - - - Welcome to Admin Access Control - - - - -")
        print("1. Insert New Items\n2. Update Items\n3. Delete Items\n4. Stock Taking\
            \n5. View Replenish List\n6. Stock Replenishment\n7. Search Items\n8. Exit")
        func  = int(input(">>> "))
        if func == 1:
            COMMAND_REPEAT(INSERT_NEW_ITEM)
        elif func == 2:
            COMMAND_REPEAT(UPDATE_ITEM)
        elif func == 3:
            COMMAND_REPEAT(DELETE_ITEM)
        elif func == 4:
            COMMAND_REPEAT(STOCK_TAKING)
        elif func == 5:
            COMMAND_REPEAT(VIEW_REPLENISH_LIST)
        elif func == 6:
            COMMAND_REPEAT(STOCK_REPLENISHMENT)
        elif func == 7:
            COMMAND_REPEAT(SEARCH_ITEMS)
        elif func == 8:
            print("Thank for coming :D")
            break
        else:
            print("Invalid Value")
            print("Please Enter the correct command !")

# INVENTORY-CHECKER
def INVENTORY():
    while (True):
        print("- - - - - Welcome to INVENTORY-CHECKER Access Control - - - - -")
        print("1. Stock Taking\n2. Search Items\n3. Exit")
        func  = int(input(">>> "))
        if func == 1:
            COMMAND_REPEAT(STOCK_TAKING)
        elif func == 2:
            COMMAND_REPEAT(SEARCH_ITEMS)
        elif func == 3:
            print("Thank for coming :D")
            break
        else:
            print("Invalid Value")
            print("Please Enter the correct command !")

# PURCHASER
def PURCHASER():
    while (True):
        print("- - - - - Welcome to Purchaser Access Control - - - - -")
        print("1. View Replenish List\n2. Stock Replenishment\n3. Search Items\n4. Exit")
        func  = int(input(">>> "))
        if func == 1:
            COMMAND_REPEAT(VIEW_REPLENISH_LIST)
        elif func == 2:
            COMMAND_REPEAT(STOCK_REPLENISHMENT)
        elif func == 3:
            COMMAND_REPEAT(SEARCH_ITEMS)
        elif func == 4:
            print("Thank for coming :D")
            break
        else:
            print("Invalid Value")
            print("Please Enter the correct command !")

# CREATE NEW ACCOUNT
def CREATE_ACCOUNT():
    with open("user.txt",'a')as write_file:
        with open("user.txt",'r')as read_file:
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            print("(1) Admin\n(2) Inventory\n(3) Purchaser")
            role = int(input(">>> "))
            if role == 1:
                role = "ADMIN"
            elif role == 2:
                role = "INVENTORY"
            elif role == 3:
                role = "PURCHASER"
            else:
                print("Invalid Value")
            flag = 0
            lines = read_file.readlines()
            for line in lines:
                value = line.split(',')
                if len(value) > 1:
                    if username == value[0]:
                        flag = 1
            if flag == 1:
                print("-"*50)
                print("Unfortunately, Your Username is Existed !")
                print("-"*50)
            else:
                sentence = username + ',' + password + ',' + role
                write_file.write(sentence)
                write_file.write('\n')
                print("-"*50)
                print("Created New Account Successfully !")
                print("-"*50)

# LOGIN AUTHENTCATION
def LOGIN():
    with open("user.txt","r")as read_file:
        username = input("Username: ")
        password = input("Password: ")
        flag = 0
        lines = read_file.readlines()
        for line in lines:
            value = line.split(',')
            if len(value) > 1:
                if username == value[0] and password == value[1]:
                    if value[2] == "ADMIN\n":
                        flag = 1
                        ADMIN()
                    elif value[2] == "INVENTORY\n":
                        flag = 1
                        INVENTORY()
                    elif value[2] == "PURCHASER\n":
                        flag = 1
                        PURCHASER()
        if flag == 0:
            print("-"*50)
            print("Sorry, Your Username or Password is not correct !")
            print("-"*50)

