#coding: utf-8
class iStr(str):
    """
    大小写不敏感的字符串类
    行为方式类似于str，只是所有的比较和查询
    都是大小写不敏感的
    """

    def __init__(self, *args):
        self._lowered = str.lower(self)
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))
    def __hash__(self):
        return hash(self._lowered)
    def lower(self):
        return self._lowered

def _make_case_insensitive(name):
    '''将str的方法封装成istr的方法，大小写不敏感'''
    str_meth = getattr(str, name)
    def x(self, other, *args):
        '''
        先尝试将other小写化，通常这应该是一个字符串，
        但必须要做好准备应对这个过程中出现的错误，
        因为字符串是可以和非字符串正确地比较的
        '''
        try:
            other = other.lower()
        except (TypeError, AttributeError, ValueError):
            pass
        return str_meth(self._lowered, other, *args)
        #x.func_name = name
    setattr(iStr, name, x)
for name in 'eq lt le gt gt ne contains'.split():
    _make_case_insensitive('__%s__' % name)
for name in 'count endswith find index rfind rindex startswith'.split():
    _make_case_insensitive(name)
del _make_case_insensitive

def _make_return_iStr(name):
    str_meth = getattr(str, name)
    def x(*args):
        return iStr(str_meth(*args))
    setattr(iStr, name, x)
for name in 'center ljust rjust strip lstrip rstrip'.split():
    _make_return_iStr


class iList(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self[:] = self
    wrap_each_item = iStr
    def __setitem__(self, i, v):
        if isinstance(i, slice): 
            v = map(self.wrap_each_item, v)
        else:
            v = self.wrap_each_item(v)
        list.__setitem__(self, i, v)
    def append(self, item):
        list.append(self, slef.wrap_each_item(item))
    def extend(self, seq):
        list.extend(self, map(self.wrap_each_item, seq))