total= 0

while True:
    num=input("Type a number:")
    if num=="q" or num=="Q":
        break


    num=int(num)

    total+=num
print ("Total of numbers:",total)
    
