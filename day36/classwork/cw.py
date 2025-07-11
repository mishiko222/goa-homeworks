#N1
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
#
def check_vowel(strng, position) -> bool:
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return 0 <= position < len(strng) and strng[position] in VOWELS 