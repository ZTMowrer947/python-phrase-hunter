"""Module for Phrase class"""
# Create your Phrase class logic here.

"""
class Phrase
    define initializer
        with arg phrase of type string
        
        set phrase property on instance to lowercased phrase
        set correct_guesses property to empty list
    end initializer
    
    define method display
        with arg correct_guesses of type list
        set split_string to instance phrase converted to list
        
        for each index and char in enumerating split_string
            if char is not in guesses
                set char at index to "_"
            end if
        end for
        
        set rejoined_string to split_string rejoined by ""
        print rejoined_string
    end method
    
    define method check_letter
        with arg letter of type string
        
        set is_correct to result of checking if letter is in instance phrase
        
        if is_correct
            append letter to instance correct_guesses list
        end if
        
        return is_correct
    end method
    
    define method check_complete
        with arg guesses of type list
        
        set letters to instance phrase converted to set
        set guesses_set to guesses converted to set
        
        return result of checking if letters is a subset of guesses_set
    end method    
end class
"""