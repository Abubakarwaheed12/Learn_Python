# APPLY DISCOUNT FUNCTION 

from tkinter.messagebox import RETRY


class laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def apply_discount(self , a):
        r= (a/100)*self.price
        print(f"discount price  is {r}")
# object 
lp1=laptop('hp' , "core i 5" , 40000)
print(lp1.brand_name , lp1.model_name, lp1.price)
lp1.apply_discount(20)

