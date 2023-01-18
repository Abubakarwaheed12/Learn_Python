# comm elementer finder in two lists 

def common_element_finder(a,b):
    new_list=[]
    for i in a:
        if i in b:
            new_list.append(i)
    return new_list
a=[1,3,4,5,3]
b=[1,2,34,5,23]
print(common_element_finder(a,b))