import random
number = random.randint(1, 10)
for chances in range(3):
    guess = int(input("Enter your guess! Any number from 1 to 10."))
    if number < guess:
        print("Your guess is too high! Try again.")     
    elif number > guess:
        print("Your guess is too low! Try again.")
    else:
        print("Yay! You guessed right! Well done.")
        break