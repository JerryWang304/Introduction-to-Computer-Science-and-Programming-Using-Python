def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    word = ''
    total = 0
    while word != None:
        print 'Current Hand: ',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word == None:
            continue
        score = getWordScore(word,n)
        total += score
        hand = updateHand(hand, word)
        print '\"'+word+'\"'+' earned '+ str(score) + ' points. '+'Total: '+ str(total)+' points'        
    print 'Total socre: '+str(total)+' points.'  