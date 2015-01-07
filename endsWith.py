import itertools

def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)

def endsWith(s, *endings):
    return anyTrue(s.endswith, endings)

if __name__ == '__main__':
    import os
    for filename in os.listdir('.'):
        if endsWith(filename, '.jpg', '.jpeg', '.gif'):
            print filename