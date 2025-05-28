# kata N1

def check_alive(healt):
    if healt<=0:
        return False
    else:
        return True
    
# kata N2

def repeat_str(repeat, string):
    return string*repeat

#kata N3

def coocie(x):
    if type(x)==float or type(x)==int:
        return 'who ate the last cookie? it was monica!'
    else:
        return 'who ate last cookie? it was the dog!'
    
#kata N4
def century(year):
    century=year/100
    if century>int(century):
        century = int(century) + 1
    return int (century)