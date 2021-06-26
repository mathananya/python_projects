#importing random commands
import random

#creating movie_list, selecting movie, creating empty letter_list, creating answer_list
movie_list = ["frozen", "spiderman", "incredibles", "coco", "moana", "zootopia", "brave", "rango", "tangled", "pinocchio"]
movie = random.choice(movie_list)
letter_list = []
answer_list = []

#adding movie's letters to letter_list
for letter_num in range(len(movie)):
	letter_list.append(movie[letter_num])

#adding dashes to answer_list
for dashes in range(len(movie)):
	answer_list.append("_")

#Introduction
print ("")
print "Welcome to the hangman game"
print "You have to guess the letters of the animated movie by the number of dashes given to you. You have 7 lives; and you will lose one with every wrong guess."

#lives and game status(running or over)
lives = 7
game = 1

#the actual game(...finally!)
print answer_list
print ""
while lives > 0 and game == 1:
	user_letter = raw_input("Enter a letter: ")
	if len(user_letter) > 1:
		print "Only 1 letter please!"
		continue
	else:
		correct = 0
		for letter_check in range(len(movie)):
			if user_letter == movie[letter_check]:
				answer_list[letter_check] = user_letter
				correct = 1
		if correct == 0:
			print "Oops!"
			print answer_list
			lives = lives-1
			print "Lives:", lives
			print ""
		else:
			print "Great Job!"
			print answer_list
			print "Lives:", lives
			print ""
		if "_" not in answer_list:
			game = 0
			
#deciding if game won or lost
if lives > 0:
	print "Congratulations!!!"
	print "You guessed the movie",movie,"with",lives,"of your lives remaining!"
	print ""
if lives == 0:
	print "Oopsy daisy!"
	print "The man is hanged! The movie was", movie,"."	
	print ""
			
			
			
			
			
			
			
			
			
			
			
			
				
