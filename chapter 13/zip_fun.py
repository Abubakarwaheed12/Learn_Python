# zip function
from tkinter import N


user=['user1','user2','user3']
names=['abu bakar' , 'waheed' , 'moin']

# for combining numbers 
# it returns tuple but we can convert it into list
# we can zip more than two list in dictionary
print(dict(zip(user, names)))

a=[('a',1), ('b',2)]
print(dict(a))

# l1=[1,3,5,7,9]
# l2=[2,4,6,8]
l=[(1, 2), (3, 4), (5, 6), (7, 8)]
l1,l2=list(zip(*l))
# it make two tuples 
print(l1,l2)

l3=[1,3,5,7,9]
l4=[2,4,6,8,8]
n_list=[]
for pair in zip(l3,l4):
    n_list.append(max(pair))

print(n_list)
# same in program with list for


