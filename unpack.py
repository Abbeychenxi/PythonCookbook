import struct

def fields(baseformat, theline, lastfield=False, _cache={ }):
    key = baseformat, len(theline), lastfield
    format = _cache.get(key)
    if format is None:
        numremain = len(theline) - struct.calcsize(baseformat)
        _cache[key] = format = "%s %d%s" % (
            baseformat, numremain, lastfield and "s" or "x")
    return struct.unpack(format, theline)

def split_by(theline, n, lastfield=False):
    #切割所有需要的片段
    pieces = [theline[k: k+n] for k in xrange(0, len(theline), n)]
    if not lastfield and len(pieces[-1]) < n:
        pieces.pop()
    return pieces

def split_at(theline, cuts, lastfield=False):
    #切割所有需要的片段
    pieces = [ theline[i: j] for i j in zip([0]+cuts, cuts+[None]) ]
    if not lastfield:
        pieces.pop()
    return pieces

#生成器版本
def split_at(the_line, cuts, lastfield=False):
    last = 0
    for cut in cuts:
        yield the_line[last: cut]
        last = cut
    if lastfield:
        yield the_line[last: ]

def split_by(the_line, n, lastfield=False):
    return split_at(the_line, xrange(n, len(the_line), n), lastfield)