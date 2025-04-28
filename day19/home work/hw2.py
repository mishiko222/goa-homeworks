#N2
l1 = [5,6,7,8,9,10]
l2 = [11,12,13,14,15]
def l(list1,list2):
    li1 = sum(list1)
    li2 = sum(list2)

    if li1 > li2:
        return li1
    else:
       return li2

print(l(l1,l2))