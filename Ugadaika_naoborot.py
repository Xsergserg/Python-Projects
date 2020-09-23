verh_predel = int(input("введите верхний предел "))
x = int (input ("Введите любое число в пределе "))

tries = int(1)
                  
nizh_predel = 1
y = verh_predel//2
print (y)
while x != y:
    if x > y:
        nizh_predel = y + 1
        y = verh_predel -((verh_predel - nizh_predel) // 2)
    else:
        verh_predel = y - 1
        y = verh_predel -((verh_predel - nizh_predel) // 2)
    print(y)
    tries += 1
            
print("Я угадал за", tries, "попыток")
input()
