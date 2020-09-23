begin = int(input("Введите начало счёта "))
end = int(input("Введите конец счёта "))
intwal = int(input("Введите интервало между числами "))
x = begin
posl = ()
sum = 0
while end >= x:
    posl += (x,)
    sum += x
    x += intwal   
    

print ("Всего в последовательности", len(posl), "элементов. \nА именно: ", posl, "\nСумма элементов: ", sum)
input ()
