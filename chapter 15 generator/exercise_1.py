
# define a function that return only even numbers with the help of generarotor function

def num(n):
    for i in range(1 , n+1):
        if i%2==0:
            yield i 

number=num(20)
for j in number:
    print(j)
for j in number:
    print(j)