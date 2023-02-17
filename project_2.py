from random import randrange
from time import sleep


def rand_dice():
    m, n = randrange(1, 7), randrange(1, 7)
    print(f"The sum of dice is {m} + {n} = {m + n}")
    return m + n

player_wins = [7, 11]
casino_wins = [2, 3, 12]
a= rand_dice()

if a in player_wins:
    print("You won")
elif a in casino_wins:
    print("You lose")
else:
    print(f"Now your goal number is {a}")
    print("You lose if number is 7")
    player_wins = a
    casino_wins = 7
    sleep(1.5)
    
    while True:
        a = rand_dice()
        if a == player_wins:
            print("You won")
            break
        elif a == casino_wins:
            print("You lose")
            break
        sleep(1.5)
