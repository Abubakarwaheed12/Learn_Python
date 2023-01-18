# pass function as a argument 
from hashlib import new


l=[1,2,3,4,5]
def square(a):
    return a**2
print(list(map(square, l)))
# create own function  that is same to the map function 

def my_map(func, i):
    new_list=[]
    for j in i:
        new_list.append(func(j))
    return new_list

li=[1,2,3,4,5]
print(list(my_map(square, li)))
# we can use also a lamda function 

# with  list comprehension 
def my_map(func, i):
    return [func(item) for item in i]

li=[1,2,3,4,5]
print(list(my_map(square, li)))