#Making Multiplication Table Project

print ("Welcome to Program... We'll make a multiplication table")

for fst in range (1,11):
    print ("**************************")
    for sec in range(1,11):
        print("{} x {} = {}".format (fst,sec,fst*sec))