
age = int(input("შეიყვანეთ თქვენი ასაკი: "))


if age <= 10:
    print("Kid")
elif age > 10 and age < 18:
    print("teenager")
elif age >= 18 and age < 30:
    print("adult")
else:
    print("unc")

    #N2

def ჩემი_ფუნქცია(სია):
    
    if not სია:
        return []

    დადებითი = 0
    უარყოფითი = 0

   
    for რიცხვი in სია:
        if რიცხვი > 0:
           
            დადებითი += 1
        elif რიცხვი < 0:
            
            უარყოფითი+= რიცხვი

  
    return [დადებითი, უარყოფითი]