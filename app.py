"""Main application"""
from phrasehunter.game import Game

if __name__ == '__main__':
    should_keep_playing = True

    while should_keep_playing:
        # Initialize a new game every time
        game = Game()

        game.start()

        # Continue playing games until user explicitly opts to stop
        should_keep_playing = input("\nPlay again? (Y/n) ").lower() != "n"
        print()
    else:
        print("Thanks for playing.")
