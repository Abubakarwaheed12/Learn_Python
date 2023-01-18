# filter function
# filter function is iterable
#  you can iterate only one time in map and filter function but when you make a list then yo can iterate more than one times 

# def even(a):
#     if a%2==0:
#         return True
#     else:
#         return False

# print(even(3))

# but we pass a list and filter all the even numbers 
a=[1,2,3,4,5,6,7,89,9]
# we can use here a lambda function
nlist=tuple(filter(lambda a:a%2==0 , a))
print(nlist)