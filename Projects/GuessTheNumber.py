import random


def guess_command_interface():
    print("Welcome to guess the number")
    print("===========================")
    print(" ")
    print("I'm thinking of a number, you have to guess what it is.")
    print("The number is between 0-100 Good luck!")
    print(" ")

    num = random.randrange(100)
    guess = ""

    while guess != num:
        guess = int(input("Take a guess: "))
        if guess < num:
            print("Guess higher next time :)\n")
        elif guess > num:
            print("Guess lower next time :P\n")
    print("CONGRATULATIONS!")
    input()


commands = input(">>>: ")
while commands != "clr" + "test" + "calc":
    if commands == "guess":
        guess_command_interface()
