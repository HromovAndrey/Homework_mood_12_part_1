# Завдання
# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Number:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_element(self, value):
        if not self.head:
            print("Список порожній")
            return
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                if current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
            current = current.next

    def display_list(self, from_start=True):
        if not self.head:
            print("Список порожній")
            return
        if from_start:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
        else:
            current = self.tail
            while current:
                print(current.data, end=" -> ")
                current = current.prev
            print("None")

    def check_value(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def replace_value(self, old_value, new_value, replace_all=False):
        if not self.head:
            print("Список порожній")
            return
        current = self.head
        replaced = False
        while current:
            if current.data == old_value:
                current.data = new_value
                if not replace_all:
                    replaced = True
                    break
            current = current.next
        if not replaced:
            print("Елемент не знайдено")

def display_menu():
    print("Меню:")
    print("1. Додати нове число до списку")
    print("2. Видалити усі входження числа зі списку")
    print("3. Показати вміст списку (з початку)")
    print("4. Показати вміст списку (з кінця)")
    print("5. Перевірити, чи є значення у списку")
    print("6. Замінити значення у списку")
    print("7. Вийти")

def main():
    doubly_linked_list = Number()

    while True:
        display_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            data = input("Введіть число для додавання: ")
            if doubly_linked_list.check_value(data):
                print("Це число вже присутнє у списку")
            else:
                doubly_linked_list.add_element(data)
        elif choice == "2":
            data = input("Введіть число для видалення: ")
            doubly_linked_list.delete_element(data)
        elif choice == "3":
            print("Вміст списку (з початку):")
            doubly_linked_list.display_list(from_start=True)
        elif choice == "4":
            print("Вміст списку (з кінця):")
            doubly_linked_list.display_list(from_start=False)
        elif choice == "5":
            data = input("Введіть число для перевірки: ")
            if doubly_linked_list.check_value(data):
                print("Це число знайдено у списку")
            else:
                print("Це число не знайдено у списку")
        elif choice == "6":
            old_value = input("Введіть старе число: ")
            new_value = input("Введіть нове число: ")
            replace_option = input("Замінити всі входження? (так/ні): ")
            replace_all = True if replace_option.lower() == "так" else False
            doubly_linked_list.replace_value(old_value, new_value, replace_all)
        elif choice == "7":
            print("До побачення!")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
