
number=list(range(1,29))

# print(number)

# print(number.index(1))

# print (number.pop())

def negative(l):
    neg=[]
    for i in l:
        neg.append(-i)
    return neg
print(negative(number))