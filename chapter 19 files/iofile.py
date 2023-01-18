# read file 
# open function
# read , tell , seek method 
# read line , readlines method
# close method 
f=open('ab.txt' ) # it return the the object
# print(f"cursor position - {f.tell()}")
# print(f.read())
# print(f"cursor position - {f.tell()}")
# f.seek(0)


# print(f"cursor position - {f.tell()}")
# print(f.readline() , end='') # read one line on one time 
# print(f.readline(), end='')
# print(f.readline(), end='')
lines=f.readlines()
# print(len(lines))
for line in lines:
    print(line , end="")
print(f.name)
print(f.closed)
f.close()
print(f.closed)