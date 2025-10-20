def show_menu() -> str:
    print("\n--- Меню ---")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Найти контакт")
    print("0. Выход")
    return input("Ваш выбор: ")

def get_new_contact_info() -> dict:
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    if name or phone == "":
        print("Этот параметр не может быть 0.")
    else:
        return {"name": name, "phone": phone}

def get_search_query() -> str:
    return input("Введите строку для поиска: ")

def display_contacts(contacts: list[dict]):
    if not contacts:
        print("Записная книжка пуста или ничего не найдено.")
        return

    print("\n--- Список контактов ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} (тел: {contact['phone']})")
    print("-----------------------")

def display_message(message: str):
    print(message)