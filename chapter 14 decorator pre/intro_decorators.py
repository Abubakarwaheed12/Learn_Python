#  decorators 
# first class functions/ clousers 

def square(a):
    return a**2

# assign a function in variable 
a=square #(2)
print(a)
# check the name of functions 
print(square.__name__)
print(a.__name__)