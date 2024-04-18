class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
def input_numbers():
    numbers = input("Введіть набір чисел через пробіл: ").split()
    return [int(num) for num in numbers]

def main():
    linked_list = LinkedList()
    numbers = input_numbers()

    for num in numbers:
        linked_list.add_element(num)


if __name__ == "__main__":
    main()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.data == data:
                    print("Це число вже присутнє у списку")
                    return
                current = current.next
            if current.data == data:
                print("Це число вже присутнє у списку")
                return
            current.next = new_node

    def delete_element(self, value):
        if not self.head:
            print("Список порожній")
            return
        while self.head and self.head.data == value:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
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
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            while current:
                print(current.data, end=" -> ")
                current = prev
                prev = prev.prev
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


# Функція для виведення меню
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
    linked_list = LinkedList()

    while True:
        display_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            data = int(input("Введіть число для додавання: "))
            linked_list.add_element(data)
        elif choice == "2":
            data = int(input("Введіть число для видалення: "))
            linked_list.delete_element(data)
        elif choice == "3":
            print("Вміст списку (з початку):")
            linked_list.display_list(from_start=True)
        elif choice == "4":
            print("Вміст списку (з кінця):")
            linked_list.display_list(from_start=False)
        elif choice == "5":
            data = int(input("Введіть число для перевірки: "))
            if linked_list.check_value(data):
                print("Це число знайдено у списку")
            else:
                print("Це число не знайдено у списку")
        elif choice == "6":
            old_value = int(input("Введіть старе число: "))
            new_value = int(input("Введіть нове число: "))
            replace_option = input("Замінити всі входження? (так/ні): ")
            replace_all = True if replace_option

