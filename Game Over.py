car_price=input("Введите тоимость автомобиля:")
car_price=car_price.replace(" ", "")
print (car_price)
car_price=float(car_price)
car_nalog = float(car_price*0.15)
car_poshlina = float (car_price*0.20)


print ("Налог 15%", car_nalog)
print ("Пошлина 20%", car_poshlina)
print ("Доставка 10 000")
print ("Агентские 15 000")
print ("Оющая стоимость", float(car_price + car_nalog + car_poshlina + 10000 + 15000))


input("\npress Enter to close the window \a")
