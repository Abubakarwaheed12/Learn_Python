# funtion practice 
name=input("enter your name   :  ")
def last_char_string(name):
    return name[-1]

print(f"the last character of your name is : " + last_char_string(name))


# funtion practice 
number=int(input("enter any number : "))

def even_odd(number):
    if number%2==0:
        return ("your number is even")
    else:
        return("your number is odd")
print(even_odd(number))

# funtion example 

def is_even(num):
    return num%2==0
print(is_even(9))