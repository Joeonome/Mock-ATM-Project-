name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love'] 
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

if(name in allowedUsers):
    password = input("What is your password? \n")
    userId = allowedUsers.index(name)
    
    if(password == allowedPassword[userId]):
        print('Welcome %s' %name)
        import datetime
        Current_Date = datetime.datetime.today()
        print ('Current Date: ' + str(Current_Date))
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Balance')
        print('4. Complaint')

        selectedOption = int(input('Please select an option: \n'))

        if(selectedOption == 1):
            print("You selected %s" %selectedOption)

            selectedAmount = int(input("Please enter your amount: \n"))

            if(selectedAmount >= 1000 and selectedAmount < 50000):
                print("withdrawal Successful!")
            
           
                endOfWithdrawal = int(input("Will you like to make another transaction? \n 1. Yes \n 2. No \n"))
                

                if(endOfWithdrawal == 1):
                    print("Restarting...")
                elif(endOfWithdrawal == 2):
                    print("Thank you for banking with us")
                else:
                    print("Invalid input, exiting...")
                    
            elif(selectedAmount < 1000):
                print("Please enter multiples of 1000")
            else:
                print("Insufficient funds, restarting...")

                
        

        elif(selectedOption == 2):
            print("You selected %s" %selectedOption)

            selectedDeposit = int(input("Select the amount you want to deposit and insert cash: \n"))

            if(selectedDeposit >= 1):
                print("Deposit Successful!")

                endOfWithdrawal = int(input("Will you like to make another transaction? \n 1. Yes \n 2. No \n"))
                

                if(endOfWithdrawal == 1):
                    print("Restarting...")
                elif(endOfWithdrawal == 2):
                    print("Thank you for banking with us")
                else:
                    print("Invalid input, exiting...")
                
            else:
                print("Invalid input, exiting...")
            

            

            
        elif(selectedOption == 3):
            print("You selected %s" %selectedOption)

            accountDetailsForBalance = input("Enter your account details: \n 1. Account Number \n 2. Bank \n")

            if( accountDetailsForBalance == "12"):
                print ("Account details unavailable, please contact your bank \nExiting... \n")
            else: print("Invalid input, exiting...")



        elif(selectedOption == 4):
            print("You selected %s" %selectedOption)

            complaintBox = int(input("Kindly choose: \n1. For card complaint \n2. for bank complaint \n"))
            if(complaintBox == 1):
                print('You will be attended to shortly...')
            elif(complaintBox == 2):
                print('You will be attended to shortly...')
            else:
                 print("Invalid input, exiting...")
            
                
                                     
            
            

            
        else: print('Invalid option, please try again')


    else: print("Password incorrect, please try again")
        
        


           




else: print("Name not found, please try again")

