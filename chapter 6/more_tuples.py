days=("staurday","sunaday","monday","tuesday","wednesday","thursday","friday")

print(days[-1])

for i in days:
    print(i)

#comma is nesseccary otherwise pyhton not consider that is  tuple 
# for exampla
# a=(1)
# so change is  write comma at end then python consider its a tuple
a=(1,)
print(type(a))

# list in inside the tuple 

days=("staurday","sunaday","monday",["tuesday","wednesday","thursday","friday"])

print(days[3].pop())

print(days)

#    we can unpack the tuple values 
#  we can use min , mac ,sum functions in tuple 

t=(1,2,34,5,)
print(max(t))

#  we can create a tuple through a range function 

abc=tuple(range(1,33))
print(abc)

# we can change tuple to list

abc=list(tuple(range(1,33)))
print(abc)
