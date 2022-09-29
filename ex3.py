x = int(input('Введите координаты числа x: '))
y = int(input('Введите координаты числа y: '))
print()

def coordinate(x,y):
    if x > 0 and y > 0:
        print('Точка находится в 1 четверти')
    elif x > 0 and y < 0:
        print('Точка находится в 4 четверти')
    elif x < 0 and y < 0:
        print('Точка находится в 3 четверти')
    else:
        print('Точка находится в 2 четверти')

coordinate(x,y)