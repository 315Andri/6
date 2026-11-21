
# перше завдання

sum = 0

for i in range(1, 101, 2):
    sum = sum + i

print("Сума непарних чисел:", sum)


# друге завдання

text = input("Введи якийсь текст: ")

if text != "":
    letter = text[0]
    count = 0

    for i in text:
        if i == letter:
            count = count + 1

    print("Перша літера:", letter)
    print("Кількість букв:", count)
else:
    print("Ти нічого не ввів")
