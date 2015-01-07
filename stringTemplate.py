import string

new_style = string.Template('this is $thing')
print new_style.substitute({'thing': 5})
print new_style.substitute(thing='test')


#python 2.3
def expand(format, d, marker='"', safe=False):
    if safe:
        def lookup(w): return d.get(w, w.join(marker*2))
    else:
        def lookup(w): return d[w]
    parts = format.split(marker)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

if __name__ == '__main__':
    print expand('just "a" test', {'a': 'one'})