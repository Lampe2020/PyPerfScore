import time as t

def counter(runs_max = 100000):
	runs_passed = 0
	global number
	number = 0

	while runs_passed <= runs_max:
		if runs_passed < runs_max:
			print(number, end="\r")
			number +=1
			runs_passed += 1
		elif runs_passed == runs_max:
			print(number)
			exit()

def pts_down():
	global sec
	sec = 0
	while True:
		t.sleep(0.25)
		number = number - 10000
		sec += 1
		print(number, "score after", sec, "seconds...")

with counter():
	pts_down()
