# function with all type of parameters 

# def fun(param,  *args,  defualt_parameter, **args)

# keep it mind the order of args and parms
# PADK
def fun(name,*args ,lname="unknown" ,**kwargs):
    print(name , args , lname , kwargs)

print(fun('abubakar' , 12,3,3 , lna="abubajae"))