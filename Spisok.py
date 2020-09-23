import random

WORDS = ('one', 'two', 'three', 'four', 'five')
spisok = []
kolvo = len(WORDS)

for i in WORDS:
    s = random.randrange(kolvo)
    word = WORDS [s]
    while word in spisok:
        s = random.randrange(kolvo)
        word = WORDS [s]
  
    spisok.append(word)
print (spisok)

input ("ESC")
