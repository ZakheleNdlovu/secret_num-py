import random
import time


def play(number):
    lives = 5
    print("Press (00) to exit")
    while lives > 0:
       print(f"You have {lives} lives remaining")
       try:
           guess = int(input("Enter your guess: "))
           if guess == 00:
               print("Thank you for playing secret number :)")
               exit(0)
           while guess < 0 and guess > 9:
               print("Your guess must be between 1 and 9\n")
               guess = int(input("Enter your guess: "))
           if guess == number:
               time.sleep(1)
               print("You got it!")
               break
           else:
               if guess > number:

                   print("Your guess is higher than the secret number")
                   lives -=1
               else:

                   print("Your guess is lower than the secret number")
                   lives -=1
       except ValueError as e:
           print("please enter a number")
    else:
        print("You are out of lives, Game over")
        time.sleep(2)


while True:
    number = random.randint(1, 9)
    print("This is a number guessing game, you are given 5 chances to guess a number between 1 and 9")
    play(number)
    play_again = input("Do you want to play again?\n: ")
    while len(play_again) > 1:
        print("Enter a (y) for Yes or (n) for No")
        play_again = input(": ")
    while play_again.lower() == 'y':
        number = random.randint(1, 9)
        play(number)
        play_again = input("Do you want to play again?\n: ")
    if play_again.lower() == 'n':
        print("Thank you for playing :)")
        break