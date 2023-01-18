
with open('file.txt' , 'r') as f:
    with open('output.txt' , 'a') as wr:
        for line in f.readlines():
            name,salary= line.split(',')
            wr.write(f"the name is {name} and salary is {salary}")

