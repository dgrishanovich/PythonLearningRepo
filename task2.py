import datetime

timeSec = int(input('Input time in seconds: '))
t = str(datetime.timedelta(seconds=timeSec))
print(t)

#hours = timeSec // 3600
#minutes = timeSec // 60 - hours * 60
#seconds = timeSec % 60
#print('Time is: ' + str(hours) + ':' + str(minutes) + ':' + str(seconds))