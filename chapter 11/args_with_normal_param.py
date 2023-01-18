
#  multipy program 
# this function ois with normal parameters 
def mul(num,*args):
    ml=1
    for i in args:
        ml *=i
    return ml

# argument k baad hum koi parameter pass nai kar sakty 


print(mul(1,2,3))