def containsAll(seq, aset):
    for c in seq:
        if c not in aset:
            return False
    return True
