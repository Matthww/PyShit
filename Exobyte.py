import random
import random as passgen
import string
import sys
import time
from datetime import datetime
from random import randint
from tkinter import Tk
import pyowm
# PIL is replace by Pillow in requirements.txt
from PIL import Image
from termcolor import colored, cprint

from media.password import password

# All defined stuff
t = datetime.now()
random = random.random()
current_password = password

""" Old Loading stuff from @strNophix
    for x in range(100):
        print("[%s] loading...\n" % x, end="")
        time.sleep(0.03)
        if x == 99:
            print("[100] loaded successfully ")
"""


def load_interface():
    print('\n' * 100)
    text = colored('Loading Exobyte', 'cyan', attrs=['bold'])
    print(text)
    for x in range(101):
        time.sleep(0.09)
        sys.stdout.write("\r%d%%" % x)
        sys.stdout.flush()

        if x == 100:
            print('\n' * 100)
            text = colored('Loaded Exobyte successfully!', attrs=['bold'])
            print(text)
            # print('Loaded Exobyte successfully!')
            text = colored("100%", attrs=['bold'])
            print(text)
            # print('100%')
            time.sleep(2.0)
            print('\n' * 100)


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
    text = colored('Exobyte system©', 'red', attrs=['bold'])
    print(text)
    # print('Exobyte system©')
    print(' ')
    print('default password: Hello')
    print('change your password with: chpass')
    password = str(input("Please enter password to continue: "))
    if password == current_password:
        print("\n" * 100)
        text = colored('- Access Granted -', 'green', attrs=['bold'])
        print(text)
    else:
        print("\n" * 100)
        text = colored('Invalid password!', 'red', attrs=['bold'])
        print(text)
        time.sleep(2)
        print("\n" * 100)
        text = colored('Access Denied!', 'red', attrs=['bold'])
        print(text)
        sys.exit()


def changepsw_interface():
    current_pass = input("Enter your current password: ")
    if current_pass == password:
        new_pass = input("Enter you new password: ")
        f = open('media/password.py', 'w')
        f.write('password = ' + repr(new_pass) + '\n')
        f.close()
    else:
        text = colored('Invalid password!', 'red', attrs=['bold'])
        print(text)


def time_interface():
    print("Time = %s:%s:%s" % (t.hour, t.minute, t.second))
    print("Date = %s/%s/%s" % (t.day, t.month, t.year))
    print(" ")
    text = colored('Welcome to Exobyte system!', 'green')
    print(text)
    # print("Welcome to Exobyte system!")
    # print("type <help> for available commands!")
    text = colored('<help>', attrs=['bold'])
    print("type", text, "for available commands!")


def help_command_interface():
    cmd_cmd = lambda x: cprint(x, 'grey', 'on_white')
    cmd_cmd('Commands:')
    cmd_test = colored('test', attrs=['underline'])
    print(cmd_test + " {performs a test}")
    cmd_calc = colored('calc', attrs=['underline'])
    print(cmd_calc + " {A calculator}")
    cmd_clr = colored('clr', attrs=['underline'])
    print(cmd_clr + " {clears console}")
    cmd_rps = colored('rps', attrs=['underline'])
    print(cmd_rps + " {Rock Paper Scissors game}")
    cmd_screen = colored('screen', attrs=['underline'])
    print(cmd_screen + " {opens a window}")
    cmd_cat = colored('cat', attrs=['underline'])
    print(cmd_cat + " {opens a pic of the cutes kitty cat you'll ever see}")
    cmd_numgen = colored('numgen', attrs=['underline'])
    print(cmd_numgen + " {Generates random numbers}")
    cmd_passgen = colored('passgen', attrs=['underline'])
    print(cmd_passgen + " {Generates a random password}")
    cmd_chpass = colored('chpass', attrs=['underline'])
    print(cmd_chpass + " {Change your login password}")
    cmd_guess = colored('guess', attrs=['underline'])
    print(cmd_guess + " {Guess the number}")
    cmd_snow = colored('snow', attrs=['underline'])
    print(cmd_snow + " {Shitty falling snow}")
    cmd_datingsim = colored('datingsim', attrs=['underline'])
    print(cmd_datingsim + " {A dating simulator}")
    cmd_weather = colored('weather', attrs=['underline'])
    print(cmd_weather + " {Check the weather}")
    cmd_soon = lambda x: cprint(x, 'grey', 'on_white')
    cmd_soon('- More commands soon -')


def test_command_interface():
    print("Hello this is a test.")


def calc_command_interface():
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
        player = input("Rock, Paper, Scissors\nChoice: ")
        if player == computer:
            text = colored('Draw', 'yellow', attrs=['bold'])
            print(text)
        elif player == "Rock" or player == "rock":
            if computer == "Paper":
                text = colored("You lose! Paper covers Rock", 'red', attrs=['bold'])
                print(text)
                # print("You lose!", computer, "covers", player)
            else:
                text = colored("You win! Rock smashes Scissors", 'green', attrs=['bold'])
                print(text)
                # print("You win!", player, "smashes", computer)
        elif player == "Paper" or player == "paper":
            if computer == "Scissors":
                text = colored("You lose! Scissors cut Paper", 'red', attrs=['bold'])
                print(text)
                # print("You lose!", computer, "cut", player)
            else:
                text = colored("You win! Paper covers Rock", 'green', attrs=['bold'])
                print(text)
                # print("You win!", player, "covers", computer)
        elif player == "Scissors" or player == "Scissor" or player == "scissors" or player == "scissor":
            if computer == "Rock":
                text = colored("You lose! Rock smashes Scissors", 'red', attrs=['bold'])
                print(text)
                # print("You lose!", computer, "smashes", player)
            else:
                text = colored("You win! Scissors cut Paper", 'green', attrs=['bold'])
                print(text)
                print("You win!", player, "cut", computer)
        else:
            text = colored("Rock, Paper or Scissors", 'red', attrs=['bold'])
            print(text)
            # print("Rock, Paper or Scissors")

        player = False
        computer = actions[randint(0, 2)]


def weather_command_interface():
    weather_command = input("Your place: (example: London,UK) ")
    owm = pyowm.OWM('797153f746aae22307499da4ad723468')

    observation = owm.weather_at_place(weather_command)
    w = observation.get_weather()
    print(w)

    wind = w.get_wind()
    temp = w.get_temperature('celsius')
    print(wind)
    print(temp)


def screen_command_interface():  # strNophix made it :P

    if __name__ == '__main__':
        root = Tk()
        root.title("Test title")
        root.geometry("1920x1080")
        root.mainloop()


def cat_command_interface():
    image = Image.open('media/cat.jpg')
    image.show()


def numbergen_command_interface():
    # print("Generated number password: ")
    # print(randint(100000, 1000000))
    def numgen():
        num_length = int(input("Password length: "))
        chars = string.digits
        size = num_length
        text = colored("Generated password: ", 'blue', attrs=['bold'])
        print(text)
        # print("Generated password: ")
        return ''.join(passgen.choice(chars) for x in range(size))

    text = colored("", 'red')
    print(text, numgen())


def pwdgen_command_interface():
    def pswgen():
        psw_length = int(input("Password length: "))
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = psw_length
        text = colored("Generated password: ", 'blue', attrs=['bold'])
        print(text)
        # print("Generated password: ")
        return ''.join(passgen.choice(chars) for x in range(size))

    text = colored("", 'red')
    print(text, pswgen())


def snow_command_interface():
    actions = [" ", "*", " ", " ", " "]
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    computer = actions[randint(0, 4)]
    print(computer, end="")
    print(" ")


def datingsim_command_interface():
    name = input("What is your name? ")
    print("Hello " + name)
    print("Nice to meet you and oohh nice shoes, wanna bang lmao")
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
        print(name + ": Hey, that's pretty good, but I got to go, ill ttyl *gives phone number*")
        phone = int(input("Enter phone number here "))
        print("Erwin Rommel: VERDAMPT JA")
        print(name + ": Bye")

    sjw = input("ARE YOU A SJW? ")
    freunde = input("Habt du freunden? ")
    # More storyline soon
    f = open('media/dox.txt', 'w')
    f.write('D0X:' + '\n')
    f.write('name = ' + repr(name) + '\n')
    f.write('phone = ' + repr(phone) + '\n')
    f.write('sjw = ' + repr(sjw) + '\n')
    f.write('freunden = ' + repr(freunde) + "\n")
    f.close()
    print("Ty for the dox Kappa")


def guess_command_interface():
    print("Welcome to guess the number")
    print("===========================")
    print(" ")
    print("I'm thinking of a number, you have to guess what it is.")
    print("The number is between 0-100 Good luck!")
    print(" ")

    num = passgen.randrange(100)
    guess = ""

    while guess != num:
        guess = int(input("Take a guess: "))
        if guess < num:
            print("Guess higher next time :)\n")
            break
        elif guess > num:
            print("Guess lower next time :P\n")
            break
        elif guess == num:
            print("CONGRATULATIONS!")
            break


def logout_command_interface():
    print("\n" * 100)
    text = colored("Logging out...", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Logging out..", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Logging out.", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Logging out..", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Logging out...", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Logging out..", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Logging out.", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    text = colored("Logged out!", 'red', attrs=['bold'])
    print(text)
    time.sleep(1.5)
    print("\n" * 100)
    psw_interface()
    time_interface()


def exit_command_interface():
    print("\n" * 100)
    text = colored("Shutting down.", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Shutting down..", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Shutting down...", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Shutting down..", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Shutting down.", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Shutting down..", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    print("\n" * 100)
    text = colored("Shutting down...", 'red', attrs=['bold'])
    print(text)
    time.sleep(0.5)
    text = colored("Successfully shutdown!", 'red', attrs=['bold'])
    print(text)
    time.sleep(2)
    exit("Bye!")


load_interface()
psw_interface()
time_interface()
cmdcol = colored('>>>: ', attrs=['bold'])
commands = input(cmdcol)
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
    elif commands == "chpass":
        changepsw_interface()
    elif commands == "help":
        help_command_interface()
    elif commands == "cat":
        cat_command_interface()
    elif commands == "numgen":
        numbergen_command_interface()
    elif commands == "pwdgen" or commands == "passgen" or commands == "password":
        pwdgen_command_interface()
    elif commands == "snow":
        snow_cycle = int(input("Snow cycle: "))
        for i in range(snow_cycle):
            time.sleep(0.4)
            snow_command_interface()
    elif commands == "DatingSim" or commands == "datingsim":
        datingsim_command_interface()
    elif commands == "Guess" or commands == "guess":
        guess_command_interface()
    elif commands == "weather" or commands == "Weather":
        weather_command_interface()
    elif commands == "logout":
        logout_command_interface()
    elif commands == "exit" or commands == "shutdown":
        exit_command_interface()
    else:
        text = colored("Unknown command type", 'red')
        text1 = colored("<help>", 'red', attrs=['bold'])
        text2 = colored("for the available commands", 'red')
        print(text, text1, text2)
        # print("Unknown command type <help> for the available commands")
    cmdcol = colored('>>>: ', attrs=['bold'])
    commands = input(cmdcol)

# We have been working on this for 4 days now and learned so many things, its our first project, hope we can keep going and become
# good devs, I know theres way more and difficulter stuff but we will learn it.
