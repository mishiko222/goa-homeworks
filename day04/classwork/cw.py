#N1
# მომხმარებელს ეუბნებით რიცხვის შეყვანას
number = int(input("შეიყვანეთ რიცხვი: "))

# შეამოწმებთ, არის თუ არა რიცხვი ლუწი
if number % 2 == 0:
    # თუ რიცხვი ლუწია, გამოიტანეთ სიტყვა "ლუწი"
    print("ლუწი")
else:
    # თუ რიცხვი კენტია, გამოიტანეთ სიტყვა "კენტი"
    print("კენტი")

#N2
# მომხმარებელს ეუბნებით რიცხვის შეყვანას
number = int(input("შეიყვანეთ რიცხვი:"))


if number > 0:
    print(1) 

elif number < 0:
    print(-1)  
    
else:
    print(0)  

#N3
# მომხმარებელს შეაქვს ორი რიცხვი
num1 = int(input("num1:"))
num2 = int(input("num2:"))

if num1>num2:
    print(num1)
if num2>num1:
    print(num2)


#N4
# მომხმარებელს ეუბნებით რიცხვის შეყვანას
number = int(input("შეიყვანეთ რიცხვი: "))

# თუ რიცხვი იყოფა 5-ზე, გამოიტანეთ თავად რიცხვი, თუ არა - 0
if number % 5 == 0:
    print(number)  # რიცხვი 5-ზე იყოფა
else:
    print(0)  # რიცხვი 5-ზე არ იყოფა

#N5
# მომხმარებელს შეყავს რიცხვი
year = int(input("შეიყვანეთ რიცხვი: "))

# შემოწმება, არის თუ არა რიცხვი ახალი საუკუნე
if year % 100 == 0:
    print("ახალი საუკუნე")
else:
    print("ეს არ არის ახალი საუკუნე")# მომხმარებელს შეყავს რიცხვი
year = int(input("შეიყვანეთ რიცხვი: "))

# შემოწმება, არის თუ არა რიცხვი ახალი საუკუნის შსაბამისი
if year % 100 == 0:
    print("ახალი საუკუნე")
else:
    print("ეს არ არის ახალი საუკუნე")

