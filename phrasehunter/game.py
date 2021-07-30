"""Module for Game class"""
# Create your Game class logic in here.

"""
class Game
    set TOTAL_LIVES property on class to 5

    define initializer
        set phrases property on instance to list of Phrase instances each with predetermined phrases
        set missed property on instance to 0
        set active_phrase property on instance to None
        set guesses property on instance to an empty list
    end initializer
    
    define method get_random_phrase
        return randomly selected phrase from instance phrases list
    end method
    
    define method welcome
        print "Welcome to Phrase Hunter! Can you guess the phrase before you run out of lives?"
    end method
    
    define method get_guess
        while user guess is not valid
            prompt user for guess
            store result in user_guess
            
            if user_guess is not one character or is not a letter
                print "Sorry, that isn't a valid guess. Guesses must consist of single letters."
                loop so that user can make another guess
            else if user_guess is in instance guesses list
                print "You have already guessed that letter."
                loop so that user can make another guess
            else
                append user_guess to instance guesses list
                return user_guess
            end if
        end while
    end method
    
    define method game_over
        set message
            to "Congratulations, you win!" if result of calling check_complete on instance active_phrase is True
            to "Sorry, you lost..." otherwise
        end set
        
        print message
    end method
    
    define method start
        call welcome method
        
        set instance active_phrase to result of calling get_random_phrase method
        
        while instance missed property is less than class TOTAL_LIVES property
            and result of calling check_complete on instance active_phrase is False
            
            call display method on instance active_phrase
            
            set guess to result of calling get_guess method
            
            if result of calling check_letter on instance active_phrase is False
                increment instance missed by 1
                print "Incorrect. You have {missed} out of {TOTAL_LIVES} remaining."
            end if
        end while
        
        call method game_over
    end method
end class
"""