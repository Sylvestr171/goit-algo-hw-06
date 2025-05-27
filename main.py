from collections import UserDict

# Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    def __init__(self, name):
        self.name = name

class IncorrectPhoneNumber(Exception):
    def __init__(self, message="Помилка формату номера телефону.Номер телефону повинен містити тільки цифри та дорівнювати 10 знакам"):
        self.message = message
        super().__init__(self.message)


# Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    '''
    Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    Наслідує клас Field. Значення зберігaється в полі value .
    '''
    # реалізація класу
    def phone_number_validation(self, phone:str):
        if len(phone)==10 and phone.isdigit():
            return phone
        else:
            raise IncorrectPhoneNumber



# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    '''
        Реалізовано зберігання об'єкта Name в атрибуті name.
        Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
        Реалізовано метод для додавання - add_phone .На вхід подається рядок, який містить номер телефона.
        Реалізовано метод для видалення - remove_phone. На вхід подається рядок, який містить номер телефона.
        Реалізовано метод для редагування - edit_phone. На вхід подається два аргумента - рядки, які містять старий номер телефона та новий. 
    У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
        Реалізовано метод для пошуку об'єктів Phone - find_phone. На вхід подається рядок, який містить номер телефона. Метод має повертати або об’єкт Phone, або None .
    '''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone: str):
        self.phones.append(Phone.phone_number_validation(phone))

    def remove_phone(self, phone: str):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print('Номер не знайдено')

    def edit_phone(self, old_phone: str, new_phone: str):
        try:
            self.phones.remove(old_phone)
            add_phone(new_phone)
        except ValueError:
            print(f'Номер {old_phone} не знайдено')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

#Клас для зберігання та управління записами.
class AddressBook(UserDict):
    '''
        Має наслідуватись від класу UserDict.
        Реалізовано метод add_record, який додає запис до self.data. 
    Записи Record у AddressBook зберігаються як значення у словнику. 
    В якості ключів використовується значення Record.name.value.
        Реалізовано метод find, який знаходить запис за ім'ям. 
    На вхід отримує один аргумент - рядок, якій містить ім’я. Повертає об’єкт Record, або None, якщо запис не знайден.
    Реалізовано метод delete, який видаляє запис за ім'ям.
    Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .
    '''
    # реалізація класу
    pass
