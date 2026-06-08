num = int(input("enter number: "))
a=0
for i in range(num):
    for j in range (i+1):
        print(a+1,end =" ")
        a+=1
    print()
