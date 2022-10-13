# INHERITENCE 
# IT IS VERY  IMPORTANT TOPIC OF OOP

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
        
p2=phone('infinx' ,112,2000,)
p1=smartphone('nokia' ,112,2000, '4gb','45gb')
print(p1.full_name())
print(p2.full_name() + "\n" +  f"{p2.price}" )
# print(p1.make_a_call(2301241))