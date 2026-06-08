num = int(input("enter number: "))
for i in range(num):
    for j in range (i+1):
        print((i+j+1) % 2, end ="")
    print()