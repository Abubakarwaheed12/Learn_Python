import random

win_number=random.randint(1,100)
guess=1
guess_number=int(input("Guess the number"))
game_over=False

while not game_over:
    if win_number==guess_number:
        print(f"you guess this in {guess} times : ")
        game_over=True
    else:
        if guess_number<win_number:
            print("to low")
            guess_number=int(input("Guess Again"))
            guess+=1
        else:
            print("to high")
            guess_number=int(input("Guess Again"))
            guess+=1
    
# The same Code  in DRY DODING WAY  if 
# DRY means don't Repeat Yourself

# win_number=35
# guess=1
# guess_number=int(input("Guess the number"))
# game_over=False

# while not game_over:
#     if win_number==guess_number:
#         print(f"you guess this in {guess} times : ")
#         game_over=True
#     else:
#         if guess_number<win_number:
#             print("to low")
           
#         else:
#             print("to high")
#         guess_number=int(input("Guess Again"))
#         guess+=1
