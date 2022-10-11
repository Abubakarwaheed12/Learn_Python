
from email import iterators
import numbers


number=[1,2,3,4,5,6,7,8,9]  # iterable 
squares=map(lambda a:a%2==0 , number) # iterator it reutrn map object
# print(squares)

# for i in squares:
#     print(i)

# steps for iter 
# 1: iter(function)
# 2: next(function)
# example 
number_iter=iter(number) # working of foor loop 
print(next(number_iter)) # working of foor loop 
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))


print(iter(number))

# in map and filter function we can call directly next function because it is iterators

print(next(squares))
print(next(squares))