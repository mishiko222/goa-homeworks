#N1
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
#N3
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
#N4
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
#N5
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
#N6
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
#N7
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)