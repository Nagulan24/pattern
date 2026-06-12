num = int(input("enter number:"))
for i in range(2*num-1):
    for j in range(2*num-1):
        layer = min(i,j,(2*num-2)-i,((2*num-2))-j)
        val=num-layer
        print(val,end="")
    print()
