def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total = 0
    word = ''
    while calculateHandlen(hand) != 0:
        print 'Current Hand: ',
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            break
        elif not isValidWord(word, hand, wordList):
            print 'Invalid word, please try again.'
            continue
        else:
            score = getWordScore(word,n)
            total += score
            hand = updateHand(hand, word)
            print '\"'+str(score)+'\"'+' earned '+ str(word) + ' points. '+'Total: '+ str(total)+' points'
    if word == '.':
        print 'Goodbye! Total score: ' + str(total) + ' points.'
    else:
        print 'Run out of letters. Total score: ' + str(total) + ' points.'
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


#
# Problem #5: Playing a game
# 
