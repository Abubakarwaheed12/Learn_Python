# DEBUGGING MEANS FINDING THE ERROR IN THE CODE 
import pdb
# set trace 
# execute code line by line n
pdb.set_trace()
name=input("enter name ..")
age=input("enter age ..")
print(f"hello {name} and {age}")
age2=int(age)+5
print(f" five next years of your {name} then {age}")