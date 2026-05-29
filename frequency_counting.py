val = "nagulan"
checked ={}
for i in val:
    if i in checked:
        checked[i]+= 1
    else:
        checked[i]= 1
print(checked)