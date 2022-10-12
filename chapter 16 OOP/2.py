# INSTANCE METHODS IN CLASS 
# INSTANCE AND OBJECT IS SAME THING 
# FUNCTION INSIDE THE CLASS IS CALLED A METHOD 

class person:
    def __init__(self , fname , lname):
        self.fname=fname
        self.lname=lname

    def full_name(self):
        return f"{self.fname} {self.lname}"

p=person("abu bakar" , "waheed")
print(p.full_name())