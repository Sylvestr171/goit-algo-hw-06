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

    def add_record(self, value):
        key = value.name.value
        value = value
        self.data[key] = value

    def find(self, search_value):
        return self.data.get(search_value, None)
    
    def delete(self, delete_value):
        if delete_value in self.data.keys():
            del self.data[delete_value]
        else:
            print (f"Value not found")
    
    def __str__(self):
        result = []
        for name, record in self.data.items():
            result.append(f"Address book {name}:\n {record}")
        return "\n".join(result)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
print(type(john))
print(f"{john}<<<<<<<<<")
john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
# book.delete("Jane")

# book = AddressBook()
# bob = Record("Bob")
# piter = Record("Piter")
# alex = Record("Alex")
# # print(f"Створено об'єкт {bob}")
# piter.add_phone('1111111111')
# bob.add_phone("1234567890")
# # print (f"виконано bob.add_phone('1234567890')\n{bob}")
# bob.add_phone("0004567890")
# piter.add_phone('2222222222')
# piter.add_phone('3333333333')
# alex.add_phone('0912837465')
# # print (f"виконано bob.add_phone('0004567890')\n{bob}")
# # bob.add_phone("0004567890")
# # print (f"виконано bob.add_phone('0004567890')\n{bob}")
# # print (f"Перевірка remove_phone")
# # bob.remove_phone('1234567890')
# # print (f"виконано bob.remove_phone('1234567890')\n{bob}")
# # bob.remove_phone('1234567890')
# # print (f"виконано bob.remove_phone('1234567890')\n{bob}")
# # print('Перевірка edit')
# # bob.edit_phone('1234567890','0004567890')
# # print (f"виконано bob.edit_phone('1234567890','0004567890')\n{bob}")
# # bob.edit_phone('0004567890','1234567000')
# # print (f"виконано bob.edit_phone('0004567890','1234567000')\n{bob}")
# # print(bob.find_phone('1234567000'))
# # print (f"виконано print(bob.find_phone('1234567000'))\n{bob}")
# # print(bob.find_phone('5555555555'))
# # print (f"виконано print(bob.find_phone('5555555555'))\n{bob}")
# # print(bob.name.value)
# book.add_record(bob)
# book.add_record(piter)
# book.add_record(alex)
# # print(book)
# # print(book.find('Bob'))
# print(book)
# book.delete('Alex')
# book.delete('Alex')
# print(book)
# # print(bob.name.value)
