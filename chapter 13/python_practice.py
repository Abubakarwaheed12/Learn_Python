# any and all function 
n1=[2,4,6,8,0]
n2=[1,3,5,7,5,6,9]

n3=all([i%2==0 for i in n2])
n3=any([i%2==0 for i in n2])
print(n3)

# more practice of this function 
def mysum(*args):
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        tot=0
        for i in args:
            tot +=i
        return tot
    else:
        print ('wrong input')

print(mysum(1,2,4,))