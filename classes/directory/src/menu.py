from loader import phonebook, Contact

from const import FILE_PATH



def start_menu():
    while True:
        change = int(input('\n1. Посмотреть контакты'
                    '\n2. Найти контакт'
                    '\n3. Удалить контакт'
                    '\n4. Изменить контакт'
                    '\n5. Добавить контакт'
                    '\n6.Выйти'
                    '\nВыбирете пункт меню: '))
        if change == 1:
            phonebook.get_contact(FILE_PATH)
            print(phonebook)
        elif change == 2:
            phonebook.get_contact(FILE_PATH )
            print(phonebook.search_contact())
        elif change == 3:
            phonebook.get_contact(FILE_PATH )
            phonebook.remove_contact()
            print(phonebook)  
        elif change == 4:
            phonebook.get_contact(FILE_PATH )
            phonebook.change_contact()
            print(phonebook)
            
        elif change == 5:
            phonebook.get_contact(FILE_PATH )
            phonebook.add_contact(Contact(input('Введите фамилию: '),
                                          input('Введите имя: '),input('Введите отчество: '),
                                          input('Введите номер телефона: ')))
            print(phonebook)   
                                          
        else:
            break