from random import randint

actions = ["Rock", "Paper", "Scissors"]

computer = actions[randint(0, 2)]

player = False

while not player:
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
