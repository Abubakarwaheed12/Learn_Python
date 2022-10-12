
class laptop:
    discount=10


    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price

    def apply_discount(self):
        r= (self.discount/100)*self.price
        print(f"discount price  is {r}")


# object 
lp1=laptop('hp' , "core i 5" , 40000)
lp1.discount=20
print(lp1.brand_name , lp1.model_name, lp1.price)
print(lp1.apply_discount())

print(lp1.__dict__)

# PEHLY OBJECT VARIABLE  PASS HOGA OTHERWISE PYHTON CLASS WALA USE KAR GAA 