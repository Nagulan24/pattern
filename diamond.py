num = int(input("enter number: "))
for i in range(num):
    #spaces
    for j in range(num-i-1):
        print(" ",end="")
    #star
    for k in range(2*i+1):
        print("*",end="")
    print()
for c in range(1,num):
    #space 2
    for a in range(c):
        print(" ",end="")
    #stars2
    for b in range((2*num)-(2*c+1)):
        print("*", end="")
    print()    