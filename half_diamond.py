num=int(input("enter number: "))
for i in range(num):
    #upper 
    for j in range(i+1):
        print("*", end ="")
    print()

for b in range(1,num):
    #lower 
    for k in range(num-b):
        print("*",end ="")
    print()