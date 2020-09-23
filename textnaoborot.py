text = input ("Ввведите текст: ")
textnaob = ""
while text:
    textnaob += text[(len(text)-1)]
    text = text [:(len(text)-1)]
print("Текст наоборот:", textnaob)
input
