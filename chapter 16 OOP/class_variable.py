# CLASS VARIABLES 
# INSTANCE VARIBALE ARE DIFFERENT FOR EVERY OBJECT 
# BUT CLASS VARIABLE VALUE IS SHARED FOR  EVERY FUNCTION

# CIRLE 
# AREA
# CIRCUM

class circle:
    pi=3.14 #class variable 
    def __init__(self ,radius):
        self.radius=radius
    def circum(self):
        return 2*circle.pi*self.radius
    
ar=circle(5)
print(ar.circum())

# EX 1
# APPLY DISCOUNT FUNCTION 


class laptop:
    discount=10
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def apply_discount(self):
        r= (laptop.discount/100)*self.price
        print(f"discount price  is {r}")
# object 
lp1=laptop('hp' , "core i 5" , 40000)
print(lp1.brand_name , lp1.model_name, lp1.price)
print(lp1.apply_discount())




