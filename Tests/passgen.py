import string
import random as passgen

from datetime import datetime
startTime = datetime.now()

def pswgen():
    #psw_length = int(input("Password length: "))
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 999999
    print("Generated password: ")
    return ''.join(passgen.choice(chars) for x in range(size))


print(pswgen())
print(datetime.now() - startTime)