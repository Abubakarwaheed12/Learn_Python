name=input("enter any single word :  ")

def is_palindrome(name):
    if name==name[::-1]:
        return True
    else:
        return False


print(is_palindrome(name))

