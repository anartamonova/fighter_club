import phonebook_worker

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
            phonebook_worker.get_phonebook()
        elif change == 2:
            phonebook_worker.search_contact()
        elif change == 3:
            phonebook_worker.delete_contact()
        elif change == 4:
            phonebook_worker.change_contact()
        elif change == 5:
            phonebook_worker.add_contact()
        else:
            break