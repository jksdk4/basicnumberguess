# 10 Jun 19
# free education bruh
# based on Invent With Python's num guess game, but I added a few things
# refactored this a bit, 10 Jul 19

import random

def guess_increment(guesses, max_guesses, num_guesses, actual_num):
	"""Provides feedback on number entered, increments guess count"""
	variable = ''
	num_guesses += 1
	if guesses == actual_num:
		return num_guesses
	elif guesses > actual_num:
		variable = 'high'
	elif guesses < actual_num:
		variable = 'low'
	print(f"\nToo {variable}.")
	return num_guesses
	
actual_num = random.randint(1,101)
max_guess = 6
num_guess = 0
guessed_nums = []

player = input("Hi. What's your name?\n")
print(f"\n{player.title()}, guess a number between 1 and 100.")
print(f"You currently have {str(max_guess)} tries. Hit 'q' to quit.")

guess = input("\nEnter a number: ")

while guess != 'q':
	try:	
		guess = int(guess)
	except ValueError:		# input is not an integer, does not increment counter
		print("\nInvalid input. Try again.")
		print(f"You still have {str(max_guess - num_guess)} guesses left.")
		guess = input("\nEnter a number: ")
	else:
		if guess not in guessed_nums:		# checks for repeated guesses
			guessed_nums.append(guess)
		else:
			print("You already guessed this number. Try again.")
			print(f"You still have {str(max_guess - num_guess)} guesses left.")
			guess = input("\nEnter a number: ")
			continue		# restarts try/except w/o running rest of program

		# counter increments here if prev conditions not met
		num_guess = guess_increment(guess,max_guess,num_guess,actual_num)

		# if user guesses equals max guesses and still isn't right, break out
		# RHS bool prevents game from giving one extra guess 
		#   and then breaking here regardless of accuracy
		if num_guess == max_guess and guess != actual_num:
			print(f"\nOut of guesses. The number was {str(actual_num)}.")
			break
		elif guess == actual_num:
			if num_guess == 1:		# guessed right on the first try
				print(f"\nDamn are you a robot? {player.title()}, you got it right in {str(num_guess)} try.")
				break
			else:
				print(f"\n{player.title()}, you got it right in {str(num_guess)} tries.")
				break
		else:		# nothing above applies and game is still going, do this
			print(f"Guesses left: {str(max_guess - num_guess)}")
			guess = input("\nEnter a number: ")