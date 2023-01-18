# make flexible functions 
# * operator

def total(a,b):
    return a+b

print(total(4,6))

#  with * operator we can pass multiple 
def ab(*args):
    # return args
    total_num=0
    for i in args:
        total_num +=i
    return total_num
print(ab(1,2,2,3))