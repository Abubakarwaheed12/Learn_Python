# FIRTS WE WILL DISCUUSS ABOUT CLASS METHODS

# STATIC METHOD IS NOT RELATED TO CLASS AND INSTANCE BUT IT HAS A LOGICAL CONNECTION TO CLASS

class person:
    # constructer function 
    def __init__(self,fname,lname,age):
        print("constructer called")
        self.fname=fname
        self.lname=lname
        self.age=age
    # define a static method 
    @staticmethod
    def hello():
        print("hello STATIC METHOD CALLED")


    # @classmethod
    # def fromstring(cls,string):
    #     fname,lname,age=string.split(',')
    #     return cls(fname, lname ,age)

    def is_above(self):
        return self.age>18
# creating ibject of thos class 
p1=person('abu bakar waheed' , 'waheed ahmad' , 20)
p1=person('abu bakar waheed' , 'waheed ahmad' , 20)
print(p1.fname,p1.age,p1.lname)
print(p1.age)
print(p1.lname)
print(p1.is_above())

print(p1.hello())


# class method 
# p4=person.fromstring('abu bakar waheed 23')
# print(p4.is_above())