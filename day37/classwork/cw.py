#N1
def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
#N2
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
#N3
def remove_exclamation_marks(s):
    return s.replace('!','')