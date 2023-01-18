# very important function 
#  map function 
# map is iterable 
import numbers


def saquare(a):
    return a*a

print(saquare(3))

# in map function 
a=[1,2,3,4,5,6,7,8,9]
b=list(map(saquare , a))
# but we can convert it into a list
print(b)

# with lambda funtion
c=list(map(lambda d:d**2 , a))
print(c)

# with list comp
new_list=[i**2 for i in a]
print(new_list)
# with for loop 
n=[]
for y in a:
    n.append(saquare(y))
print(n)
# there are many to solve a one problem 

# program for finding a length of list items 
names=['abu bakar', 'waheed', 'moin']
length=map(len , names)
for x in length:
    print (x)
