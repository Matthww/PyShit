import random
import sys
import time
from datetime import datetime
from random import randint
from tkinter import Frame, Label, Tk
from PIL import Image

t = datetime.now()
random = random.random()

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
    t = datetime.now()
    print('Year = %s' % t.year)
    print('Month = %s' % t.month)
    print('Day = %s' % t.day)
    print('Hour = %s' % t.hour)
    print('Minutes = %s' % t.minute)
    print('Microsecond = %s' % t.microsecond)

    print("Time = %s:%s:%s" % (t.hour, t.minute, t.second))
    print("Date =  %s/%s/%s" % (t.day, t.month, t.year))


def help_command_interface():
    if commands == "help":
        print("Commands: ")
        print("test {performs a test}")
        print("calc {A calculator}")
        print("clr {clears console}")
        print("RPS {Rock Paper Scissors game}")
        print("screen {opens a window")
        print("cat {opens a pic of the cutes kittycat you'll ever see}")
        print("pwd {Generate random numbers")
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
            time.sleep(2.5)
            print("\n" * 40)
            print("Loading.")
            time.sleep(0.6)
            print("\n" * 40)
            print("Loading..")
            time.sleep(1.2)
            print("\n" * 40)
            print("Loading...")
            time.sleep(0.5)
            print("\n" * 40)
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
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose!", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
            else:
                print("Rock, Paper or Scissors")

            player = False
            computer = actions[randint(0, 2)]


def screen_command_interface():  # strNophix made it :P
    class openWindow(Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            Frame.pack(self)
            Label(self, text='Test', width=72).pack()

    if __name__ == '__main__':
        root = Tk()
        root.title("Test title")
        root.geometry("1920x1080")
        app = openWindow(root)
        root.mainloop()


def cat_command_interface():
    image = Image.open('images/cat.jpg')
    image.show()


def pwdgen_command_interface():
    print("Generated password: ")
    print(randint(100000, 1000000) + 123)


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
    elif commands == "pwd":
        pwdgen_command_interface()
    commands = input(">>>: ")
