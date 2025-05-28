#kata N1
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

#kata N2
def to_alternating_case(s: str) -> str:
    return s.swapcase()
#kata N3
def abbrevName(name):
    new = name.title()
    a = new.split()
    b = a[0]
    c = a[1]
    d = b[0]+"."+c[0]
    return d
#kata N4
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"