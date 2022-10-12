# clousers 
# practice 
# function returning fuction 

def to_power(num):
    def  to_num(n):
        return n**num
    return to_num
cube=to_power(3)
print(cube(2))