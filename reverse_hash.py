def hash(s):
    """
    This function takes string as an argument and converts it into 
    hash number using the characters in the letters variable.
    """
    h = 7
    letters = "acdegilmnoprstuw"
    for char in s:
        h = (h * 37 + letters.index(char) )
    return h


def reverse_hash(num):
    """
    This function is reverse of the above function (hash), 
    takes integer as an argument and converts it into string.
    """
    h = 7
    letters = "acdegilmnoprstuw"
    s = ''
    while num > h:
        pos = num % 37
        s += letters[pos]
        num = num / 37
    return s[::-1]


if __name__ == "__main__":
    print 'Hash: ', hash("leepadg")
    print 'Reverse Hash: ', reverse_hash(680131659347)
