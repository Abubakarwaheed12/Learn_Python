# INHERITENCE 


class phone:
    def __init__(self , brand , model_name , price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price , 0)

    def full_name(self):
        return f"full nae is {self.brand}   {self.model_name}"
        
    def make_a_call(self, phone):
        return f"calling {phone} ......"

    