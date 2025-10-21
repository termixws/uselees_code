from storage_manager import *
from user_interface import *

file_save = "contacts.json"

def main():
    contact_list = load_contacts(file_save)
    while True:
        chouse = show_menu()
        if chouse == "1":
            display_contacts(contact_list)
        elif chouse == "2":
            new_user = get_new_contact_info()
            contact_list.append(new_user)
            save_contacts(file_save, contact_list)
            display_message(f"Контанкт {new_user['name']} добавлен")
        
        elif chouse == "3":
            queri = get_search_query()
            found = []
            for contact in contact_list:
                name_search = queri in contact['name']
                phone_search = queri in contact['phone']
                if name_search or phone_search:
                    found.append(contact)
                if found:
                    display_contacts(found)
                else:
                    print("Контакт не найден")
        elif chouse == "0":
            break
        
if __name__ == "__main__":        
    main()
            