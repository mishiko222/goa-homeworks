#N1
def plus(x,y):
    if type(x) and int(x) != int:
        return int(x) + int(y)
    if type(x) or type(y) !=int:
        return int(x) + int(y)
    else:
        return x + y 
    
print(plus('4',7))


#N2
def devision(x, y):
    x=int(x)
    y=int(y)

    if x == 0 or y == 0:
        return "zero devission error"
    if x < y:
        return x / y
    elif x > y:
        return 
    else: 
        return x + y
    
print(devision('12',4))

#N3
def string_add(x,y):
    if type(x) == int and type(y) == str:
        return y + str(x)
    elif type(y) == int and type(x) == str:
        return x +str(y)
    elif type(x) == int and type(y) ==int:
        return str(x) +str(y)
    
#N4 
def check(world,type_of_world):
    if type(world)!=type_of_world:
        return False
    else:
        return False
    
