'''
    Hanna Motande-Nizet
    Dec 3rd 2021
    Project: Number of Guesses
'''

# This module makes random numbers
import random 
class Guess():
	def __init__(self, guess, name, number_guesses):
		self.guess = guess  # The user's guess
		self.name = name    # The user's name
		self.number_guesses = number_guesses    # The number of guesses taken
		
	def entry(self):		
		self.number = random.randint(0, 100)    # The number the computer chooses between 0 and 100
		while(self.number_guesses < 7):     # While loop repeats a block of code as long as a certain condition is true. The number of guesses taken is less than 7 
			self.number_guesses = self.number_guesses + 1      # The total of number of guesses is 8
			guesses_left = 8 - self.number_guesses      # Everytime the user guess a number, it subtract from the total number and display the number of guesses left 
				
			if self.guess < self.number:        # If the user's guess is less than the random number
				guesses_left = str(guesses_left)    # Create the number of guesses left to a string
				print("Your guess is too low! You have {} guesses left".format(guesses_left))   # Prints out a message that the user's number is too low and the number of guesses left
				self.guess = int(input("\nTake a guess: "))     # Take another guess till the user gets it right

			elif self.guess > self.number:      # If the user's guess is greater than the random number
				guesses_left = str(guesses_left)    # Create the number of guesses left to a string
				print("Your guess is too high! You have {} guesses left".format(guesses_left))  # Prints out a message that the user's number is too high and the number of guesses left
				self.guess = int(input("\nTake a guess: "))    # Take another guess till the user gets it right

			else:
				self.guess == self.number       # The user's guess is equal to the random number 
				self.number_guesses == str(self.number_guesses)     # Create the number of guesses taken to a string
				print("\nGood job! You guessed the number in {} tries :)".format(self.number_guesses))      # Prints out a message that the user's number is correct to the number the computer has pick in number of tries
		if self.guess != self.number:       # The user's guess is not equal to the random number 
			self.number = str(self.number)      # Create the number the computer has picked to a string
			print("\nSorry. The number I was thinking of was {} :P".format(self.number))        # Prints out a message that the user's number is not correct to the number the computer has pick and print the computer's number 


# Welcome the player by name	
# And tells them that the computer is thinking of a random number, take a guess			
if __name__ == "__main__":
	name = input("Hello! What is your name? ")
	print("{}, I am thinking of a whole number between 0 and 100. Can you guess what it is?".format(name))
	guess = int(input("\nTake a guess: "))
	new_game = Guess(guess, name, 0)	
	new_game.entry()
