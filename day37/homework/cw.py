#N1 kata
def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))
#N2 kata
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
#N3 kata
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0
#N4 kata
def getCount(s):
    return sum(c in 'aeiou' for c in s)
#N5 kata
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2