import string
#def buildCoder(shift):
#    """
#    Returns a dict that can apply a Caesar cipher to a letter.
#    The cipher is defined by the shift value. Ignores non-letter characters
#    like punctuation, numbers, and spaces.
#
#    shift: 0 <= int < 26
#    returns: dict
#    """
#    ### TODO 
#    lower = string.ascii_lowercase
#    upper = string.ascii_uppercase
#    ret = {}
#    for i in range(len(lower)):
#        ret[lower[i]] = lower[(i+shift)%26]
#    for i in range(len(upper)):
#        ret[upper[i]] = upper[(i+shift)%26]
#    return ret
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    function  = coder
    ans = ""
    for char in text:
        if char in string.ascii_letters: 
            ans += function[char]
        else:
            ans += char
    return ans
#print applyCoder("Hello, world!",buildCoder(3))