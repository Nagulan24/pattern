num = int(input("enter number: "))
for i in range(num):
    #upper
    # left stars 
    for j in range(i+1):
        print("*",end="")
    #spaces
    for k in range((num*2)-2-(2*i)):
        print(" ",end="")
    #right stars
    for l in range(i+1):
        print("*",end="")
    print()
for a in range(1,num):
    for x in range(num-a):
        print('*',end ="")
    for y in range(2*a):
        print(" ",end="")
    for z in range(num-a):
        print("*",end="")
    print()
