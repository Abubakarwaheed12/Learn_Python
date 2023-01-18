#  loop 
user={
    'name':'abu bakar waheed',
    'age':20,
    'hobby':['computing', 'cricket', 'learn to code'],
}

for i  in user:
    print(i)

# check if key exist in dict
if 'name' in user:
    print("present")
else:
    print("not present")

# check if value exist in dict
if 'abu bakar waheed' in user.values():
    print(True)
else:
    print(False)

# looping in dictionaries 
for i  in user:
    print(user[i])


#  most important method items method 

user_items=user.items()
print(user_items)

for key,value in user_items:
    print(f"{key} : {value}")
