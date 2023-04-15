from const import FILE_PATH

def get_phonebook() -> None:
    with open (FILE_PATH, 'r', encoding='utf8') as phonebook_data:
        for line in phonebook_data:
            print(line.strip())

def search_contact()-> None:
    with open (FILE_PATH, 'r', encoding='utf8') as phonebook_data:
        contact = input("Введите имя/фамилию/отчество/номер телефона: ").lower()
        for line in phonebook_data:
            if contact in line.lower():
                print(line.strip())