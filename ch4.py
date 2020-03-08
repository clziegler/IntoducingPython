import random

secret = random.randint(1, 100)


for x in range(1, 11):
    guessed_number = input("Guess a number between 1 and 100 \n")
    if guessed_number == secret:
        print("You guessed the number in {} tries".format(x))
        break
    else:
        if guessed_number < secret:
            print("The number is greater than {}. Guesses remaining: {}".format(guessed_number, 10 - x))
        elif guessed_number > secret:
            print("The number is less than {} Guesses remaining: {}".format(guessed_number, 10 - x))
        else:
            print("I didn't understand what you typed!")
else:
    print('You didnt find the number. It was {}'.format(secret))

