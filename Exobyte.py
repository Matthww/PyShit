from datetime import datetime
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
        print("[100%] loaded succesfully ")

test = input("Enter password: ")
while test != "Hello":
    print("Invalid Password!")

print(" - Access granted - ")
time = datetime.now()

print('Year = %s' % time.year)
print('Month = %s' % time.month)
print('Day = %s' % time.day)
print('Hour = %s' % time.hour)
print('Minutes = %s' % time.minute)
print('Microsecond = %s' % time.microsecond)

print("Time = %s:%s:%s" % (time.hour, time.minute, time.second))
print("Date =  %s/%s/%s" % (time.day, time.month, time.year))

commands = input(">>>: ")
while commands != "clr" + "test" + "calc":
    commands = input(">>>: ")
    if commands == "clr":
        print("\n" * 100)
    elif commands == "help":
        print("Commands:\ntest {performs a test}\ncalc {A calculator}\nclr {clears console}\nRPS {Rock Paper scissors game}")
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
    elif command == "RPS":
        actions = ["Rock", "Paper", "Scissors"]
        computer = actions[randint(0, 2)]
        player = False
        while not player:
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