from storage_manager import *
from user_interface import *

file_save = "contacts.json"

def main():
    contact_list = load_contacts(file_save)
    while True:
        chouse = show_menu()
        if chouse == 1:
            display_contacts(contact_list)
        elif chouse == 2:
            get_new_contact_info(contact_list)
            