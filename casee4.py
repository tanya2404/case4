text = input("Введите текст:")

sentens = text.find(".")
count_sentens = text.count(".")

words = text.find(" ")
count_words = text.count(" ")+1

volues = ['у', 'е', 'ы', 'а', 'о', 'э', 'ё', 'я', 'и', 'ю']
count_syllables = 0
for letter in text:
    b = letter.lower()
    if b in volues:
        count_syllables += 1

ASL = count_words/count_sentens

ASW = count_syllables/count_words

Fre=1.3*ASL
fre=60.1*ASW
FRE=206.835-Fre-fre


print('Предложений:', count_sentens)
print('Слов:', count_words)
print('Слогов:', count_syllables)
print('Средняя длина предложения в словах:', ASL)
print('Средняя длина слова в слогах:', ASW)
print('Индекс удобочитаемости Флеша:', FRE)

if FRE > 80:
    print("Текст очень легко читается (для младших школьников).")
elif 50 < FRE < 80:
    print("Простой текст (для школьников).")
elif 25 < FRE < 50:
    print("Текст немного трудно читать (для студентов).")
elif FRE < 25:
    print("Текст трудно читается (для выпускников ВУЗов).")

