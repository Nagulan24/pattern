#using with range

value=[[1,2,3],[4,5,6]]
for i in range(len(value)):
    for j in range(len(value[i])):
        print(value[i][j])

#using direct values
print("")
for i in value:
    for j in i:
        print(j)