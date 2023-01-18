# n=int(input("enter a number"))
# def cube_finder(n):
#     num={}
#     i=1
#     while i<=n:
#         val=i**3
#         i+=1
#         num[i]=val
#     return num

# print(cube_finder(3))

# another simple way
n=int(input("enter a number"))
def cube_finder(n):
    num={}
    for i in range(1,n+1):
        num[i]=i**3

    return num

print(cube_finder(n))



