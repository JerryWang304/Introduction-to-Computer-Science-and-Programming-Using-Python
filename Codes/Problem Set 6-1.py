
import string
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    ret = {}
    for i in range(len(lower)):
        ret[lower[i]] = lower[(i+shift)%26]
    for i in range(len(upper)):
        ret[upper[i]] = upper[(i+shift)%26]
    return ret
print buildCoder(3)