#This program is printing only numbers divisible by 3 in the range of 1-?      ?:Your chose value

max = int(input ("Please choose a range (1- ?):"))

for val in range (1,max+1):
    if val % 3 != 0 :
        continue
    print (val)
    