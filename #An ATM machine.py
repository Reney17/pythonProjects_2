#An ATM machine

print('Welcome to python bank ATM')
restart = 'y'
chances = 3
balance = 999.12

while chances >= 0:
    pin = int(input('Please enter your 4 Digit Pin: '))

    if pin == (1234):

        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For your Balance')
            print('Please Press 2 To Make a Withdraw')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Whould you like to choose?: '))

            if option == 1:
                print('Your Balance is R', balance)
                restart = input('Would you like to go back?')

                if restart in ('n', 'NO', 'no', 'N'):
                    break
            elif option == 2:
                #option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? 10,20,50,100,200 for other enter 1: '))
                if  withdrawl in [10, 20, 50, 100, 200]:
                        balance = balance - withdrawl
                        print('\nYour Balance is now R', balance)
                        restart = input('Would you like to go back?')
                        if restart in ('n', 'NO', 'no', 'N'):
                            break

                elif withdrawl != [10, 20, 50, 100, 200]:
                    print('Invalid Amount,Please Re-try\n')

                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please ENter Desired amount:'))

            elif option == 3:
                pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + pay_in
                print('\nYour Balance is now R', balance)
                restart = input('Would you like to go back')
                if restart in ('n', 'NO', 'no', 'N'):
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break


