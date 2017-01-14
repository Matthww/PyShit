from random import randint
import time

commands = input(">>>: ")

def snow_command_interface():
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

snow_command_interface()

for i in range(10):
    time.sleep(0.4)
    snow_command_interface()

commands = input(">>>: ")