stacks = 30
sila = 0
lovka = 0
intel = 0
zhiza = 0
i=0
print ("Для увеличения силы введите 1, для увеличения ловкости введите 2, для увеличения интеллекта введите 3, для увеличения живучести введите 4, для уменьшения силы введите 5, для уменьшения ловкости введите 6, для уменьшения интеллекта введите 7, для уменьшения живучести введите 8, для окончания введите 9")
print ("Осталось:", stacks, "очков")

while i==0:
    choise = int(input())
    if choise > 0 and choise < 10:
        if choise == 1 and stacks > 0:
            sila += 1
            stacks -= 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 2 and stacks > 0:
            lovka += 1
            stacks -= 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 3 and stacks > 0:
            intel += 1
            stacks -= 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 4 and stacks > 0:
            zhiza += 1
            stacks -= 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 5 and sila > 0:
            sila -= 1
            stacks += 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 6 and lovka > 0:
             lovka -= 1
             stacks += 1
             print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 7 and intel > 0:
            intel -= 1
            stacks += 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 8 and zhiza > 0:
            zhiza -= 1
            stacks += 1
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =", stacks )
        elif choise == 5 and sila == 0:
            print ("нечего отсюда вычитать")
        elif choise == 6 and lovka == 0:
            print ("нечего отсюда вычитать")
        elif choise == 7 and intel == 0:
            print ("нечего отсюда вычитать")
        elif choise == 8 and zhiza == 0:
            print ("нечего отсюда вычитать")   
        elif choise > 0 and choise <5 and stacks==0:
            print ("Ну нет же больше очков, чего тыкать")
        elif choise == 9 and stacks != 0:
            print ("Рано, очки есть ещё")
        elif choise == 9 and stacks == 0:
            print ("Поздравляю, подсчёт окончен!")
            print ("Характеристики: Сила =", sila, "Ловкость =", lovka, "Интеллект =", intel, "Живучесть =", zhiza, "Осталось очков =")
            i=1
    else:
           print ("Совсем дурные? Нет такой цифры")
input ("\tХорош, выходим отсюда")
