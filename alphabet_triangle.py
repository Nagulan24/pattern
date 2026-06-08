num = int(input("enter number: "))
val = "A"
for i in range(num):
    for j in range(i+1):
        print(chr(ord(val)+j),end=" ")
    print()

# chr used to ascii value to character
# ord used to character to ascii value