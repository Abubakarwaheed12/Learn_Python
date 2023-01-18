age=input("enter your age ")
age=int(age)
if age==0:
    print("you can't watch")
elif 0<age<3:
    print("free")
elif 3<age<10:
    print("100")
elif 10<age<23:
    print("150")
elif 23<age<50:
    print("299")
else:
    print("500")