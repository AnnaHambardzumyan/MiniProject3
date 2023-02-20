import time

print("Insert time to count down (h:m:s) ")
str = input()
h, m, s = list(map(int, str.split(':')))
total_secs = h * 3600 + m * 60 + s
while total_secs >= 0:
	sec = total_secs % 60
	min = (total_secs % 3600) // 60
	hour = total_secs // 3600
	print("{:02d}:{:02d}:{:02d}".format(hour, min, sec))
	time.sleep(1)
	total_secs -= 1
