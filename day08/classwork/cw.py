#N1






#N2
sum_result = sum(range(101))  # range(101) მოიცავს რიცხვებს 0-დან 100-მდე


print("0 დან 100-მდე რიცხვების ჯამი:", sum_result)


#N3 ვერგავიგე

    
#N4
for number in range(100, 301):
    print(number**2)
    
#N5
for i in range(1000):
    print(i % 2 == 0)


#N6

N = int(input("შეიტანეთ რიცხვი: "))

# ნეგატიური რიცხვისთვის ფესვი არ არსებობს
if N < 0:
    print(False)
else:
    print(N ** 0.5)