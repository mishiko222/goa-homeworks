#N1
list=[1,2,4,5,8,14]
def manual_remove(list, value):
    new_list = []
    for item in list:
        if item != value:
            new_list.append(item)
    return new_list
print(manual_remove)

#N2
def manual_index(a,b):
    this = -1
    for i in a:
        this += 1
        if i==b:
            return this

print(manual_index)

#N3
list=[3,7,9,7,0]
def manual_len(a):
    len = 0
    for i in a:
        len += 1
        return len
    
print(manual_len(list))

#N4
def manual_pop(a,b):
    list = []
    index =- 1
    for i in a:
        index += 1
        if index - b:
            list - list +[i]
            return list
    
print(manual_pop)

#N5
def manual_reverse(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list
print(manual_reverse([1, 2, 3, 4]))