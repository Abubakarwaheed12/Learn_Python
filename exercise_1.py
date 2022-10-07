# power program 
def mul(num , *args):
    if args:
        return [i**num for i in args]
    else:
        return( " you did not pass any value")
l=[1,23,4,5]
print(mul(2,*l))