#  decorators part 2
#  solve some problems in this program  




def decorator_function(any_function):
    def wrapper_function(*args , **kwargs ):
        print("this is awesome function")
        return any_function(*args , **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f"this is function with argument {a}")
func(3)

@decorator_function
def func1(a,b):
    return a+b
var=func1(4,5)
print(var)



