from random import randint
import time

commands = input(">>>: ")

def rps_command_interface():
    if commands == "snow":
        actions = ["*", " ", " ", "*", " "]
        computer = actions[randint(0, 3)]
        print(computer, end="")
        computer = actions[randint(0, 3)]
        print(computer, end="")
        computer = actions[randint(0, 3)]
        print(computer, end="")
        computer = actions[randint(0, 3)]
        print(computer, end="")
        computer = actions[randint(0, 3)]
        print(computer, end="")
        print("\n")

rps_command_interface()

for i in range(999999):
    time.sleep(0.3)
    rps_command_interface()