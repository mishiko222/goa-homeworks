#1
def print_date():
    day = input("შეიყვანე დღე: ")
    month = input("შეიყვანე თვე: ")
    year = input("შეიყვანე წელი: ")

    print(f"თარიღი: {day}/{month}/{year}")


print_date()
#2
def check_password():
    password = input("შეიყვანე პაროლი: ")

    if len(password) < 8:
        print("პაროლი ძალიან მოკლეა")
    else:
        print("პაროლი მიღებულია")

check_password()
#3
def find_max():
    a = int(input("შეიყვანე პირველი რიცხვი: "))
    b = int(input("შეიყვანე მეორე რიცხვი: "))
    c = int(input("შეიყვანე მესამე რიცხვი: "))

    maximum = max(a, b, c)
    print(f"ყველაზე დიდი რიცხვი არის: {maximum}")

find_max()
#4
def sum_of_five_numbers():
    numbers = []

    for i in range(5):
        num = float(input(f"შეიყვანე {i+1}-ე რიცხვი: "))
        numbers.append(num)

    total = sum(numbers)
    print(f"რიცხვების ჯამი არის: {total}")

sum_of_five_numbers()
