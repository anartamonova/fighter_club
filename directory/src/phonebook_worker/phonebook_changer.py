from const import FILE_PATH

def delete_contact()-> None:
    with open (FILE_PATH, 'r', encoding='utf8') as phonebook_data:
        all_contacts = phonebook_data.readlines()
        delete = input('Введите контакт для удаления: ')
        result = [line for line in all_contacts if delete.lower() not in line.lower()]
    with open (FILE_PATH, 'w', encoding='utf8') as phonebook_data:
        for line in result:
            phonebook_data.write(line)

def change_contact()-> None:
    with open (FILE_PATH, 'r', encoding='utf8') as phonebook_data:
            all_contacts = phonebook_data.readlines()
            delete = input('Введите контакт для изменения: ')
            result = [line for line in all_contacts if delete.lower() not in line.lower()]
            сhange = [line.split(' ') for line in all_contacts  if delete.lower() in line.lower()]
            r=int(input('\nВыбирете, что нужно изменить:'
                        '\n1. Фамилия'
                        '\n2. Имя'
                        '\n3. Отчество'
                        '\n4. Номер телефона'))
            print(сhange)
            if r ==1:
                f= str(input('Введите новую фамилию: '))
                сhange[0][0]=f
            elif r == 2:
                n= str(input('Введите новое имя: '))
                сhange[0][1]=n
            elif r == 3:
                s= str(input('Введите новое отчество: '))
                сhange[0][2]=s
            elif r == 4:
                num= str(input('Введите новый номер телефона'))
                сhange[0][3]=num

    with open (FILE_PATH, 'w', encoding='utf8') as phonebook_data:
            for line in result:
                phonebook_data.write(line)
            phonebook_data.write(f'\n{сhange[0][0]} {сhange[0][1]} {сhange[0][2]} {сhange[0][3]}')

def add_contact():
    surname = input('Введите фамилию: ')
    second_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    with open (FILE_PATH, 'a', encoding='utf8') as phonebook_data:
        phonebook_data.write(f'\n{surname} {second_name} {patronymic} {number}\n')

