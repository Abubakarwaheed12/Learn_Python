#  function return two values in tuple
def add(n1,n2):
    add=n1+n2
    mul=n1*n2
    return add ,mul

print(add(1,2))

# soution is that 
# we can store it in variables

add,mul=(add(1,2))
print(add)
print(mul)
