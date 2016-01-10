def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char in lettersGuessed:
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ret = ''
    for char in secretWord:
        if char in lettersGuessed:
            ret = ret + char
        else:
            ret = ret + '_'
    return ret

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allStr = string.ascii_lowercase
    ret = ''
    for char in allStr:
        if char not in lettersGuessed:
            ret = ret + char
    return ret
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = [] # The letters player has guessed
    mistakesMade = 0
    availableLetters = ''
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    guessedWord =  getGuessedWord(secretWord,lettersGuessed)
    print '-------------'
    while mistakesMade < 8 and guessedWord != secretWord:    
        print 'You have ' + str(8-mistakesMade) + ' guesses left'
        availableLetters = getAvailableLetters(lettersGuessed)
        print 'Available Letters: ' + availableLetters       
        answer = raw_input('Please guess a letter: ')
        if answer in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter: ' + guessedWord
        elif answer not in secretWord:
            lettersGuessed.insert(len(lettersGuessed),answer)
            mistakesMade += 1
            print 'Oops! That letter is not in my word: ' + guessedWord
        elif answer in secretWord:
            lettersGuessed.insert(len(lettersGuessed),answer)
            guessedWord = getGuessedWord(secretWord,lettersGuessed)
            print 'Good guess:' + guessedWord
        print '-------------'    
    if mistakesMade >= 8:
        print 'Sorry, you ran out of guesses. The word was else.'
    else:
        print 'Congratulations, you won!'

    
hangman('abcd')
    
    
    
    
    
    
    
    