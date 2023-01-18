import random 
num=(random.randint(0,9))
inp=input("guess numer")
inp=int(inp)
if num==inp: 
    print("YOU WIN")
else:
    if inp<num:
        print("too low")
    else:
            print("too high")
