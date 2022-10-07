#  args as args 

def mul(*args):
    ml=1
    for i in args:
        ml *=i
    return ml

# argument k baad hum koi parameter pass nai kar sakty 

# we can use this method with list and tuple
l=[1,2,3,4]
print(mul(*l))