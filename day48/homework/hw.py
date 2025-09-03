#N1
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 3]

duplicates = set()
seen = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("განმეორებული რიცხვები:", duplicates)
#N2
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique_elements = list(set(list1 + list2))
print("უნიკალური ელემენტები:", unique_elements)
#N3
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

common_elements = list(set(list1) & set(list2))
print("საერთო ელემენტები:", common_elements)
#N4
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

unique_numbers = list(set(numbers))
print("უნიკალური ელემენტები:", unique_numbers)
#N5
my_set = {10, 20, 30, 40}
value = 30

if value in my_set:
    print(f"{value} შედის ნაკრებში.")
else:
    print(f"{value} არ შედის ნაკრებში.")
