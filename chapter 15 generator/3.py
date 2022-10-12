# generator comprehension 

square=[i**2 for i in range(1,11)]
print(square)
#  we can change it into a generator 

square=(i**2 for i in range(1,11))
for num in square:
    print(num)
    

# n=square
# new_list=[]
# for i in n:
#     new_list.append(i)
# print(new_list)