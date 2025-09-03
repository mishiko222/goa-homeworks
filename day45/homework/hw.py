#N1
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
#N2
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
#N3
def find_smallest(numbers,to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))
#N4
def calc(s):
    total1 = ''.join(map(lambda c: str(ord(c)), s))
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))
#N5
def get_size(w, h, d):
    area = 2*(w*h + h*d + w*d)
    volume = w*h*d
    return [area, volume]