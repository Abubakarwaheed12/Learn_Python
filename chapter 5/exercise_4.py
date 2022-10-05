# take a list from user of numbers and output the even and odd in separate

def n_lis(l):
    even_l=[]
    odd_l=[]
    for i in l:
        if i % 2==0:
            even_l.append(i)
        else:
            odd_l.append(i)
    output= [even_l,odd_l]
    return output

ab=[1,2,3,4,5,6,7,8,9]
print(n_lis(ab))

