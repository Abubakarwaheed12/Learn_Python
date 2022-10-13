# MULTILEVEL INHERITENCE 
# MRO 
# OVERRIDIDING
# CAN WE DRIVE MORE THAN ONE CLASS FROM BASE CLASS ? ANS : YES WE CAN 
# METHOD RESOLUTION ORDER 
# METHOD OVERRIDING 
# ISIINSTANCE() ISSUBCLASS()

from __future__ import barry_as_FLUFL


class phone: # BASE CLASS / PARENT CLASS
    def __init__(self , brand , model_name , price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price , 0)

    def full_name(self):
        return f"full name is {self.brand}   {self.model_name}"
        
    def make_a_call(self, phone):
        return f"calling {phone} ......"

class smartphone(phone): # INHERIT CLASS
    def __init__(self , brand , model_name , price ,ram , memory,):
        #phone.__init__(self ,brand , model_name , price)# thic is UNCOMMON WAY
        super().__init__( brand , model_name , price) # COMMON WAY
        self.ram=ram
        self.memory=memory

# MULTILEVEL INHERITENCE 
# THIS IS CALLED MULTILEVEL INHERITENCE 
class flagship_phone(smartphone):
    def __init__(self, brand, model_name, price, ram, memory,fron_camera):
        super().__init__(brand, model_name, price, ram, memory)
        self.front_camera=fron_camera
    #THIS IS METHOD OVERRIDING  
    def full_name(self):
        return f"brand name is   {self.brand}  model name is {self.model_name} and price is {self.price}"
# making an object of flagshpi  class 
flagship=flagship_phone('iphone',233,444444,3,56,"front camera is availabe")
print(flagship.full_name())
#METHOD RESOLUTION ORDER  we can check method resolution order with the help of help function
# print(help(flagship))
# # ANOTHER CLASS THAT INHERITS THE BASE CLASS OF PHONE 

# class smartphone2(phone): # INHERIT CLASS
#     def __init__(self , brand , model_name , price ,ram , memory,):
#         #phone.__init__(self ,brand , model_name , price)# thic is UNCOMMON WAY
#         super().__init__( brand , model_name , price) # COMMON WAY
#         self.ram=ram
#         self.memory=memory

# # creating objects of smart[phone 2 class
# smartphone2=smartphone2("vivo",23223 ,212121,'2gb' , '3gb')
# print(smartphone2.full_name())

#  
p2=phone('infinx' ,112,2000,)
p1=smartphone('nokia' ,112,2000, '4gb','45gb')
# print(p1.full_name())
# print(p2.full_name() + "\n" +  f"{p2.price}" )
# print(p1.make_a_call(2301241))

#ISINSTANCE  
# ye check karny k liye ye obn=ject is class ka  ha ya nai 
print(isinstance(p1 , smartphone))

# ISSUBCLASS
# ye check karny k liye k ye subclass  ha ya nai 
print(issubclass(smartphone , phone))