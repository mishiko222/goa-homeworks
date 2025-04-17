#N1
numbers = [1, 4, 3, 6, 9, 11, 17, 13, 26, 30]

even_sum = 0
odd_count = 0


for num in numbers:
    if num % 2 == 0:
        even_sum += num  # თუ ლუწია ვამატებთ ჯამში
    else:
        odd_count += 1   # თუ კენტია, ერთით გავზარდოთ მრიცხველი

print("ლუწი რიცხვების ჯამი:", even_sum)
print("კენტი რიცხვების რაოდენობა:", odd_count)

#N2
my_lists=[1,4,5,8,2,22]

my_lists.append(3)

print(my_lists)

#N3
my_lists= [1,2,3,3,4,5] 

my_lists.pop(3)

print(my_lists)

#N4
my_lists=[1,2,3,4,6,8,9] 

my_lists.insert(4,5) 
my_lists.insert(6,7)

print(my_lists)
#N5
# append() - ამატებს ელემენტს სიის ბოლოში
# pop() - შლის ელემენტს სიიდან (ნაგულისხმევად ბოლოს)
# insert() - ამატებს ელემენტს კონკრეტულ ადგილას (ინდექსზე)
