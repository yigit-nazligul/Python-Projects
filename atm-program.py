print("Welcome to ATM. Please choose a process.")
print("1. View Balance\n2. Withdraw Cash\n3. Deposit Cash")

while True:
    balance=1000 
    p = str(input("Choose a process (type Q for exit:)"))
    if p=="q"or p=="Q":
        ("Exiting...")
        break
    elif p=="1":
        print("Your Balance:",balance)
    elif p=="2":
        wd = int(input("How many USD will you withdraw ?"))

        if wd>balance:
            print ("Low balance ! Your balance:",balance)
            break

        if balance>=wd:
            balance=balance-wd
            print("Withdrawing USD. Please Wait... \n Succesful !\Remaining Balance:",balance)
            break

    elif p=="3":
        dep=int(input("How many USD will you deposit ?"))
        balance = balance+dep
        print ("Succesful ! Your new balance:",balance)
        break
    else:
        print ("Invalid process... Please try again")
        break