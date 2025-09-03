#N1 kata
def square_digits(n):
    return int("".join(str(pow(int(i), 2)) for i in str(n)))
#N2 kata
def get_min_max(seq): 
    return min(seq), max(seq)
