# practice for advance functions 
# average finder program for two lists

from pdb import line_prefix


l1=[1,2,3]
l2=[7,8,9]
l3=[4,5,6]


# def avg_finder(*args):
#     avg=[]
#     for pair in zip(*args):
#         avg.append(sum(pair)/len(pair))
#     return avg
# print(avg_finder(l1,l2,l3))
# same program in one line
average=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average(l1,l2,l3))