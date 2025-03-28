#N1
number = int(input("შეიყვანეთ რიცხვი: "))
# ჯამი
number1 = sum(int(digit) for digit in str(number))
# გავიგოთ ნაშთი
remainder = number % number1

print("ნაშთი:", remainder)

#N3
number = int(input("შეიყვანეთ რიცხვი: "))

# რიცხვის ზრდა
number = number + 5 if number % 2 == 0 else number * 3

# ნაშთის გამოთვლა 
print(number % 5)


#N4
#მომხმარებლის imp
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
country = input("შეიყვანეთ ქვეყანა: ")

full_imp = f"გამარჯობა მე ვარ {name} ჩემი გვარია {surname} ვარ {age}წლის ვცხოვრობ {country}"

print(full_imp)
#N5
# ახსენით რომელი გირჩევნით და რატომ:
num = 2
print("Hello " + str(num) + " world")
print("Hello", num, "world")
print(f'Hello {num} world')
#ჩემთვის ყველაზე კარგი პრაქტიკაა მესამე რადგან წარმოადგენს ყველაზე თანამედროვე და ნაკლებად დამაბნეველ მეთოდს სტრიქონების ფორმატირებისთვის.