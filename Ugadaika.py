import random

def ask_number(qwestion, low, high):

    response = None
    while response not in range(low, high):
        response = int(input(qwestion))
    return response

tries = int(1)


predel = int (ask_number ("Я могу загадать число от 1 до скольки угодно, укажите верхнюю границу: ", 0, 1000000))
x = int(random.randint (1, predel))

print("Я загадал число от 1 до", predel, "за сколько попыток вы сможете его отгадать? ")
number = int(input())

while number > 10:
    number = int(input("Слишком многого хотите, укажите количество по-меньше "))
    
y = 0

while tries <= number and x != y:
    
    y = int (input("Какое число я загадал? "))
       
    
    if x==y and tries != 1:
        print ("Поздравляю! Угадали. Количество попыток:", tries)
        
    elif x==y and tries == 1:
         print ("Поразительно! С первого раза!")
         
    elif y > x:
        print("Ваше число БОЛЬШЕ загаданного")
        
    elif y < x:
        print("Ваше число МЕНЬШЕ загаданного")  
    tries += 1 
if x != y:
    print ("\nПопытки окончились, вы не угадали! Я загадал число", x)

input ("\nНажмите enter для выхода")
