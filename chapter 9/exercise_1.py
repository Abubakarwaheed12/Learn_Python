#  function that return reverse string 
l=["abc" , "def" , "ghi"]
def rev(l):
    new_list=[name[::-1] for name in l]

    return new_list;
print(rev(l))
