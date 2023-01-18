# ENCAPSULATION
# ABSTRACTION
# SPECIAL NAMING CONVENTIONS
# NAME MANGLING 

# EX
# _LNAME ISKA MATLAB HA K YE AIK PRIVATE METHOD HA / convention for private 
# __name__ dunder or magic methods
class person:
    def __init__(self , fname , lname):
        self.fname=fname
        self.lname=lname

    def full_name(self):
        return f"{self.fname} {self.lname}"

p=person("abu bakar" , "waheed")
print(p.full_name())