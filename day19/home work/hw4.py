#N4
li = [134,22,13,24,5,16,73,8,]

def l(list):
    l2 = []
    for i in list:
        if i % 3 != 0:
            l2.append(i)

    return l2

    print(l(l1))