l=[True,False ,1,2,3, 1.0 ,[1,2,3,4]]

def list_fun(l):
    new_list=[str(i) for i in l if type(i)==int or type(i)==float]
    print (new_list)

list_fun(l)
