import string

notrans = string.maketrans('', '')
def containsAny(str, strset):
    return len(strset) != len(strset.translate(notrans, str))

def iscapitalized(s):
    return s == s.capitalize() and containsAny(s, string.letters)

if __name__ == '__main__':
    print iscapitalized('abc')