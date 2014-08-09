from math import*

F1 = " Area of an ellipse."
F2 = " Area of a triangle."
F3 = " Area of an equilateral triangle."
F4 = " Volume of a cone."
F5 = " Volume of a sphere."

def elsePhrase():
    print("Wrong input, I'll just send you back to the menu.\n")
    menu()

def menu():
    print("- - - - - - - -- PROGRAM  MENU -- - - - - - - -")
    print("Please choose a desired formula to solve with: \n")
    print("1 )" + str(F1)) # Prints from previously defined list
    print("2 )" + str(F2))
    print("3 )" + str(F3))
    print("4 )" + str(F4))
    print("5 )" + str(F5))
    menu_Choice = raw_input("6 ) Exit.\n\n")

    if menu_Choice == 1:
        A_Ellipse()
    elif menu_Choice == 2:
        A_Triangle()
    elif menu_Choice == 3:
        A_EQ_Triangle()
    elif menu_Choice == 4:
        V_Cone()
    elif menu_Choice == 5:
        V_Sphere()
    elif menu_Choice == 6:
        exit()
    while menu_Choice not in [str(i) for i in range(1,7)]: #Executes if input = any number not listed.
        print("Invalid input. Please try again.\n")
        menu()
    else:
        print("Error: Please enter a number as shown and try again.")
        print(('-' * 60) + "\n\n") #Prints 60 "-"s
        menu()

def Restart():
    toMenu = raw_input("\nWould you like to go back to the main menu? Y / N\n\n")
    if toMenu == "Y":
        menu()
    elif toMenu == "N":
        toExit = raw_input("Oh.. Okay then want me to just exit the program? Y /N\n\n")
        if toExit == "Y":
            exit()
        elif toExit == "N":
            print("Alright, I guess I'll just leave you be, you know where the big red X button is I guess. Take your time.")
        else:
            elsePhrase()
    else:
        elsePhrase()
    
def A_Ellipse():
    print("\nSolving for:" + str(F1))
    R1 = input("\nPlease enter first radius: ")
    R2 = input("Please enter second radius: ")
    AoE = pi * int(R1) * int(R2) # AoE stands for - Area of Ellipse
    print "Your answer is: " + str(AoE)
    Restart()
    
def A_Triangle():
    print("\nSolving for:" + str(F2))
    Tbase = input("Please enter the base of the triangle: ")
    Theight = input("Please enter the height of the triangle: ")
    AoT = 0.5 * int(Tbase) * int(Theight) # AoT stands for - Area of Triangle
    print "Your answer is: " + str(AoT)
    Restart()
    
def A_EQ_Triangle():
    print("\nSolving for:" + str(F3))
    SideLength = input("Please enter the side length of the equilateral triangle: ")
    AoEQT = sqrt(3) / 4 * pow(SideLength,2) # AoEQT stands for - Area of Equilateral Triangle
    print "\nYour answer is " + str(AoEQT)
    Restart()
    
def V_Cone():
    print("\nSolving for:" + str(F4))
    C_height = input("Please enter the height of the cone: ")
    C_Radius = input("Please enter the radius of the cone: ")
    VoC = pow(C_Radius,2) * pi * int(C_height) * 1 / 3 # VoC stands for - Volume of Cone
    print "\nYour answer is " + str(VoC)
    Restart()
    
def V_Sphere():
    print("\nSolving for:" + str(F5))
    S_Radius = input("Please enter the radius of the sphere: ")
    VoS = pi * pow(S_Radius,3) * 4 / 3 # VoS stands for - Volume of Sphere
    print "\nYour answer is " + str(VoS)
    Restart()
    
menu()
