import random

user_wins = 0
computer_wins = 0
game = 0
games = 1
guesses = 0
guessing_games = 0

print ("Welcome to game %s"%(games))
color = ["green","blue","yellow","red",]

user_choice_to_play = input(" You Want to Play? (yes or no) ")
user_choice_to_play_2 = input(" You Want to Play? (yes or no) ")

user_choice = " what color? "

computer = random.choice(color)

if user_choice_to_play == "yes":
	guessing_games += 1	
	while guesses < 5:
		print ("Welcome to game %s"%(games))
		computer = random.choice(color)
		user_choice = input(" what color ")
		if user_choice == computer:
			print("Correct the computer chose %s"%(computer))
			user_wins += 1
			games += 1
			guesses += 1
			continue				
		elif user_choice != computer:
			print("Incorrect the computer chose %s"%(computer))
			computer_wins += 1
			games += 1
			guesses += 1
			continue
		else:
			print("Pick a Color")	
	else:
		print(f"wins: {user_wins} ... losses: {computer_wins}")
elif user_choice_to_play == "no":
	print(" No! What is wrong with you! ")
	guessing_games += 0
else:
	print(" okay you have to say yes or no ")

print("Again? ")

if user_choice_to_play_2 == "yes":
	guessing_games += 1	
	while guesses < 5:
		print ("Welcome to game %s"%(games))
		computer = random.choice(color)
		user_choice = input(" what color ")
		if user_choice == computer:
			print("Correct the computer chose %s"%(computer))
			user_wins += 1
			games += 1
			guesses += 1
			continue				
		elif user_choice != computer:
			print("Incorrect the computer chose %s"%(computer))
			computer_wins += 1
			games += 1
			guesses += 1
			continue
		else:
			print("Pick a Color")	
	else:
		print(f"wins: {user_wins} ... losses: {computer_wins}")
elif user_choice_to_play == "no":
	print(" No! What is wrong with you! ")
	guessing_games += 0
else:
	print(" okay you have to say yes or no ")

	