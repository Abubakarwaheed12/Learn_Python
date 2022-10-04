number=input("enter more than one numbers")

total=0
i=0
while i<len(number):
    total+=int(number[i])
    i+=1

print(total)