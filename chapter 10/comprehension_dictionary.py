

# square={1:1,2:2.....9:}  example 

square={f"square of {num} is ":num**2 for num in range(1,11)}
for i , j in square.items():
    print(i ,j)
print(square)



#  for character counting
string="abu bakar"

n={i:string.count(i) for i in string}

print(n)