import random

print("Number Guessing Game")
number= random.randint(1,9)
print("guess a number between 1 and 9")
chances=0

while chances < 5:
    guess= int(input("Enter your guess"))
    if guess== number:
        print("CONGRATULATIONS, You Won!")
        break
    elif guess > number:
        print("Try a number lower than ",guess)
    else:
        print("Try a number higher than ",guess)
    chances+=1
if not chances <5:
    print("You lost. The number is ",number)