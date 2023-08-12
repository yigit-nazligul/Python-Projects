#Finding Perfect Number Program...
print("Welcome to Program...")
i = 1
eq = 0
number=int(input("Please type a number:"))
while (eq<number):
    if(number % i == 0):
        eq += i
    i+=1
if eq == number:
    print ("{} is a Perfect Number".format (number))
else:
    print ("{} is not a Perfect Number".format(number))