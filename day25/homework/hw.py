#kata N1
def remove_char(s):
    return s[1 : -1]
#kata N2
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum = sum + i
    return sum
#kata N3
def sum_array(a):
  return sum(a)
#kata N4
def twice_as_old(a, b):
    return abs(b * 2 - a)
