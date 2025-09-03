#N1
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
#N2
def double_integer(i):
    return i+i
#N3
def repeat_str(repeat, string):
    return repeat * string
#N4
def remove_char(s):
    return s[1 : -1]