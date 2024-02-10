attempts = 3
userPin = 1234
userPreference = 0
totalMoney = 0

print(
'''
************************************************************
* Welcome to Adeu's ATM Online Banking Software.           *
*                                                          *
* Please select a number                                   *
************************************************************
''')

print(
'''1: Access the System
2: Exit''')
userPreference = int(input())

if userPreference == 2:
    SystemExit

if userPreference == 1:
    while attempts != 0:
        attemptPin = int(input("Please Enter Your 4 Digit Pin Number: "))
        if attemptPin != userPin:
            attempts -= 1
            print('Wrong Pin Number, you have ' + str(attempts) + ' attempts left')
            print('Try Again')
        else:
            print('You have successfully accessed Adeu\'s ATM system')
            print('''

Please Select an Option                  

D) Deposit        
W) Withdraw
T) Check Total Balance
X) Change Pin Number
E) Exit
''')
            userChoice = input()
            if userChoice == "D" or userChoice == "d":
                userDeposit = input('Enter the Total Amount You Would like to Deposit: ')
                totalMoney += userDeposit
                print('$', userDeposit, ' have been added to your account')
            elif userChoice == "W" or userChoice == "w":
                userWithdrawn = input('Enter the Total Amount You Would like to Withdraw: ')
                totalMoney -= userWithdrawn
                print('$', userDeposit, ' have been withdrawn from your account')
            elif userChoice == "T" or userChoice == "t":
                print("You have a total amount of $" + str(totalMoney) + " in your bank account")
            elif userChoice == "X" or userChoice == "x":
                newPin = input('Please enter your new Pin Number: ')
                confirmedPin = input('Please confirm your Pin Number: ')
                userPin = newPin
                if userPin == newPin:
                    print('Your Pin has been successfully updated')
            elif userChoice == "E" or userChoice == "e":
                SystemExit
            UserHasFinished = input('Would You Like to Continue? Y/N: ')
            if UserHasFinished == 'Y':
                continue
            elif UserHasFinished == 'N':
                print("Thank you for your time!")
                print('Have a Nice Day')
                break