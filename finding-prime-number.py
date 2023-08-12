#Finding prime number program.

def is_number_prime(num):
    if (num == 1):
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num % i ==0):
                return False
            
        
while True:
    num = (input ("Type a number:"))            

    if num == "q" or num == "Q":
        break

    else:
        num = int (num)

        if (is_number_prime(num)):
            print (num, "is a Prime number.")
        else:
            print (num,"is not a Prime number.")

            