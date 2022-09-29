from random import randint

x = randint(1, 10)
print(x)
choice = 0

while choice < 3:
    find_number = int(input(f'Попытка #{choice + 1}:'))
    if 1<= find_number <= 10:
        choice += 1
        if find_number > x:
            print('Бери меньше')
        if find_number < x:
            print('Бери больше')
        if find_number == x:
            break
    else:
        print('Введите число от 1 до 10')
if find_number == x:
    print("Ты угадал")
else:
    print('Попробуйте снова')
