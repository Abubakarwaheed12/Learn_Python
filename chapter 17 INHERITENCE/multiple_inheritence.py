# MLTIPLE INHERITENCE 

class A:
    def mth1(self):
        return "hello i am just CLASS A "
    def mth(self):
        return "i am class a method "
class B:
    def mth2(self):
        return "hello i am just CLASS B "
    def mth(self):
        return "i am class B method "
    
class  C(A,B):
    pass

obj1=C()
print(obj1.mth())