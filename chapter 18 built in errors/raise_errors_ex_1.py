# NOT IMPLEMENTED ERROR 
# ABSTRACT METHOD 
# VERY IMPORTANT 
class animal:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        raise NotImplementedError('you have to define the function in subclasses')
    
class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "BHOW BHOW"

class cat(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "MEAO MEAO"

cat=cat('mano', 'pug')
print(cat.sound())