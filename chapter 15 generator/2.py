# create firs generator with generator function 
# generator function
# generator comprehension

# 0 to 10 

import numbers


def nums(n):
    for i in range(0 , n+1):
        yield (i)
# generator returns a iterator 
number = nums(20)
for num in number:
    print(num)

# we can convert generator into list but we cannot use benefits of 
# print(number)
#  we cannot print one than more time to a generator 
# print(list(i for i in number))