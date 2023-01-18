# pracrtice of decorator functions 
# function that return the sum for all and decorator check that all values is int or not 

from functools import total_ordering, wraps

# decorator function 
def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # n_list=[] 
        # for arg in args:
        #     n_list.append((type(arg)==int))
        # if all(n_list):
        #     return function(*args , **kwargs)
        # else:
        #     print("invalid")
            # short code for this
        if all([type(arg)==int for arg in args]):
            return function(*args , **kwargs)
        else:
            return ("invalid input you can pass only integers")
    return wrapper

        
        
@decorator
def all_sum(*args):
    total=0
    for i in args:
        total +=i
    return total

print(all_sum(1,2,3,4,5,6))