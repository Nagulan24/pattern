num = int(input("enter number:"))
for i in range(num):
    for j in range(num-i):
        print("*",end="")
    print()