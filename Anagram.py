import random
WORDS = ("мать", "отец", "сын", "дочь")
word = random.choice(WORDS)
correct = word
anagram = ''
score = len (word) - 1
answer = 0
tries = 0

while word:
    position = random.randrange(len(word))
    anagram += word [position]
    word = word [:position] + word [position+1:]

print("Я загадал анаграмму " + anagram + " отгадай её! Для получения подсказки введи 1, всего можно набрать", score, "очков, у вас", score, "попыток или ", score-1,  " подсказок.")

while answer != correct and score != 0:
    
    answer = input ("Какое слово загадано? ")
    
    if answer == "1" and score == 1:
        print ("Подсказок больше нет!")
        
    if answer == "1" and score >= 2:
        tries += 1
        print ("Следующая буква ", correct [(tries-1)])
        score -= 1
        print ("Осталось", score-1, "подсказок и ", score, "попыток")    

    if answer == correct:
        print ("Правильно, с учётом подсказок вы набрали", score, "очков")

    if answer != correct and answer != "1" and score > 1:
        score -= 1
        print ("Неправильно! Осталось", score-1, "подсказок и ", score, "попыток")

    if answer != correct and answer != "1" and score == 1:
        score -= 1
        print ("Неправильно! Попыток больше нет!")
        
input ()
    
