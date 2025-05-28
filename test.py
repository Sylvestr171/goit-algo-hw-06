from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value)==10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError(f"{ValueError}\nНе вірний формат номера")
    
    def __eq__(self, other):
        eq = (self.value == other.value)
        return eq

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
   
    def add_phone(self, phone: str):
        #!!!!ChatGPT поради реалізувати через __eq__ в class(Phone) тому попередню реалізацію закоментив!!!
        # triger=True                      
        # for ithem in self.phones:
        #     if str(ithem)==phone:
        #         triger=False
        # if triger:
        #     self.phones.append(Phone(phone))
        # else:
        #     print(f'{phone} is already present in the notebook for {self.name}')
        if Phone(phone) not in self.phones:
            self.phones.append(Phone(phone))
        else:
            print(f'{phone} is already present in the notebook for {self.name}')

    def remove_phone(self, phone):
        if Phone(phone) in self.phones:
            self.phones.remove(Phone(phone))
        else:
            print('Номер не знайдено')

    def edit_phone(self, old_phone, new_phone):
        try:
            self.phones.remove(Phone(old_phone))
            self.add_phone(new_phone)
        except ValueError:
            print(f'{ValueError}\nНомер {old_phone} який необхідно змінити не знайдено')

    def find_phone(self, phone_for_search):
        if Phone(phone_for_search) in self.phones:
            return Phone(phone_for_search)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    '''
    Done 1) Реалізовано зберігання об'єкта Name в атрибуті name.
    Done 2) Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
    Done 3) Реалізовано метод для додавання - add_phone. 
    На вхід подається рядок, який містить номер телефона.
    Done 4) Реалізовано метод для видалення - remove_phone. 
    На вхід подається рядок, який містить номер телефона.
    5) Реалізовано метод для редагування - edit_phone. 
    На вхід подається два аргумента - рядки, які містять старий номер телефона та новий. 
    У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
    6)Реалізовано метод для пошуку об'єктів Phone - find_phone. На вхід подається рядок, який містить номер телефона. 
    Метод має повертати або об’єкт Phone, або None .
    '''


bob = Record("Bob")
print(f"Створено об'єкт {bob}")
bob.add_phone("1234567890")
print (f"виконано bob.add_phone('1234567890')\n{bob}")
bob.add_phone("0004567890")
print (f"виконано bob.add_phone('0004567890')\n{bob}")
bob.add_phone("0004567890")
print (f"виконано bob.add_phone('0004567890')\n{bob}")
print (f"Перевірка remove_phone")
bob.remove_phone('1234567890')
print (f"виконано bob.remove_phone('1234567890')\n{bob}")
bob.remove_phone('1234567890')
print (f"виконано bob.remove_phone('1234567890')\n{bob}")
print('Перевірка edit')
bob.edit_phone('1234567890','0004567890')
print (f"виконано bob.edit_phone('1234567890','0004567890')\n{bob}")
bob.edit_phone('0004567890','1234567000')
print (f"виконано bob.edit_phone('0004567890','1234567000')\n{bob}")
print(bob.find_phone('1234567000'))
print (f"виконано print(bob.find_phone('1234567000'))\n{bob}")
print(bob.find_phone('5555555555'))
print (f"виконано print(bob.find_phone('5555555555'))\n{bob}")
