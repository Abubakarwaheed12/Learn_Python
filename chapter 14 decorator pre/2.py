#  function returning function  

def func(a):
    def func1():
        print (f"hello {a}")
    return func1()

# print(func("abu bakar"))

#  example another 
def outer():
    def inner():
        print("you are now inside the inner function")
    return inner

var=outer()
var()