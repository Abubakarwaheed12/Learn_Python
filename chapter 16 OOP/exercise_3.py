
from itertools import count


class person:
    count_instance=0
    def __init__(self):
        print('ewjsbhaf')
        person.count_instance +=1

p1=person()
p2=person()
p3=person()

print(person.count_instance)