
def validate(name):
    if len(name)<8:
        raise ValueError("name is too short")

name=input("enter your name ... ")
validate(name)
print(f"hello {name}")