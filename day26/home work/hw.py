#1
def data(a):
    if type(a)==str:
        return "literature"
    elif type(a)== bool:
        return "science"
    return "math"
print(data(2))
#2
from collections import Counter

def most_common_type(lst):
    type_list = [type(item).__name__ for item in lst]  # თითო ელემენტის ტიპის სახელი
    type_counter = Counter(type_list)                  # ვითვლით ტიპების რაოდენობას
    most_common = type_counter.most_common(1)[0][0]    # ვიღებთ ყველაზე გავრცელებულ ტიპს
    return most_common

sample = [True, False, "hello", 1, 2, 3.14, 42]
print(most_common_type(sample))
