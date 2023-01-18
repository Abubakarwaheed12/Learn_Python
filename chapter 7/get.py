user={
    'name':'abu bakar waheed',
    'age':20,
    'age':78,
    'hobby':['computing', 'cricket', 'learn to code'],
}
#  it return none if key not found
#  its only used when you want to return anything else in the place of none 
print(user.get('name', 'not found'))

# if two keys same in the dictionary
# it acces the last key in the same keys 
print(user.get('age'))

# so it  reuturn the 78 bcz its in the last key 
