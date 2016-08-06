import time
import webbrowser
import random

print "When do you want to wake up?"
print "Use format HH:MM:SS "
Alarm =raw_input("> ")

Time=time.strftime("%H:%M:%S")

with open("Youtube.txt") as f:

	content=f.readlines()


while Time != Alarm:
	print "Time is" + Time
	Time = time.strftime("%H:%M:%S")
	time.sleep(1)

if Time == Alarm:
	print "Time to wake up!"
	random_vid = random.choice(content)
	webbrowser.open(random_vid)


