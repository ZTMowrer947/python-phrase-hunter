"""Module for Game class"""
import random

from phrasehunter.phrase import Phrase


class Game:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    TOTAL_LIVES = 5

    def __init__(self):
        self.phrases = [
            Phrase('friendship is magic'),
            Phrase('all your base are belong to us'),
            Phrase('what is a man a miserable little pile of secrets'),
            Phrase('seize the day'),
            Phrase('the cat in the hat')
        ]
        self.missed = 0
        self.active_phrase: Phrase = None  # Will be initialized in start()
        self.guesses = []

    def get_random_phrase(self) -> Phrase:
        return random.choice(self.phrases)

    def welcome(self):
        """Print a welcome message for the user"""
        print("Welcome to Phrase Hunter!")
        print("Can you guess the phrase before you run out of lives?\n")

    def get_guess(self) -> str:
        """
        Repeatedly prompt the user to guess a letter until a valid
        guess is received

        :return: The user's guess
        """
        while True:
            user_guess = input('Guess a letter: ').lower()

            if len(user_guess) != 1 or user_guess not in Game.ALPHABET:
                print("Sorry, that isn't a valid guess.")
                print("Guesses must consist of single letters.\n")
            elif user_guess in self.guesses:
                print("You have already guessed that letter.\n")
            else:
                self.guesses.append(user_guess)
                return user_guess

    def game_over(self):
        """Print the result of the game along with what the phrase was"""

        if self.active_phrase.check_complete():
            message = "Congratulations, you win!\n"
        else:
            message = "Sorry, you lost...\n"
            self.active_phrase.reveal_complete_phrase()

        print(message)
        print('The phrase was:')
        self.active_phrase.display()

    def start(self):
        """Begin the game"""

        self.welcome()

        self.active_phrase = self.get_random_phrase()

        # Loop while player has neither lost nor won
        while (self.missed < Game.TOTAL_LIVES and
                not self.active_phrase.check_complete()):
            self.active_phrase.display()

            guess = self.get_guess()

            is_correct = self.active_phrase.check_letter(guess)
            if not is_correct:
                self.missed += 1
                remaining_guesses = Game.TOTAL_LIVES - self.missed
                print(f'Incorrect. You have {remaining_guesses} guesses left.')

            print()

        self.game_over()

