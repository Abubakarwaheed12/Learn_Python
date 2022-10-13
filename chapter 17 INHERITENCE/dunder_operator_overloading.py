# POLYMORPHISM  mean many forms of object
# OPERAOROR IVELOADING
# DUNDER METHOD __INIT__


class phone: # BASE CLASS / PARENT CLASS
    def __init__(self , brand , model_name , price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price , 0)

    def full_name(self):
        return f"full name is {self.brand}   {self.model_name}"
        
    def make_a_call(self, phone):
        return f"calling {phone} ......"
# str repr
# ye method khd hi call ho jaty han jab hum object ko print karwaty han 
    def __str__(self): # nicely formatted string
        return f"full name is {self.brand}   {self.model_name}"
    def __repr__(self): # for  onject representation for debuging for developers 
        return f"full name is {self.brand}   {self.model_name} {self.price}"
    # OPERATOR OVERLOADING
    def __add__(self, other ):
        return self.price+other.price
    # we can also use mul add min operators



p2=phone('infinx' ,112,2000,)
p3=phone('infinx' ,112,2000,)
# operator overloading
print(p2+p3)
# this is also the example of polymorphism 
print(p2)
print(repr(p2))
# print(p2.full_name() + "\n" +  f"{p2.price}" )
# print(p1.make_a_call(2301241))