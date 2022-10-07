#  for the help of list comprehension we can create list in one line

#  square of 1 to 10 numbers in one line 

square=[]
for i in range(1,11):
    square.append(i*i)
    print(i)

print(square)

# list comprehension way
#  same output but short code
s2=[i*i for i in range(1,11)]
print(s2)

# example 2 
s=[]
for j in range(1,11):
    s.append(-j)
print(s)

# list coprehension 
s1=[-i for i in range(1,11)]
print(s1)

#  example program 
names=["abu bakar " ,"talha" , "ubaid"]
new_name=[]
for name in names:
    new_name.append(name[0])
print(new_name)

# same in list comprehension
names=["abu bakar " ,"talha" , "ubaid"]
new=[nam[0] for nam in names]

print(new)