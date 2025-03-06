
#N1
text = input("შეიყვანეთ ტექსტი: ")
number = int(input("შეიყვანეთ რიცხვი (მაშინ, რიცხვი იქნება ასოინდექსი): "))

if 0 < number <= (text):
    print("მომხმარებლის მიერ მითითებული რიცხვის ასო არის:", text[number-1])
else:
    print("თქვენ შეიყვანეთ არასწორი რიცხვი!")

#N2

for number in range(100, 0, -1):
    print(number)



#3
for number in range(1, 101, 2):
    print(number)
    

#4
for number in range(250, 500, 10):
    print(number)

#5

sityva = input("შეიყვანეთ სიტყვა: ")  #ვთხოვთ მომხმარებელს, რომ შეიტანოს სიტყვა


if sityva[0] == '_':  # სიტყვა უნდა იწყებოდეს _-ით
    print(True)  #თუ სიტყვა _-ით იწყება, გამოსცემს True
else:
    print(False)
    
#6
number = int(input("შეიყვანეთ რიცხვი: "))  # ვთხოვთ რიცხვს

if number % 2 == 0:  # თუ რიცხვი ლუწია
    for _ in range(10):
        print("Yes")
else:  # თუ რიცხვი კენტია
    print("No")