num=1
total=0
while num<=10:
    total +=num
    num+=1
print(total)

#  same program in for loop
nam=1
eq=0

for name in range(10):
    eq+=nam
    nam+=1

print(eq)


# sum of numbers in string
# user_input=input("enter more than one numbers")
# tot=0
# for i in range(0 , len(user_input)):
#     tot+=int(user_input[i])
# print(tot)

#  ex: 4 ask username and print the index and character 
name=input("enter your name")
tem=""
for i in range(0, len(name)):
    if name[i] not in tem:
        print(f"{name[i]} : {name.count(name[i])}")
        tem+=name[i]

