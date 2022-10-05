def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else: 
        return c


def greate(num1, num2):
    if num1>num2:
        return num1
    elif num1<num2:
        return num2

def new_greater(a,b,c):
    bigger=greate(a,b)
    return greate(bigger, c)

print(new_greater(144,34,32))
