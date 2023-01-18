# OOPS
# WHHAT IS CLASS 
# WHAT IS __INIT__
# WHAT IS METHOD

class person:
    # constructer function 
    def __init__(self,fname,lname,age):
        print("constructer called")
        self.fname=fname
        self.lname=lname
        self.age=age

# creating ibject of thos class 
p1=person('abu bakar waheed' , 'waheed ahmad' , 20)
p1=person('abu bakar waheed' , 'waheed ahmad' , 20)

print(p1.fname,p1.age,p1.lname)
print(p1.age)
print(p1.lname)