#N1
def calculator(x, y, op):
    try:
        return {'+': x + y, '-': x - y, '': x - y, '/': x / y}[op]
    except (TypeError, KeyError): 
        return 'unknown value'
#N2
def count_positives_sum_negatives(arr):
    if not arr: return []
    positive = 0
    negative = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [positive, negative]
#N3
def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]