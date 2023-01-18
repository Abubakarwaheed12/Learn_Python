# EXAMPLE 2 
# another example of error 
class mobile:
    def __init__(self,name):
        self.name=name
class mobile_store:
    def __init__(self):
        self.mobiles=[]
    def add(self, new_mobile):
        if isinstance(new_mobile, mobile):
            self.mobiles.append(new_mobile)
        else: 
            raise TypeError("only pass instance of mobile")


mob=mobile("one plus 6")
print(mob.name)
sam="samsung"
new=mobile_store()
print(new.add(mob))
print(new.mobiles)
