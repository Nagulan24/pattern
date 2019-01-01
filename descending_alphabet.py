num = int(input("enter"))
val='E'
for i in range(num):
    for j in range(i+1):
        print(chr(ord(val)-j),end="")
    print()