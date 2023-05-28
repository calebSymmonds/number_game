from art import logo
import random

def number_game():
  print("Welcome to the number game! Try and guess my number.")
  mode = input("Which mode would you prefer? easy (10 guesses) or hard (5 guesses)").lower()
  while mode != "easy" and mode != "hard":
    input("Invalid input. Please type easy or hard.")
  guesses = 0
  number = random.randint(1, 100)
  if mode == "easy":
    guesses = 10
    choice = int(input("OK. Pick a number between 1 and 100."))
  elif mode == "hard":
    guesses = 5
    choice = int(input("OK. Pick a number between 1 and 100."))
  if choice == number:
    win = input("You got it! Play again?")
    while win != "yes" and mode != "no":
      input("Invalid input. Please type yes or no.")
    if win == "yes":
      number_game()
    if win == "no":
      return
