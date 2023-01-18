#  practice 
from functools import wraps

def dec(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"you are calling {function.__name__}")
        print(f" {function.__doc__}")
        return function(*args , **kwargs)
    return wrapper

@dec
def mul(a,b):
    '''hello you are in multiply function'''
    return a*b

print(mul(2,2))

# sum
@dec
def sam(a,b):
    '''hello you are in multiply function'''
    return a*b

print(sam(2,2))


