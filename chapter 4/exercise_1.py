# PROBLEM 
#  TAKE A NUMBER FROM USER AND SHOW WHICH IS GREATER 

num1=int(input("enter a number 1  : "))
num2=int(input("enter a number 2  : "))

def greater(num1, num2):
    if num1>num2:
        return (f"{num1} is greater than {num2}")
    elif num1<num2:
        return (f"{num2} is  greater than {num1}")
    else:
        return ("both numbers is equal")

print(greater(num1, num2))

