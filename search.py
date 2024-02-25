import json


# def has_cyrillic(text):
#     # Проверяем, содержит ли текст кириллические символы
#     data = any(ord(char) > 127 for char in text)
#     del data

def remove_cyrillic(json_data):
    if isinstance(json_data, dict):
        for key, value in list(json_data.items()):
            if isinstance(value, str):
                new_value = ''.join([char for char in value if ord(char) <= 127])
                print(new_value)
                json_data[key] = new_value
            elif isinstance(value, (list, dict)):
                remove_cyrillic(value)
    elif isinstance(json_data, list):
        for item in json_data:
            remove_cyrillic(item)


# Загрузка JSON из файла
with open("data.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Проверяем и удаляем кириллические символы
remove_cyrillic(json_data)

# Сохраняем обновленный JSON
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
