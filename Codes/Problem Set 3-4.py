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

print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])