# another problem solve in this program 

from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args , **kwargs ):
        ''' THIS IS WRAPPER FUNCTION FOR A DECORATOR FUNCTION'''
        print("this is awesome function")
        return any_function(*args , **kwargs)
    return wrapper_function


@decorator_function
def func1(a,b):
    '''this func 1 '''
    print("hello world")
    return a+b

# var = (func1.__doc__)
print(func1(2,2))
