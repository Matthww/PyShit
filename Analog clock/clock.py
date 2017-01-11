from datetime import datetime

time = datetime.now()

print('Year = %s' % time.year)
print('Month = %s' % time.month)
print('Day = %s' % time.day)
print('Hour = %s' % time.hour)
print('Minutes = %s' % time.minute)
print('Microsecond = %s' % time.microsecond)

print("Time = %s:%s:%s" % (time.hour, time.minute, time.second))
print("Date =  %s/%s/%s" % (time.day, time.month, time.year))
