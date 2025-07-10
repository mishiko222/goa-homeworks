#1 kata
def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))
#N2 kata
def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"
#N3 kata
def getCount(s):
    return sum(c in 'aeiouAEIOU' for c in s)
#N4 kata
