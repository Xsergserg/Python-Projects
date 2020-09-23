import random
print("Добро пожаловать, я кину монету 100 раз и скажу сколько раз выпал орёл, а сколько решка")
number = 0
money = 0
orel = 0
reshka = 0
while number != 100:
    money = random.randint (1, 2)
    if money == 1:
        orel += 1
    elif money == 2:
        reshka += 1
    else:
        print ("Что-то не так")
        break
    number += 1
print ("Решка:", reshka )
print ("Орёл:", orel )
input ("\nНажмите enter для выхода")
