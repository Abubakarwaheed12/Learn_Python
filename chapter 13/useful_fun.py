# what are doc strings
# how to write doc strings
# how to see docstrings
# what is help function 

#  we use triple single quotes ''' ''' or double quotes """""""" for doc string

def add(a,b):
    '''this function takes two input and return the sum'''
    return a+b

print(add.__doc__)
# we cansee the docstring of inbuilt functions 
print(sum.__doc__)