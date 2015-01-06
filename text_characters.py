from __future__ import division
import string

text_characters = ''.join(map(chr, range(32, 127))) + "\n\r\t\b"
_null_trans = string.maketrans('', '')

def istext(s, text_characters=text_characters, threshold=0.30):
    if "\0" in s:
        return False
    if not s:
        return True
    #获得s的由非文本字符构成的字符串
    t = s.translate(_null_trans, text_characters)
    #如果超过30%的字符是非文本字符，s是字符串
    return len(t)/len(s) <= threshold