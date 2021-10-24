timeSec = int(input('Input time in seconds: '))

hours = timeSec // 3600
minutes = timeSec // 60 - hours * 60
seconds = timeSec % 60
print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))