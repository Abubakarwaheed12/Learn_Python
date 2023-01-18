
class laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price

# object 
lp1=laptop('hp' , "core i 5" , 40000)

print(lp1.brand_name , lp1.model_name, lp1.price)


