import os
import random

def guess_command_interface():

    if os.path.isfile('../media/insults.txt'):
        insults = 'yes'
        file = open('../media/insults.txt', 'r')
        list = file.readlines
    else
        insults = "no"

    print("Welcome to guess the number")
    print("===========================")
    print(" ")
    print("I'm thinking of a number, you have to guess what it is.")
    print("The number is between 0-100 Good luck!")
    print(" ")

    num = random.randrange(100)
    guess = ""

    while guess != num
        guess = int(input("Take a guess: "))
        if guess < num:
            if insults == "yes":
                print(random.choice(list))
            print("Guess higher next time :)\n")
        elif guess > num:
            if insults == "yes"
                print(random.choice(list))
            print("Guess lower next time :P\n")
    if insults == "yes":
        file.close


commands = input(">>>: ")
while commands != "clr" + "test" + "calc":
    if commands == "guess":
        guess_command_interface()