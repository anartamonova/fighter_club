# Задача 1. Продукты
# Необходимо написать функцию, принимающую неопределенное количество аргументов.
#  Принимаемые аргументы могут содержать множество различных данных, но требуются
# найти среди них лишь список продуктов, которые записаны просто в виде строк. 
# Если продуктов не нашлось, то вывести соответствующее сообщение.
# Примеры вызова и вывода функции
# Вызов #1:
# printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)
# Вывод #1:
# 1) Бананы
# 2) Яблоки
# 3) Макароны
# 4) Кофе 
# Вызов #2:
# printGroceries([4], {}, 1, 2, {'Mathlab'}, '')
# Вывод #2:
   
# Нет продуктов


# def printGroceries(*args):
#     list = [name for name in args if type(name) == str and len(name) > 0]
#     print(list)
#     if len(list) > 0:
#         n=1
#         for prod in list:
#             print(f"{n}). {prod}")
#             n +=1 
#     else:
#         print("Нет продуктов")

# printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)    
# printGroceries([4], {}, 1, 2, {'Mathlab'}, '')

def printGroceries(*args):
    list = [name for name in args if type(name) == str and len(name) > 0]
    print('\n'.join([f'{num}). {prod}' for num, prod in enumerate(list, 1)]) if list else 'Нет продуктов')


printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)    
printGroceries([4], {}, 1, 2, {'Mathlab'}, '')


# Задача 2. Личные данные
# Необходимо написать функцию, принимающую неопределенное количество данных о 
# сотрудниках в виде пар ключ=значение.
# Вывести эту информацию в более удобном виде (как в примерах). 
# Важное условие - ключи должны быть отсортированы по алфавиту, 
# т.е. в лексикографическом порядке.
# Примеры вызова и вывода функции
# Вызов #1:
# personalData(first_name='John', last_name='Doe', age=28, position='Python developer')
# Вывод #1:
# age: 28
# first_name: John
# last_name: Doe
# position: Python developer
# Вызов #2:
# personalData(first_name='Jack', last_name='Smith', age=32, 
# work_experience = '5 years', position='Project manager')
# Вывод #2:
# age: 32
# first_name: Jack
# last_name: Smith
# position: Project manager
# work_experience: 5 years
# Доп. условие:
# Решить задачи с использованием наименьшего количества строк

def personalData(**kwargs):
    [print(f'{key}: {kwargs[key]}') for key in sorted(kwargs.keys())]
# def personalData(**kwargs):
#     for key, value in sorted(kwargs.items()): 
#         print(key + ": " + str(value))

print(personalData(first_name='Jack', last_name='Smith', age=32, work_experience = '5 years', position='Project manager'))