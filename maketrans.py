import string

notrans = string.maketrans('', '')

def containsAny(astr, strset):
    return len(strset) != len(strset.translate(notrans, astr))

def containsAll(astr, strset):
    return not strset.translate(notrans, astr)
