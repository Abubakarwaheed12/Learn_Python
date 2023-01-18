# fromkey
# unknown value for all the keys 
d=dict.fromkeys(['name','age','phone'],'unknown')
print(d) 
# get
# it is very useful method 
user={
    'name':'abu bakar waheed',
    'age':20,
    'hobby':['computing', 'cricket', 'learn to code'],
}

a=user.get('name')
print(a)

if user.get('name'):
    print("present")
else:
    print("not present")

# copy
d1=dict(user.copy())
print(d1)
# clear 
print(user.clear())



