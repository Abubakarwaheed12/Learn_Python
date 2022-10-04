# for i in range(1,11):
#     print(f"abu bakar  ::  {i}")


#  sum 1-21 numbers 

# total=0
# for i in range(1,21):
#     total +=i

# print(total)

# number=input("enter more than one numbers")
# # number=int(number)
# total=0
# for i in range(0 , len(number)+ 1):
#     total+=i
# print(total)

# ask username input and show index and numbers
name=input("enter your name")
temp=""
for i in range(0 , len(name)+1):
    if name[i] not in temp:
        print(f"{name[i]}  :  {name.count(name[i])}")
    temp+=name[i]


