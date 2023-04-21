from phonebook_worker import Contact

class Phonebook:
    def __init__(self, name: str = 'Список контактов', phonebook_list: list = None) -> None:
        if phonebook_list is None:
            phonebook_list = []
        self.name = name
        self.phonebook_list = phonebook_list
        
    def get_contact(self, path):
        with open(path, 'r', encoding='utf8') as phonebook_data:
            for line in phonebook_data:
                line = line.strip().split()
                self.add_contact(Contact(*line))
    def __str__(self) -> str:
        result_str = f'\n Название {self.name}'
        for contact in self.phonebook_list:
            result_str += f'\nФИО: {contact.surname} {contact.name} {contact. patronymic}   Моб.тел: {contact.number}' 
        return result_str
    def add_contact(self, contact: Contact):
        self.phonebook_list.append(contact)
    def remove_contact(self):
        list = self.search_contact()
        self.phonebook_list.remove(list)
        
    def search_contact(self):
        search = input('Введите данные для поиска: ')
        list = [contact for contact in self.phonebook_list if search in contact.name.lower() 
                or search in contact.surname.lower()
                or search in contact.patronymic.lower()
                or search in contact.number.lower()]
        for line in list:
         return line
        
    def change_contact(self):

        list = self.search_contact()
        print(self)
        z = int(input('Что меняем?: '
                      '\n1. Фамилия,'
                      '\n2. Имя.'
                      '\n3. Отчество.'
                      '\n4. Телефон'
                      '\nВаш выбор: '))
        if z ==1:
            Contact.change_surname(list,input('Введите новые данные: '))
        elif z ==2:
            Contact.change_name(list,input('Введите новые данные: '))
        elif z ==3:
            Contact.change_patronymic(list,input('Введите новые данные: '))
        elif z ==4:
            Contact.change_number(list,input('Введите новые данные: '))

                


    


