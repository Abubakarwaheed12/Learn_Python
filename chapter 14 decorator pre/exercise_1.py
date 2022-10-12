# calculate the time of function 

import time

t1=time.time()
def calculate_time(function):
    def wrapper(): 
        t1=time.time()
        print("hi this program is for the time calculation of the program")
        returned= function()
        t2=time.time()
        print(t2-t1)
        return returned
    return wrapper

@calculate_time
def name():
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")
    print("hello how are you")

name()
