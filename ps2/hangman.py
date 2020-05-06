# Problem Set 2, hangman.py
# Name: Kevin DeAngeles
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
      if char in letters_guessed:
        continue
      else:
        return False
    
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    current_guess = []
    
    for char in secret_word:
      if char in letters_guessed:
          current_guess.append(char)
      else:
        current_guess.append("_ ")
    
    return (''.join(current_guess))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string

    letters_not_guessed = []
    ### Create list of all lowercase letters in English alphabet
    lowercase_letters = string.ascii_lowercase

    for letter in lowercase_letters:
      if letter not in letters_guessed:
        letters_not_guessed.append(letter)
    
    return (''.join(letters_not_guessed))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    ### Initialize Variables
    secret_word_length = len(secret_word)
    guesses_left = 6
    letters_guessed = []
    warnings = 3

    ### Print welcome statement and give secret word length
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(secret_word_length) + " letters long.\n-------------")

    ### Start game loop
    while True:

      ### End the game if they are out of guesses
      if guesses_left == 0:
        print("Sorry, you ran out of guesses.  The word was " + secret_word)
        exit()

      ### Print number of warnings and guesses left
      print("You have " + str(warnings) + " warnings left.")
      print("You have " + str(guesses_left) + " guesses left.")

      ### Print letters that have not yet been guessed
      letters_not_guessed = get_available_letters(letters_guessed)
      print("Available letters: " + letters_not_guessed)

      ### Prompt for guess and convert to lower
      guess = input("Please guess a letter: ").lower()

      ### If guess is not alphabetical
      if not str.isalpha(guess):

        ### If they still have warnings left, decrement warnings.  Otherwise, decrement turns (they lose a guess)
        if warnings <= 0:
          guesses_left -= 1
        else:
          warnings -= 1

        guessed_word = get_guessed_word(secret_word, letters_guessed)
        print("Oops!  That letter is not a valid letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
        print("-------------")

        continue
      
      ### If the letter was already guessed
      elif guess in letters_guessed:
        
        ### If they still have warnings left, decrement warnings.  Otherwise, decrement turns (they lose a guess)
        if warnings <= 0:
          guesses_left -= 1
        else:
          warnings -= 1

        guessed_word = get_guessed_word(secret_word, letters_guessed)
        print("Oops!  You have already guessed that letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
        print("-------------")

        continue

      else:

        ### Append guess to list of guessed letters
        letters_guessed.append(guess)

        ### Check if the guessed letter is in the secret word and display guessed word
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if guess in secret_word:
          print ("Good guess: " + guessed_word)

          ### Check to see if they have guessed the word
          if is_word_guessed(secret_word, letters_guessed):
            print("-------------\nCongratulations, you won!")

            total_score = guesses_left * secret_word_length
            print("Your total score for this game is: " + str(total_score))

            exit()

        else:
          print("Oops!  That letter is not in any word: " + guessed_word)
          
          ### Determine if vowel
          if guess in ('a','e','i','o','u'):
            ### Increment turns by 2 if they wrongly guessed a vowel
            guesses_left -= 2
          else:
            ### Increment turns by 1 only if they wrongly guessed a consonant
            guesses_left -= 1

      print("-------------")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    position_counter = 0

    for letter in my_word:

        if (letter == other_word[position_counter]) or (letter == "_"):
                position_counter += 1
        else:
            return False
    
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.replace(' ', '')
    my_word_length = len(my_word)
    same_length_words = []
    possible_matches = []

    for word in wordlist:
      if len(word) == my_word_length:
        same_length_words.append(word)
    
    for word in same_length_words:
      if match_with_gaps(my_word, word):
        possible_matches.append(word)
    
    if len(possible_matches) == 0:
      return "No matches found"
    else:
      return (' '.join(possible_matches))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    ### Initialize Variables
    secret_word_length = len(secret_word)
    guesses_left = 6
    letters_guessed = []
    warnings = 3

    ### Print welcome statement and give secret word length
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(secret_word_length) + " letters long.\n-------------")

    ### Start game loop
    while True:

      ### End the game if they are out of guesses
      if guesses_left == 0:
        print("Sorry, you ran out of guesses.  The word was " + secret_word)
        exit()

      ### Print number of warnings and guesses left
      print("You have " + str(warnings) + " warnings left.")
      print("You have " + str(guesses_left) + " guesses left.")

      ### Print letters that have not yet been guessed
      letters_not_guessed = get_available_letters(letters_guessed)
      print("Available letters: " + letters_not_guessed)

      ### Prompt for guess and convert to lower
      guess = input("Please guess a letter: ").lower()

      ### Hint funcionality
      if guess == "*":

        guessed_word = get_guessed_word(secret_word, letters_guessed)
        possible_matches = show_possible_matches(guessed_word)

        print("Possible matches are: " + possible_matches)

      ### If guess is not alphabetical
      elif not str.isalpha(guess):

        ### If they still have warnings left, decrement warnings.  Otherwise, decrement turns (they lose a guess)
        if warnings <= 0:
          guesses_left -= 1
        else:
          warnings -= 1

        guessed_word = get_guessed_word(secret_word, letters_guessed)
        print("Oops!  That letter is not a valid letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
        print("-------------")

        continue
      
      ### If the letter was already guessed
      elif guess in letters_guessed:
        
        ### If they still have warnings left, decrement warnings.  Otherwise, decrement turns (they lose a guess)
        if warnings <= 0:
          guesses_left -= 1
        else:
          warnings -= 1

        guessed_word = get_guessed_word(secret_word, letters_guessed)
        print("Oops!  You have already guessed that letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
        print("-------------")

        continue

      else:

        ### Append guess to list of guessed letters
        letters_guessed.append(guess)

        ### Check if the guessed letter is in the secret word and display guessed word
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if guess in secret_word:
          print ("Good guess: " + guessed_word)

          ### Check to see if they have guessed the word
          if is_word_guessed(secret_word, letters_guessed):
            print("-------------\nCongratulations, you won!")

            total_score = guesses_left * secret_word_length
            print("Your total score for this game is: " + str(total_score))

            exit()

        else:
          print("Oops!  That letter is not in any word: " + guessed_word)
          
          ### Determine if vowel
          if guess in ('a','e','i','o','u'):
            ### Increment turns by 2 if they wrongly guessed a vowel
            guesses_left -= 2
          else:
            ### Increment turns by 1 only if they wrongly guessed a consonant
            guesses_left -= 1

      print("-------------")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
