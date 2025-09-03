#N1
fruits = ("ვაშლი", "ბანანი", "მსხალი", "ფორთოხალი", "ანანასი")
 
print("მთელი ტუპლი:", fruits)
 
print("პირველი ელემენტი:", fruits[0])
 
print("ბოლო ელემენტი:", fruits[-1])

#N2
 
numbers = (10, 20, 30, 40, 50, 60)

print("ტუპლის სიგრძე:", len(numbers))

print("მესამე ელემენტი:", numbers[2])
#N3

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
 
print("გაერთიანებული ტუპლი:", combined_tuple)
#N4
animals = ("ლომი", "ვეფხვი", "სპილო", "მაიმუნი", "მელა")

 
for animal in animals:
    print(animal)