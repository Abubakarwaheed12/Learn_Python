name=input("enter eny single word :  ")

def is_palindrome(name):
    if name[0]==name[-1]:
        return True
    else:
        return False
print(is_palindrome(name))
