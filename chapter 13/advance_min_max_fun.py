# advance min and max function 

from unicodedata import name


numbers=[1,2,3,4,5,67,]
print(max(numbers))

names=['abu bakar' ,'waheed' , 'moin'] # find the max lentgh of the names 

print(max(names , key=lambda item:len(item)))
print(min(names , key=lambda item:len(item)))

students={
    'abu bakar':{'score':30 ,'age':19},
    'ubaid':{'score':60 ,'age':19},
    'talha':{'score':50 ,'age':19},
}
print(max(students, key=lambda item:students[item]['score']))

# students2=[
#     {'name':'abubakar','score':60 ,'age':19 },
#     {'name':'talha','score':90 ,'age':39 },
#     {'name':'ubaid','score':70 ,'age':9 },
# ]
# print(max(students2 , key=lambda item:item.get('score'))['name'])
# print(min(students2 , key=lambda item:item.get('score')))
# # according to age 
# print(min(students2 , key=lambda item:item.get('age'))['name']) #if we pass the name then it will print only name 

