# lambda function is used by built in functions for example map ()
# reduce filter map
# simple function 
# annynomous function

# practice of lambda function
# is even function 
def ev_odd(a):
    if a%2==0:
        return True
    return False

print(ev_odd(3))
# same program in lambda function 
is_even=lambda a : a%2==0

print(is_even(5))

# if else with lambda expression 
# check the lenghth is greater than 5 or not 
a=lambda a:len(a)>5

print(a('dsaasddf'))