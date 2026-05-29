value=[10,20,30,40,50]
target= 30
found = False
for i in value:
    if i == target:
        found =True
        break
if found == True:
    print(f"target {target} is found")
else:
    print(f"target {target} is not found")