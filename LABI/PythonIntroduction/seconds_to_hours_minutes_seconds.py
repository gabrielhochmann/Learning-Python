# This program converts a given number of seconds into a time format displaying hours, minutes, and seconds.

seconds = int(input("Input the seconds here: "))

hours = seconds // 3600
newsec = seconds % 3600
minutes = newsec // 60
newsec %= 60

print(f"{seconds}s is {hours}h {minutes}min e {newsec}s")
