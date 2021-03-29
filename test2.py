'''
https://github.com/Mitayes/digital-spectr-django-backend-2021-05/blob/main/test2.py
Разработано на версии Python 3.9.2
Дополнительные модули:
    re
'''

import re

# Штатный список для тестирования из задания
test_str = ['А123АА11', 'А222АА123', 'А12АА123', 'А123СС1234', 'АА123А12', 'А123ВА12']
# Расширенный список для тестирования
test_str2 = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "A123AA01", "A123AA021", "A123AA210"]
# В этот список складываем верные номера
result = []

# Шаблон для номеров с двузначным регионом
used_pattern1 = r"[АВЕКМНОРСТУХABEKMHOPCTYX]\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2}\d{2}"
# Шаблон для номеров с трёхзначным регионом
used_pattern2 = r"[АВЕКМНОРСТУХABEKMHOPCTYX]\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2}[1-9]\d{2}"

# Тут можно выбрать по какому списку будем искать верные номера
for i in test_str2:
    if re.search(used_pattern1, i):
        if re.search(used_pattern1, i).group() == i:
            result.append(i)
    if re.search(used_pattern2, i):
        if re.search(used_pattern2, i).group() == i:
            result.append(i)
# Выводим результат
print(*result, sep='\n')
