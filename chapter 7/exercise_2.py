name=input("enter name")
age=int(input("enter age"))
songs=input("enter favourite songs").split(',')

def dic_gen(name ,age , songs):
    data={}
    data['name']=name
    data['age']=age
    data['songs']=[songs]
    for key ,value in data.items():
        print(f"{key}  :   {value}")

    
    return data

print(dic_gen(name,age,songs))
    