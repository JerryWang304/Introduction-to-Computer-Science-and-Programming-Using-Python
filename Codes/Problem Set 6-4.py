def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    ans = 0
    words = text.split(' ')
    flag = False
    MAX = 0
    for i in range(26):
        flag = True
        total = 0
        for word in words:
            if isWord(wordList,applyShift(word,i)):#isWord is provided by edX
                total += 1
                
        if total > MAX:
            ans = i
            MAX = total
    return ans