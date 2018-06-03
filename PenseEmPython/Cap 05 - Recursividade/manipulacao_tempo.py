minutes = 1470
print(minutes / 60)

hours = minutes // 60
print(hours)

remainder = minutes - hours * 60
print(remainder)

print(str(hours) + ":" + str(remainder))