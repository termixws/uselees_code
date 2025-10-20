import json

def load_contacts(file_patch : str) -> list[dict]:
    with open(file_patch, 'r', encoding='utf=8') as file:
        data = json.load(file)
        if isinstance (data, list):
            return data
        return  []
    return []
<<<<<<< HEAD
=======

>>>>>>> 69cf31a (main)
def save_contacts(file_patch : str, contacts : list[dict]):
    with open(file_patch, 'w', encoding='utf=8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)