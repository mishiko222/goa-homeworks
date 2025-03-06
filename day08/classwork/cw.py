#N1
#





#N2
sum_result = sum(range(101))  # range(101) მოიცავს რიცხვებს 0-დან 100-მდე


print("0 დან 100-მდე რიცხვების ჯამი:", sum_result)


#N3
while True:
    user = input("შეიტანეთ სამ ასოიანი სიტყვა: ")

    if len(user) != 3:
        print("გთხოვთ, შეიტანოთ ზუსტად სამი ასო!")
        continue

    
    if user == user:
        print("False")
    else:
        print("true")
    break

#N4
for number in range(100, 301):
    print(number**2)
    
#N5
for i in range(1000):
    print(i % 2 == 0)