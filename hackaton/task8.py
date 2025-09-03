# Instructions:
#  Check if a number a is greater than 0. Store True in result if it is, otherwise store False.
# Test Cases:
#  assert result == True when a = 4
#  assert result == False when a = -2

i = int(input("enter your number"))
if i < 0:
    print(True)
else:
    print(False)