#N1
 
fruits = ("ვაშლი", "ნესვი", "ბანანი", "საზამთრო", "სტაფილო")
 
print("მთელი ტუპლი:", fruits)
 
print("პირველი ელემენტი:", fruits[0])
 
print("ბოლო ელემენტი:", fruits[-1])

#N2
 
numbers = (10, 20, 30, 40, 50, 60)

 
print(" სიგრძე:", len(numbers))
 
print("მესამე ელემენტი:", numbers[2])
#N3
def reverseseq(n):
    return list(range(n, 0, -1))