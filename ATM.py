attempts = 3
userPin = 1234
userPreference = 0

print(
'''
************************************************************
* Welcome to Adeu's ATM Online Banking Software.           *
*                                                          *
* Please select a number                                   *
************************************************************
''')

userPreference = int(input(
'''1: Access the System
2: Exit'''))

if userPreference == 2:
    SystemExit

if userPreference == 1:
    while attempts != 0:
        attemptPin = int(input("Please Enter Your 4 Digit Pin Number: "))
        if userPin != attemptPin:
            attempts -= 1
            print('Wrong Pin Number, you have ' + attempts + ' attempts left')
            print('Try Again')
        else:
            userChoice = input(
                '''
                D) Deposit        
                W) Withdraw
                ''')
            if userChoice == "D" or 'd':
                userDeposit = input('Enter the Total Amount You Would like to Deposit: ')
                print('$', userDeposit, ' have been added to your account')
            elif userChoice == 'W' or 'w':
                userDeposit = input('Enter the Total Amount You Would like to Withdraw: ')
                print('$', userDeposit, ' have been withdrawn from your account')
        UserHasFinished = input('Would You Like to Continue? Y/N: ')
        if UserHasFinished == 'Y':
            continue
        elif UserHasFinished == 'N':
            print("Thank you for your time")
            break