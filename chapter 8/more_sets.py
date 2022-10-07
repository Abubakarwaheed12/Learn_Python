s={"A","B","C","D","E","F","G",}

if "A" in s:
    print('present')
else:
    print(' not present')

for items in s:
    print(items)

# set maths
# union 
# intersection
a={1,2,3,4}
b={2,3,1,3,4}

# pipe symbol is used for union 
# | union symbol
# & intersection sybmol
union_set=a|b
intersection_set=a&b
print(union_set)
print(intersection_set)