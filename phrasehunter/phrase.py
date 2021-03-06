"""Module for Phrase class"""


class Phrase:
    """Phrase to be guessed by a player."""

    def __init__(self, phrase: str):
        self.phrase = phrase.lower()
        self.correct_guesses = []

    def __str__(self):
        split_string = list(self.phrase)

        for index, char in enumerate(split_string):
            # Hide each letter that has yet to be guessed
            if char != " " and char not in self.correct_guesses:
                split_string[index] = "_"

        rejoined_string = " ".join(split_string)

        return rejoined_string

    def display(self):
        """
        Display the current status of the phrase, only showing the
        letters of the phrase that have been guessed.
        """
        print(self)

    def check_letter(self, letter: str) -> bool:
        """
        Determine whether the provided letter is in this phrase.

        :param letter: The letter the user is guessing
        :return: Whether the letter is in the phrase
        """
        normalized_letter = letter.lower()
        is_correct = normalized_letter in self.phrase

        if is_correct:
            self.correct_guesses.append(normalized_letter)

        return is_correct

    def check_complete(self) -> bool:
        """
        Check whether all characters in this phrase have been
        guessed by the player.

        :return: Whether the phrase has been completed.
        """
        phrase_letters = set([char for char in self.phrase if char != " "])
        guesses_set = set(self.correct_guesses)

        return phrase_letters == guesses_set

    def reveal_complete_phrase(self):
        """Reveal all unguessed letters in the phrase"""

        if not self.check_complete():
            phrase_letters = set(
                [char for char in self.phrase if char != " "
                 and char not in self.correct_guesses
                 ]
            )

            for letter in phrase_letters:
                self.check_letter(letter)
