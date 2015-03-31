#!/usr/bin/python
# William Thing
# November 29, 2015
# Guessing Game
#
# This program allows a user to play Guessing Game.
# The user will input guesses to the console to try
# to get the correct answer between 1-100.
# Can play multiple games and will print overall
# results.

from random import randrange

# Introduction to the Guess Game
def game_intro():
   print("This program allows you to play a guessing game.");
   print("I will think of a number between 1 and");
   print("100 and will allow you to guess until");
   print("you get it.  For each guess, I will tell you");
   print("whether the right answer is higher or lower");
   print("than your guess.");

# Plays one game of the Guessing game and returns the amount of guesses
# the player took to win.
def guessing_game():
   answer = randrange(1, 100);  # randrange operates faster than randint
   guess = int(raw_input("Your guess? "));
   guess_count = 1;
   while guess != answer:
      guess = int(raw_input("Your guess? "));
      guess_count += 1;
   return guess_count;
   
def main():
   game_intro();
   # Counters
   total_games = 0;
   total_guesses = 0;
   best_game = 0;
   least_guessed = 101;
   continue_playing = "y";
   while continue_playing.startswith("y", 0, len(continue_playing)):
      guess_counter = guessing_game();
      # end of game phase
      total_games += 1;                   # increments total games
      total_guesses += guess_counter;     # increments guesses per game
      if guess_counter < least_guessed:   # checks for best game
         least_guessed = guess_counter;
         best_game = total_games;
      continue_playing = raw_input("Do you want to play again? ").lower();
   guesses_per_game = float(total_guesses)/total_games;
   # Display Information
   print("Overall results:");
   print("     total games   = %d" % total_games);
   print("     total guesses = %d" % total_guesses);
   print("     guesses/game  = %.1f" % guesses_per_game);
   print("     best game     = %d" % best_game);
   
if __name__ == "__main__": main();