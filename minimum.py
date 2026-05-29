values=(10,12,53,-12,-45,110)
smallest=values[0]
for i in values:
    if smallest >= i:
        smallest =i
print(f"minimum number is : {smallest}")
