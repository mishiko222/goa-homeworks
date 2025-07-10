#kata N1

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

#kata N2
def reverse_words(text):
    return ' '.join([ word[::-1] for word in text.split(' ')])
#kata N3
def dont_give_me_five(start,end):
    tick = 0
    for x in range(start, end+1):
        if '5' not in str(x):
            tick += 1
    return tick

#kata N4
def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum
 
# kata N5
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a