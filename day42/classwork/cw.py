#N1kata
def unique_sum(lst):
    if lst:
        return sum(set(lst))
#N2kata
def doubles(s):
    cs = []
    for c in s:
        if cs and cs[-1] == c:
            cs.pop()
        else:
            cs.append(c)
    return ''.join(cs)