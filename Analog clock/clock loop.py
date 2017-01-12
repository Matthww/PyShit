import time
from datetime import datetime

t = datetime.now()
i = False

while not i:
    print("Time = %s:%s:%s" % (t.hour, t.minute, t.second))
    time.sleep(1)
    i = False