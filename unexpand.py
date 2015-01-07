def unexpand(astring, tablen=8):
    import re
    #切分空格和非空格的序列
    pieces = re.split(r'( +)', astring.expandtabs(tablen))
    #记录目前的字符串总长度
    lensofar = 0
    for i, piece in enumerate(pieces):
        thislen = len(piece)
        lensofar += thislen
        if piece.isspace():
            #将各个空格序列改成tabs+spaces
            numblanks = lensofar % tablen
            numtabs = (thislen-numblanks+tablen-1)/tablen
            pieces[i] = '\t'*numtabs + ' '*numblanks
    return ''.join(pieces)