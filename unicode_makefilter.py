class Keeper(object):
    def __init__(self, keep):
        self.keep = set(map(ord, keep))

    def __getitem__(self, n):
        if n not in self.keep:
            return None
        return unichr(n)

    def __call__(self, s):
        return unicode(s).translate(self)

makefilter = Keeper

if __name__ == '__main__':
    m = makefilter('aeiou')
    print m(u'dasdsaigok')