#  decorator with arguments
from functools import wraps

def only_data_data_type(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args, **kwargs)
            else:
                print ("invalid input")
        return wrapper
    return decorator

@only_data_data_type(int)
def string(*args):
    stri=''
    for i in args:
        stri +=i
    return stri
print(string("hello" , "abubakar"))

# program completed  successfully*