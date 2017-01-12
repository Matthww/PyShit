from datetime import datetime
from random import randint
import random
import sys
import time
import os

t = datetime.now()
random = random.random()

for x in range(100):
    print("[%s] loading...\n" % x, end="")
    time.sleep(0.03)
    if x == 99:
        print("[100] loaded succesfully ")

test = input("Enter password: ")
while test != "Hello":
    print("Invalid Password!")
    sys.exit("Access denied")

print(" - Access granted - ")
t = datetime.now()

print('Year = %s' % t.year)
print('Month = %s' % t.month)
print('Day = %s' % t.day)
print('Hour = %s' % t.hour)
print('Minutes = %s' % t.minute)
print('Microsecond = %s' % t.microsecond)

print("Time = %s:%s:%s" % (t.hour, t.minute, t.second))
print("Date =  %s/%s/%s" % (t.day, t.month, t.year))

commands = input(">>>: ")
while commands != "clr" + "test" + "calc":
    commands = input(">>>: ")
    if commands == "clr":
        print("\n" * 100)
    elif commands == "help":
        print("Commands: ")
        print("test {performs a test}")
        print("calc {A calculator}")
        print("clr {clears console}")
        print("RPS {Rock Paper Scissors game}")
        print("screen {opens a test window")
        print("- More commands soon -")
    elif commands == "test":
        print("Hello this is a test.")
    elif commands == "calc":
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
    elif commands == "RPS":
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
            player = input("Rock, Paper, Scissor or EXIT\nChoice: ")
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
            elif player == "EXIT":
                player = False
            else:
                print("Rock, Paper, Scissor or EXIT")

            player = False
            computer = actions[randint(0, 2)]
    elif commands == "screen":
        class startWindow(Frame):
            def __init__(self, parent=None):
                Frame.__init__(self, parent)
                Frame.pack(self)
                Label(self, text='Test', width=72).pack()


        if __name__ == '__main__':
            root = Tk()
            root.title("Test title")
            root.geometry("1920x1080")
            app = startWindow(root)
            root.mainloop()
