from art import logo
import random

def number_game():
  print(logo)
  print("Welcome to the number game! Try and guess my number.")
  mode = input("Which mode would you prefer? easy (10 guesses) or hard (5 guesses)\n").lower()
  while mode != "easy" and mode != "hard":
    mode = input("Invalid input. Please type easy or hard.\n")
  number = random.randint(1, 100)
  if mode == "easy":
    guesses = 9
    choice = int(input("OK. Pick a number between 1 and 100.\n"))
  elif mode == "hard":
    guesses = 4
    choice = int(input("OK. Pick a number between 1 and 100.\n"))
  while choice != number and guesses > 0:
    guesses -= 1
    if choice < number:
      choice = int(input(f"{choice} is too low. Try a higher number.\n"))
    if choice > number:
      choice = int(input(f"{choice} is too high. Try a lower number.\n"))
  if guesses == 0:
    new_game = input(f"All out of guesses! My number was {number}. Play again?\n")
    while new_game != "yes" and new_game != "no":
      new_game = input("Invalid input. Please type yes or no.\n")
    if new_game == "yes":
      number_game()
    if new_game == "no":
      return
  if choice == number:
    win = input("You got it! Play again?\n")
    while win != "yes" and win != "no":
      win = input("Invalid input. Please type yes or no.\n")
    if win == "yes":
      number_game()
    if win == "no":
      return

number_game()
