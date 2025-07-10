#kata N1
def litres(time):
    return time // 2

#kata N2
def number_to_string(num):
    return str(num)
#kata N3
def findSmallestInt(arr):
    return min(arr)
#kata N4
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
#kata N5
def accum(s):
    str = ""
    for i in range(0, len(s)):
        str += s[i].upper()
        str += s[i].lower()*i
        if i != len(s)-1:
            str += "-"
    return str