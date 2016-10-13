"""
	Dice Rolling Simulator
	it will randomly choose a number between 1 and 6	
 """
import random
x = [1, 2, 3, 4, 5, 6]
while True:
	inp = raw_input('Do you want to roll the die? y/n:  ')
	if inp == "y":
		die = random.sample(x,1)
		print die
	elif inp == "n":
		break
print "Thank you for playing!"	


