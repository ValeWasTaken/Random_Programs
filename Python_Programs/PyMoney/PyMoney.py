# PyMoney Version 1.0
# Made in Python 3.4
# Requires: pyMoneyLogs.txt to share same directory as PyMoney.py

# Note: As this is only version 1.0 it is in a VERY crude form.
#       Updates are to be expected and code will be optimized later.
#       This is simply a minimum viable product.

def menu():
    # Intro to program / initial selection
    print("Please select an option: ")
    print("1. ) Register a new balance.")
    print("2. ) Check and/or modify an existing balance.")
    print("3. ) Exit program.")
    selection = input("Your selection: ")
    print('')

    if selection == '1':
        newBalance()
    elif selection == '2':
        loadBalance(int(input("Please enter your account #: ")))
    elif selection == '3':
        exit()

def check():
    # Used to check if data was entered correctly.
    check = input()
    if check[:1].lower() == 'y':
            print("Very well! Process saved.")
            return True
    elif check[:1].lower() == 'n':
            return False
    else:
        print("Invalid input. Please try again.\n")
        check()

def addNewEntry(name,amount,currency):
    # Used in newBalance() to help create a new account entry in the pyMoneyLogs.txt file.
    numOfAccounts = sum(1 for line in open('pyMoneyLogs.txt'))
    accountNumber = str(numOfAccounts+1)
    data = '{0}|{1}|{2}|{3}\n'.format(accountNumber,name,amount,currency)
    print("Thank you! Your account # is: {0}\n".format(accountNumber))
    with open('pyMoneyLogs.txt', 'a') as file:
        file.write(data)
        file.close()
    menu()

def newBalance():
    # Creates a new account entry.
    partyName = input("Please enter the name of the other party: ")
    amount = input('Please enter the amount owed.\n'+
                          'Example: "+400" means you owe them 400 and "-100" means they owe you 100.\n\n')
    currency = input("Please enter currency type (gold, dollars, ISK, etc.): ")
    print('')

    if amount[:1] == '+':
        print("You entered that you owe {0} {1} {2} is that correct?".format(partyName, amount[1:], currency))
        if check() == True:
            addNewEntry(partyName,amount,currency)
        else:
            print("Sorry to hear that. Restarting process.\n")
            newBalance()
            
    elif amount[:1] == '-':
        print("You entered that {0} owes you {1} {2} is that correct?".format(partyName, amount[1:], currency))
        if check() == True:
            addNewEntry(partyName,amount,currency)
        else:
            print("Sorry to hear that. Restarting process.\n")
            newBalance()
    else:
        print("Invalid input. Restarting. Remember to begin with a '+' or '-'!\n")
        newBalance()

def modify(amount):
    # Modifies an account's balance.
    modifyChoice = input("Would you like to modify the amount saved?: ")
    
    if modifyChoice[:1].lower() == 'y' and amount[0:1] == '+':
        print('-'*60+"\nREMINDER:\n"+'"+number" means you owe number to that person more.\n'+'"-number" means they owe that number more!\n'+'-'*60+'\n')
        modifyAmount = input("Input change (Ex: +200): ")
        if modifyAmount [0:1] == '+':
            newAmount = int(amount[1:]) + int(modifyAmount)
        else:
            newAmount = int(amount) + int(modifyAmount)
    elif modifyChoice[:1].lower() == 'y' and amount[0:1] == '-':
        print('-'*60+"\nREMINDER:\n"+'"+number" means you owe number to that person.\n'+'"-number" means they owe that number!\n'+'-'*60+'\n')
        modifyAmount = input("Input change (Ex: +200): ")
        if modifyAmount [0:1] == '+':
            newAmount = int(amount[1:]) + int(modifyAmount)
        else:
            newAmount = int(amount) + int(modifyAmount)
    elif modifyChoice[:1].lower() == 'n':
        print("\n\nOkay, have a nice day!")
        exit()
    else:
        print("Invalid input. Please try again.")
        modify(amount)
    if str(newAmount)[0:1] != '+' and str(newAmount)[0:1] != '-':
        newAmount = '+{0}'.format(newAmount)

    print("Is that all?: ")
    if check() == True:
        print("Thank you and have a nice day!")
    else:
        finalChoice = input("Would you prefer to return to the main menu or further modify your amount?\n"+
              "Option 1. ) Modify amount further\n"+
              "Option 2. ) Return to Main Menu\n"+
              "Your selection: ")
        if finalChoice == '1':
            try:
                modify(newAmount)
            except UnboundLocalError:
                modify(amount)
        elif finalChoice == '2':
            menu()
        else:
            print("Invalid input. Starting new modify process.")
            try:
                modify(newAmount)
            except UnboundLocalError:
                modify(amount)
    print("New balance: {0}".format(newAmount))
    return(str(newAmount))

def loadBalance(accountNumber):
    # Loads (and potentially modifies) an account's balance.
    with open('pyMoneyLogs.txt', 'r+') as file:
        data = file.readlines()
        accountInfo = data[accountNumber-1][:-1].split('|') #[:-1] is to remove the '\n' character
        accNum,partyName,amount,currency = accountInfo[0],accountInfo[1],accountInfo[2],accountInfo[3]
        if amount[:1] == '+':
            print("You owe {0} {1} {2}".format(partyName,amount[1:],currency))
        elif amount[:1] == '-':
            print("{0} owes you {1} {2}".format(partyName,amount[1:],currency))
        amount = modify(amount)
        data[accountNumber-1] = ('{0}|{1}|{2}|{3}\n'.format(accNum,partyName,amount,currency))
        file.close()
    file = open('pyMoneyLogs.txt','w')
    file.writelines(data)
    file.close()
    print("\n\nThank you for using PyMoney! Have a nice day!")
    exit()

def main():
    print("Welcome to PyMoney v0.8!")
    menu()

main()
