num=int(input("enter number :"))
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for k in range(i+i+1):
        print("*",end="")
    print()
