#N1

for i in range(1, 11):
    print(f"{i} - {i**2}")

#N2
fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit.upper())

#N3
i = 0
while i <= 20:
    print(i)
    i += 2

#N4
numbers = [3, 7, 2, 9, 4, 1]

max_number = numbers[0]

# ვადარებთ დარჩენილ ელემენტებს
for num in numbers:
    if num > max_number:
        max_number = num

print("მაქსიმალური რიცხვი არის:", max_number)

#N5
number = int(input("შეიყვანე მთელი დადებითი რიცხვი: "))

sum = 0
i = 1

while i <= number:
    sum += i
    i += 1

print("ჯამი არის:", sum)