#N1 kata
def calculator(x,y,op):
    if not isinstance(x, int) or not isinstance(y, int):
        return 'unknown value'
    
    if op == '+':
        return x + y
        
    if op == '-':
        return x - y
        
    if op == '*':
        return x * y
        
    if op == '/':
        return x / y
        
    return 'unknown value'



#N4 kata
def count_char_occurrences(strng, char):
    return sum(1 for a in strng if a == char)

