import time, calendar

seconds = time.time()

minutes = seconds/60

hours = minutes // 60

remainder = minutes - hours * 60

print(str(hours) + ":" + str(remainder))

print(time.gmtime())
print(time.localtime())
print(calendar.timegm(time.localtime()))

