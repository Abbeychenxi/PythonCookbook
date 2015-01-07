import re

class make_xlat:
    def __init__(self, *args, **kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()

    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))

    def one_xlat(self, match):
        return self.adict[match.group(0)]

    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

class make_xlat_by_whole_words(make_xlat):
    def make_rx(self):
        return re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, self.adict)))
