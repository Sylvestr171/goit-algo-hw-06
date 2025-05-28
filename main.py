from collections import UserDict

# Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім.")
        super().__init__(value)


# Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    def __init__(self, value):
        if len(value)==10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError(f"{ValueError}\nНе вірний формат номера")
    
    def __eq__(self, other):
        eq = (self.value == other.value)
        return eq

# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
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

#Клас для зберігання та управління записами.
class AddressBook(UserDict):
    '''
    Done 1) Має наслідуватись від класу UserDict.
    Done 2) Реалізовано метод add_record, який додає запис до self.data. 
    Записи Record у AddressBook зберігаються як значення у словнику. 
    Done 3) В якості ключів використовується значення Record.name.value.
    4) Реалізовано метод find, який знаходить запис за ім'ям. 
    На вхід отримує один аргумент - рядок, якій містить ім’я. Повертає об’єкт Record, або None, якщо запис не знайден.
    5) Реалізовано метод delete, який видаляє запис за ім'ям.
    Done 6)Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .
    '''
    def add_record(self, value):
        key = value.name.value
        value = value
        self.data[key] = value

    def find(self, value):
        self.data.pop(value, f"Adress book {value} not found")
    
    def __str__(self):
        return "\n".join({f"Address book: {k}" : v for k, v in self.data.items()})

book = AddressBook()
bob = Record("Bob")
piter = Record("Piter")
# print(f"Створено об'єкт {bob}")
piter.add_phone('1111111111')
bob.add_phone("1234567890")
# print (f"виконано bob.add_phone('1234567890')\n{bob}")
bob.add_phone("0004567890")
piter.add_phone('2222222222')
piter.add_phone('3333333333')
# print (f"виконано bob.add_phone('0004567890')\n{bob}")
# bob.add_phone("0004567890")
# print (f"виконано bob.add_phone('0004567890')\n{bob}")
# print (f"Перевірка remove_phone")
# bob.remove_phone('1234567890')
# print (f"виконано bob.remove_phone('1234567890')\n{bob}")
# bob.remove_phone('1234567890')
# print (f"виконано bob.remove_phone('1234567890')\n{bob}")
# print('Перевірка edit')
# bob.edit_phone('1234567890','0004567890')
# print (f"виконано bob.edit_phone('1234567890','0004567890')\n{bob}")
# bob.edit_phone('0004567890','1234567000')
# print (f"виконано bob.edit_phone('0004567890','1234567000')\n{bob}")
# print(bob.find_phone('1234567000'))
# print (f"виконано print(bob.find_phone('1234567000'))\n{bob}")
# print(bob.find_phone('5555555555'))
# print (f"виконано print(bob.find_phone('5555555555'))\n{bob}")
# print(bob.name.value)
book.add_record(bob)
book.add_record(piter)
print(book)
# print(bob.name.value)
