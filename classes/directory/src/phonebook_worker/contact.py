class Contact:
    def __init__(self, surname, name, patronymic, number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.number = number
    def __str__(self) -> str:
        return(f'{self.surname} {self.name} {self.patronymic} {self.number}')
    def change_name(self, new_name):
        self.name = new_name
    def change_surname(self, new_surname):
        self.surname = new_surname
    def change_patronymic(self, new_patronymic):
        self.patronymic = new_patronymic
    def change_number(self, new_patronymic):
        self.number = new_patronymic
