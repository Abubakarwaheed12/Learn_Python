# enumerate functions 
# we use enumerate function with for loop to track position of our itrm in iterable


# how we can do this without enumerate function 
names=['abu bakar' , 'hamna' , 'sara']
pos=0
for name in names:
    print(f"{pos} ------ {name}")
    pos +=1


# with enumeratefunction 
names=['abu bakar' , 'hamna' , 'sara']

for pos , name in enumerate(names):
    print(f"{pos} ------ {name}")


#  find position in list program 
def find_pos(l, target):
    for pos, name in enumerate(l):
        if name==target:
            return pos
    return -1

print(find_pos(names,"savfs"))