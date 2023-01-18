# with block /context manager 

with open('file.txt') as f:
    data= f.read()
    print(data)

#  in this no need to close the file file closed automatkcally 

print(f.closed)