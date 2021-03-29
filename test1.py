'''
Разработано на версии Python 3.9.2
Дополнительные модули:
    random
    time
'''

import random
import time


# Определяем необходимые переменные
left = -100
right = 100
coordinates = []
distance_list = []
distance_summ = 0
# Переменные для разбивки координат по секторам
one = []
two = []
three = []
four = []

# Запрашиваем исходные данные у пользователя: количество точек
n = input('Введите количество точек: ')

# Проверяем корректность полученных данных
try:
    n = int(n)
except ValueError:
    print('Количество точек должно быть целым числом')
    # Даём пользователю время на прочтение сообщения и завершаем выполнение скрипта
    time.sleep(5)
    exit()

# Вычисляем координаты и заполняем список координат
for i in range(n):
    point_x = random.randint(left, right)
    point_y = random.randint(left, right)
    coordinates.append((point_x, point_y))    

# Вычисляем расстояние до точек
for piont in coordinates:
    distance = (piont[0] ** 2 + piont[1] ** 2) ** 0.5
    distance_list.append(distance)
    distance_summ += distance

# Сортируем список расстояний по возрастанию
distance_sorted = sorted(distance_list)
# Вычисляем минимальное, среднее и максимальное расстояние до точек
distance_min = distance_sorted[0]
distance_med = distance_summ / n
distance_max = distance_sorted[-1]

# Готовимся к сортировке по условию: группируем точки по секторам координат
for point in coordinates:
    if point[0] <= 0:
        if point[1] >= 0:
            # х - отрицательный, у - положительный
            four.append(point)
        else:
            # х - отрицательный, у - отрицательный
            three.append(point)
    else:
        if point[1] >= 0:
            # х - положительный, у - положительный
            one.append(point)
        else:
            # х - положительный, у - отрицательный
            two.append(point)

# Сортируем каждый сектор по условию для сортировки из задания
one_sorted = sorted(one, reverse=True)
two_sorted = sorted(two)
three_sorted = sorted(three)
four_sorted = sorted(four, reverse=True)
# Собираем отсортированный список координат
points_sorted = four_sorted + three_sorted + two_sorted + one_sorted

print('Отсортированные точки', *points_sorted, sep='\n')
print('Минимальное расстояние до точки:', distance_min)
print('Среднее расстояние до точки:', distance_med)
print('Максимальное расстояние до точки:', distance_max)
