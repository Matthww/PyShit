import random
import random as passgen
import sys
import time
import string
from datetime import datetime
from random import randint
from tkinter import Frame, Label, Tk
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


def psw_interface():
    test = input("Enter password: ")
    while test != "Hello":
        print("Invalid Password!")
        sys.exit("Access denied")
    print(" - Access granted - ")


def time_interface():
    print("Time = %s:%s:%s" % (t.hour, t.minute, t.second))
    print("Date =  %s/%s/%s" % (t.day, t.month, t.year))
    print("\n")
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
    if commands == "RPS":
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
    print("W.I.P")


load_interface()
psw_interface()
time_interface()
commands = input(">>>: ")
while commands != "clr" + "test" + "calc":
    if commands == "test":
        test_command_interface()
    elif commands == "RPS":
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
    commands = input(">>>: ")
