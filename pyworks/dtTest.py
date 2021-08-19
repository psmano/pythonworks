import datetime

currentDT = datetime.datetime.now()

print("Current Year: %d" % currentDT.year)
print("Current Month: %d" % currentDT.month)
print("Current Day: %d" % currentDT.day)
print("Current Hour: %d" % currentDT.hour)
print("Current Min: %d" % currentDT.minute)
print("Current Sec: %d " % currentDT.second)
print("Current Micro Sec: %d " % currentDT.microsecond)

#print("IPv4 %d %d %d %d %d %d %d.csv" %currentDT.year %currentDT.month %currentDT.day %currentDT.hour %currentDT.minute %currentDT.second %currentDT.microsecond)
print ('IPv4' + str(currentDT.strftime("%Y%m%d%H%M%S")))

