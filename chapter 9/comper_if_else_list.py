# list comprehension with if else statement

l=[1,2,3,4,5,6,7,8,9]

new_list=[i*2 if (i%2==0) else -i for i in l]

print(new_list)