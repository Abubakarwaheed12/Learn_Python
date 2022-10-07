
#  only append even numbers 
l=[1,2,3,4,5,6,7,8,9]

newl=[i for i in l if i%2==0]
new=[i for i in l if i%2 !=0]

print(newl)
print(new)
