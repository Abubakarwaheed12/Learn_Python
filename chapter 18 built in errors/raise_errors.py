def add(a,b):
    if(type(a) is int ) and (type(b) is int):
        return a+b
    # here  we raise a error 
    raise TypeError("OOPS you are passing wrong data")

print(add(2,'3'))