#N1  https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python

def repeat_str(repeat, string):
    return string * repeat

#N2  https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python

def say_hello(name):
    return "Hello, "+ name

#N4 https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
def get_grade(s1, s2, s3):
    grd = (s1 + s2+ s3) / 3
    if grd >= 90:
        return 'A'
    elif grd >=80:
        return 'B'
    elif grd >= 70:
        return 'C'
    elif grd >= 60:
        return 'D'
    else:
        return 'F'

#N5 https://www.codewars.com/kata/583710ccaa6717322c000105/train/python
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else: 
        return number * 9