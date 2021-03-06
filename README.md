# Назначение
Тестовое задание для курса "BACKEND. PYTHON Базовый уровень" у Digital Spectr в мае 2021  
http://academy.digital-spectr.ru/backend_python_basic

# Информация для запуска
Разработано на версии Python 3.9.2  
Дополнительные модули:
  + random  
  + time  
  + re
# Задачи
### Задание 1 (**test1.py**)
Сформировать список из n точек на декартовой плоскости (х,у), заполнять значения координат точек случайными целыми числами (-100, 100).  
Расположить точки в порядке обхода против часов стрелки, начиная с точки, ближайшей к оси у, лежащей в координатном углу I (положительные абсциссы и ординаты ), если есть таковые.  
Найти среднее, мин., макс. расстояния точек от центра координатной плоскости (0,0). Вывести результаты на экран.  
Размер исходного списка n задается пользователем вручную после запуска программы.

### Задание 2 (**test2.py**)
Написать программу на языке python версии 3, отсеивающую автомобильные номера неправильного формата, т.е. проверка ГРЗ типа 1А из проверочного списка. 
  
Пример списка: ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12"].  
Для данного примера **правильным ответом будет**  ["A123AA11", "А222АА123"]. 

Дополнить список верными и неверными номерами. Список для проверки в теле программы (не в файле).  
Приветствуется несколько вариантов решений.  
  
Подробнее про регистрационные транспортные знаки можно прочитать по ссылке:  
https://ru.wikipedia.org/wiki/Регистрационные_знаки_транспортных_средств_в_России)  

# Реализованный функционал (для задачи 1)
+ Проверка входных данных от пользователя
+ Оповещение в случае, если значение введено некорректно
+ Формирование необходимого количества координат (задаётся пользователем) в виде списка
+ Сортировка списка координат по условию задачи  
Сортировка реализована через разбивку координатной плоскости на 4 сегмента
+ Вывод отсортированного списка координат на экран в столбик для наглядности
+ Вычисление минимального, среднего и максимального расстояния точек от центра координатной плоскости (0,0), исходя из полученных точек и вывод этих значений на экран

# Реализованный функционал (для задачи 2)
+ Разработано 2 паттерна для выявления валидных номеров (с двузначным и трёхзначным регионом), использующиеся при валидации
+ Проверка осуществляется как для русских, так и для английских букв (список взят из статьи https://ru.wikipedia.org/wiki/Регистрационные_знаки_транспортных_средств_в_России)
+ Вывод валидных номеров в столбец на экран
