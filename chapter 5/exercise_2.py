#  this program is return a reversed list


# def reverse_list(l):
#     l.reverse()
#     return l

# my_list=[1,2,3,4,5,6,7,8,9]
# print(reverse_list(my_list))

# same thing with string slicing method


# def reverse_list(l):
#     return l[::-1]

# my_list=[1,2,3,4,5,6,7,8,9]
# print(reverse_list(my_list))

# same thing with append and pop method

def reverse_list(l):
    newl=[]
    for i in range(len(l)):
        ap=l.pop()
        newl.append(ap)
    return newl

my_list=[1,2,3,4,5,6,7,8,9]
print(reverse_list(my_list))