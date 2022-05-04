"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
"""
year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
"""


def check_input (msg, check_data):
    answer = input(msg)
    while answer !=check_data:
        print("Не верно")
        answer = input(msg)

questions = [{'msg': 'Ввведите год рождения А.С.Пушкина:', 'check_data': '1799'},
{'msg': 'Ввведите день рождения А.С.Пушкина::', 'check_data': '6'}]

for question in questions :
    #print(question['msg'], question['check_data'])
    check_input(question['msg'], question['check_data'])