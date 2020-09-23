import random

car_price = input("Введите стоимость автомобиля:")
car_price = car_price.replace(" ", "")

print (car_price)
car_price = float(car_price)

st_nalog = random.randint(1,15)
st_poshlina = random.randrange(14) + 1
car_nalog = float(car_price * st_nalog / 100)
car_poshlina = float (car_price * st_poshlina / 100)
full_price = float(car_price + car_nalog + car_poshlina + 10000 + 15000)

print ("Налог", st_nalog, "%", car_nalog)
print ("Пошлина%", st_poshlina, "%", car_poshlina )
print ("Доставка 10 000")
print ("Агентские 15 000")
print ("Оющая стоимость", full_price)

if full_price > 100000:
    print ("Чего-то дохрена")
else:
    print ("Ну куда ни шло")

input("\npress Enter to close the window \a")
