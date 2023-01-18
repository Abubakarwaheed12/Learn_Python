# set data type 
# unordered collection of uniue items 
# no indesxing in sets 
# no dupplication in sets 

from copy import copy

#  we cannot store dict and list  in sets 

my_set={1,1,2,3,4}
# here no 1 is duplicate so it  prints only one time 
print(my_set)

# for example if we want to remove the duplicate values from list
#  this is important use of sets 
l=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,3,4,5,6,7,8,9,0]

# when we  create set the set remove All the duplicate values from list ok 
s=set(l)
print(s)

# methods of sets
s.add(11)
s.remove(2)
s.discard(34)
# s.clear()
s1=copy(s)
print(s)
print(s1)