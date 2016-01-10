def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word not in wordList:
        return False
 
    list_word = {}
    for char in word:
        if char not in list_word.keys():
            list_word[char] = 1
        else:
            list_word[char] += 1   
            
    for key in list_word.keys():
        if key not in hand.keys() or list_word[key] > hand[key]:
            return False   
    return True
          