import random
import random as passgen
import string
import sys
import time
from datetime import datetime
from random import randint
from tkinter import Tk

from PIL import Image

t = datetime.now()
random = random.random()
string.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY_LEN = 20
letters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
passwordint = ""


def load_interface():
    for x in range(100):
        print("[%s] loading...\n" % x, end="")
        time.sleep(0.03)
        if x == 99:
            print("[100] loaded successfully ")


# rip strNophix 1337 password system
"""
def psw_interface():
    test = input("Enter password: ")
    while test != "Hello":
        print("Invalid Password!")
        sys.exit("Access denied")
    print(" - Access granted - ")
"""


def psw_interface():
    password = str(input("Please enter password to continue: "))
    if password == "Hello":
        print(" - Access granted - ")
    else:
        print("Invalid Password!")


def time_interface():
    print("Time = %s:%s:%s" % (t.hour, t.minute, t.second))
    print("Date =  %s/%s/%s" % (t.day, t.month, t.year))
    print(" ")
    print("type <help> for available commands!")


def help_command_interface():
    if commands == "help":
        print("Commands: ")
        print("test {performs a test}")
        print("calc {A calculator}")
        print("clr {clears console}")
        print("RPS {Rock Paper Scissors game}")
        print("screen {opens a window")
        print("cat {opens a pic of the cutes kittycat you'll ever see}")
        print("numbergen {Generates random numbers")
        print("pwdgen {Generates random password")
        print("- More commands soon -")


def test_command_interface():
    if commands == "test":
        print("Hello this is a test.")


def calc_command_interface():
    if commands == "calc":
        num1 = int(input(">>>: Number 1: "))
        num2 = int(input(">>>: Number 2: "))
        oper = input("Choose your operator: % + - * - ")
        if oper == "+":
            print(num1 + num2)
        if oper == "-":
            print(num1 - num2)
        if oper == "*":
            print(num1 * num2)
        if oper == "%":
            print(num1 % num2)


def rps_command_interface():
    actions = ["Rock", "Paper", "Scissors"]
    computer = actions[randint(0, 2)]
    player = True
    while player:
        player = input("Rock, Paper, Scissor\nChoice: ")
        if player == computer:
            print("Draw!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors" or player == "Scissor":
            if computer == "Rock":
                print("You lose!", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("Rock, Paper or Scissor")

        player = False
        computer = actions[randint(0, 2)]


def screen_command_interface():  # strNophix made it :P

    if __name__ == '__main__':
        root = Tk()
        root.title("Test title")
        root.geometry("1920x1080")
        root.mainloop()


def cat_command_interface():
    image = Image.open('images/cat.jpg')
    image.show()


def numbergen_command_interface():
    print("Generated password: ")
    print(randint(100000, 1000000))


def pwdgen_command_interface():
    def pswgen():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 16
        return ''.join(passgen.choice(chars) for x in range(size, 24))

    print("Generated password: ")
    print(pswgen())


def snow_command_interface():
    global actions
    if commands == "snow":
        actions = ["*", " ", " ", "*", " ", " ", "*", " ", "*", " ", "*", " ", " ", " ", "*", " ", " ", "*", " ", " "]
    computer = actions[randint(0, 19)]
    print(computer, end=" ")
    computer = actions[randint(0, 19)]
    print(computer, end=" ")
    computer = actions[randint(0, 19)]
    print(computer, end=" ")
    computer = actions[randint(0, 19)]
    print(computer, end=" ")
    computer = actions[randint(0, 19)]
    print(computer, end=" ")
    print(" ")

    for i in range(999999):
        time.sleep(0.4)


def datingsim_command_interface():
    name = input("What is your name? ")
    print("Hello " + name)
    print("Nice to meet you and oohh nice shoes, wnanna bang lmao")
    bang = input("You want to bang? (yes or no) ")
    if bang == "yes":
        print("Kyaaaaaaaaaaaaa")
    else:
        if bang == "no":
            print("Get the fuck out of my way")
            print("You goofed with the wrong person")
            sys.exit(0)
        else:
            print("Hoe bye")
            sys.exit("Go away u piece of shit")

    print("*Two hours later*")
    print("???: Oeh that was nice")
    print(name + ": Yes, whats your name?")
    print("???: My name is Erwin Rommel, babe")
    haha = input("Erwin Rommel: How about you? ")
    if haha != name:
        print("Your drivers license says something else, u liar *walks away*")
        sys.exit(0)
    else:
        print("Erwin Rommel: Hmmmmm")
        print(name + ": Hey, thats pretty good, but I got to go, ill ttyl *gives phonenumber*")
        phone = int(input("Enter phone number here "))
        print("Erwin Rommel: VERDAMPT JA")
        print(name + ": Bye")

    sjw = input("ARE YOU A SJW? ")
    freunde = input("Habt du freuden? ")
    # More storyline soon
    f = open('dox.txt', 'w')
    f.write('D0X:' + '\n')
    f.write('name = ' + repr(name) + '\n')
    f.write('phone = ' + repr(phone) + '\n')
    f.write('sjw = ' + repr(sjw) + '\n')
    f.write('freunden = ' + repr(freunde) + "\n")
    f.close()
    print("Ty for the dox Kappa")


load_interface()
psw_interface()
time_interface()
commands = input(">>>: ")
while commands != "clr" + "test" + "calc":
    if commands == "test":
        test_command_interface()
    elif commands == "RPS" or commands == "rps":
        rps_command_interface()
    elif commands == "calc":
        calc_command_interface()
    elif commands == "clr":
        print("\n" * 100)
    elif commands == "screen":
        screen_command_interface()
    elif commands == "help":
        help_command_interface()
    elif commands == "cat":
        cat_command_interface()
    elif commands == "numbergen":
        numbergen_command_interface()
    elif commands == "pwdgen":
        pwdgen_command_interface()
    elif commands == "snow":
        snow_command_interface()
    elif commands == "DatingSim" or commands == "datingsim":
        datingsim_command_interface()
    commands = input(">>>: ")
