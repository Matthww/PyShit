from termcolor import colored, cprint
import string

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
print(chars)
text1 = colored(text="Commands: ", color='red')
print(text1)

print_grey_on_white = lambda x: cprint(x, 'grey', 'on_white')
print_grey_on_white('Hello, World!')

print_whiteblue = lambda x: cprint(x, 'white', 'on_blue')
print_whiteblue('Hello, World!')

print1 = lambda x: cprint(x, 'grey', 'on_green')
print1('Hello, World!')

cmdcol = colored('>>>: ', attrs=['bold'])
print(cmdcol)
sade = input("press key to continue...")