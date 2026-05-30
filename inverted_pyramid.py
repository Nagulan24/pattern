num =int(input("enter number:"))
for i in range(num):
    for k in range(i):
        print(" ",end="")
    for j in range((2*num-1)-2*i):
        print("*",end="")
   
    print()