import asyncio
import string
import random as passgen

from datetime import datetime
startTime = datetime.now()

@asyncio.coroutine
async def slow_operation(loop):
    await asyncio.sleep(0.00001)

    def pswgen():
        #psw_length = int(input("Password length: "))
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 999999
        print("Generated password: ")
        return ''.join(passgen.choice(chars) for x in range(size))

    print(pswgen())


loop = asyncio.get_event_loop()
loop.run_until_complete(slow_operation(loop))
loop.close()
print(datetime.now() - startTime)