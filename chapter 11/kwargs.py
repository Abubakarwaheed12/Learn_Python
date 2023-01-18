# kwargs keyword  arguments 
# ** operator 

def name(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i ,j in kwargs.items():
        print(f"key is {i}  : and value is {j}")

d={'name':"abu bakar waheed", 'age':'19'}
# we can pass the dictionary 
print(name(**d))
print(name(name="abu bakar waheed", age='19'))
#  it will return a dictionary

