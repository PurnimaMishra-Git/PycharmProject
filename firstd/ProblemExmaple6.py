'''
**************************Guess the number**********************************

Generate a random integer from a to b.You and your friend have to guess a number between two number a and b.
 a nd b are input from the user
Your friend is player 1 and plays first.He will have to keep choosing a numberand your program must tell whether a number
is greater than the actual number or less than the actual number. log the number of trials it took your friend to arive
at the number
you play he same game and then the person with minimum no of trials Wins!!

Randomly generate a number and dont show it to user
'''

import random

chance=9
_guess=0

a=int(input("Enter starting range number: "))
b=int(input("Enter ending range number: "))
number_range=random.randint(a, b)
print("Player 1 Guess game \n")
while _guess<chance:
    _guess=_guess+1
    guess=0
    player1_input=int(input("Enter number: "))
    if player1_input > number_range:
        guess=guess+1
        print("You guessed wrong enter less than it")
    elif player1_input < number_range:
        guess = guess + 1
        print("You guessed wrong enter greater than it")
    elif player1_input == number_range:
        guess=guess+1
        print(f"Correct number!!!\nNumber of guess you took {_guess}")
        break
number_range1=random.randint(a, b)
print(number_range)
print("Player 2 Guess game \n")
_guess1=0
while _guess1<chance:
    _guess1=_guess1+1
    guess=0
    player2_input=int(input("Enter number: "))
    if player2_input > number_range1:
        guess=guess+1
        print("You guessed wrong enter less than it")
    elif player2_input < number_range1:
        guess = guess + 1
        print("You guessed wrong enter greater than it")
    elif player2_input == number_range1:
        guess=guess+1
        print(f"Correct number!!!\nNumber of guess you took {_guess1}")
        break
if _guess>_guess1:
    print(f"Player 1 Win the match and the number was {number_range}!!!")
elif _guess<_guess1:
    print(f"Player 2 won the match and the number was {number_range1}!!!")
else:print("It's a tia!!!")




