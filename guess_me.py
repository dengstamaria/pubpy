"""
	Guess the Number

	The system randomly selects a number between 1 and 6. The user has to guess what that number is. The code will tell you if you got the number correctly. 

	If you get an error, the code will tell you if you are too high or too low.
 """
import os
import random
x = [1, 2, 3, 4, 5, 6]
upoint = 0
mpoint = 0
os.system('cls')  # clear screen on windows
#os.system('clear')  # clear screen on linux
raw_input("Do you want to play with monty?" "\n" "monty is thinking of a number between 1 and 6" "\n" "press enter to continue...")
while True:
	os.system('cls')  # on windows
	#os.system('clear')  # on linux / os x
	num = random.sample(x,1)
	nint = int(num[0])
	inp = raw_input('What is your guess? please enter a number between 1 and 6' '\n' '(press "q" to quit)--->')
	if inp == 'q':
		break
	try:
		iint = int(inp)
		if iint == nint:
			print "\n", "monty says the number is: " , nint , "\n","...fine...you are correct!" ,"\n", "you can have 1 point!"
			upoint = upoint + 1
		elif iint < 1 or iint > 6:
			print "\n","you silly user! your entry should be a number between 1 and 6"
		else:
			print "\n", "Boo! you got it wrong! the correct nmber is: " , nint
			mpoint = mpoint + 1
	except:
		print "please enter a number between 1 and 6"
	print "\n" ,"you: ", upoint , "monty: " , mpoint
	raw_input("\n" "press return to continue...")
	
	