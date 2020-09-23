print ("Чтобы добавить пару сын - отец, нажмите 1")
print ("Чтобы удалить пару сын - отец, нажмите 2")
print ("Чтобы узнать отца по сыну, нажмите 3")
print ("Чтобы узнать по внуку деда, нажмите 4")
print ("Чтобы выйти, нажмите 5")
Parents = {"АЛЕКСАНДР":"СЕРГЕЙ", "СЕРГЕЙ":"АРАП"}
choice = 0
while choice!=5:
    choice = int(input ())
    if choice > 0 and choice < 6:
        if choice == 1:
            son = input ("Введите имя сына для новой пары сын - отец: ")
            son=son.upper()
            if son not in Parents:
                father = input ("Введите имя отца: ")
                father=father.upper()
                Parents[son]=father
                print ("значение добавлено!")
            else:
                print ("знаем уже всё про него")
        if choice == 2:
            son = input ("Введите имя сына для удаления пары сын - отец: ")
            son = son.upper ()
            
            if son in Parents:
                del Parents [son]
                print ("Пара удалена")
            else:
                print ("И так про него ничего не знали")
        if choice == 3:
            son = input ("Введите имя сына: ")
            son = son.upper()
            print ("Его отец", Parents.get(son, "не известен, наверное найдёнышь"))
        if choice == 4:
            grandson = input ("Введите имя внука: ")
            grandson = grandson.upper()
            if grandson in Parents:
                son = Parents [grandson]
                if son in Parents:
                    print ("Его дед", Parents [son])
                else:
                    print ("Не известен, наверное найдёнышь")
            else:
                print ("Не известен, наверное найдёнышь")
    else:
        print ("Нет такого варианта")
