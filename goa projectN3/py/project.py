# მომხმარებლის ანგარიშის კლასი
class UserAccount:

    def __init__(self, username, password):
        self.username = username  # მომხმარებლის სახელი
        self.password = password  # მომხმარებლის პაროლი
        self.balance = 0 # საწყისი ბალანსი იწყება 0 ლარით

    def check_balance(self):
        # ბალანსის ჩვენება
        print(f"\n{self.username}, თქვენი ბალანსია: {self.balance} ლარი")

    def deposit(self, amount):
        # თანხის შეტანა
        if amount > 0:
            self.balance += amount
            print(f"{amount} ლარი წარმატებით დაემატა.")
        else:
            print("თანხა უნდა იყოს დადებითი.")

    def withdraw(self, amount):
        # თანხის გამოტანა
        if amount <= 0:
            print("შეიყვანეთ სწორი თანხა.")
        elif amount > self.balance:
            print("არასაკმარისი თანხა.")
        else:
            self.balance -= amount
            print(f"{amount} ლარი წარმატებით მოიხმარეთ.")


# მომხმარებლების მონაცემთა ბაზა (ლექსიკონი)
accounts = {}

# ახალი მომხმარებლის ანგარიშის შექმნა
def create_account():
    username = input("შეიყვანეთ სახელი: ")
    if username in accounts:
        # თუ მომხმარებელი უკვე არსებობს
        print("მომხმარებელი უკვე არსებობს.")
        return
    password = input("შეიყვანეთ პაროლი: ")
    accounts[username] = UserAccount(username, password)  # ახალი ანგარიში ინახება 
    print(f"ანგარიში შექმნილია მომხმარებლისთვის: {username}")

# მომხმარებლის ავტორიზაცია
def login():
    username = input("მომხმარებელი: ")
    password = input("პაროლი: ")

    account = accounts.get(username)
    if account and account.password == password:
        # წარმატებული შესვლის შემთხვევაში
        print(f"მოგესალმებით, {username}!")
        user_menu(account)  # გადადის მომხმარებლის მენიუში
    else:
        print("არასწორი სახელი ან პაროლი სცადე ახლიდან")
        
        

# ავტორიზებული მომხმარებლის მენიუ
def user_menu(account):
    while True:
        print("\n--- მენიუ ---")
        print("1. ბალანსის ნახვა")
        print("2. თანხის შეტანა")
        print("3. თანხის გამოტანა")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ: ")

        if choice == "1":
            account.check_balance()  # ბალანსის ჩვენება
        elif choice == "2":
            amount = float(input("შეიყვანეთ შესატანი თანხა: "))
            account.deposit(amount)  # თანხის შეტანა
        elif choice == "3":
            amount = float(input("შეიყვანეთ გამოსატანი თანხა: "))
            account.withdraw(amount)  # თანხის გამოტანა
        elif choice == "4":
            print("გამოსვლა წარმატებით შესრულდა.")  # მენიუდან გამოსვლა
            break
        else:
            print("არასწორი არჩევანი.")

# პროგრამის მთავარი მენიუ
while True:
    print("\n=== საბანკო სისტემა ===")
    print("1. ანგარიშის შექმნა")
    print("2. შესვლა")
    print("3. გამოსვლა")

    option = input("აირჩიეთ: ")

    if option == "1":
        create_account()  
    elif option == "2":
        login()  
    elif option == "3":
        print("ნახვამდის!")  
        break
    else:
        print("არასწორი არჩევანი.")
