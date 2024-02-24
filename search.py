import json


def remove_non_ascii(text):
    """Удаляет все ASCII символы из строки."""
    return ''.join(char for char in text if ord(char) < 128)


def clean_json(json_data):
    """Удаляет ASCII символы из значений в JSON данных."""
    if isinstance(json_data, dict):
        return {key: clean_json(value) for key, value in json_data.items()}
    elif isinstance(json_data, list):
        return [clean_json(item) for item in json_data]
    elif isinstance(json_data, str):
        return remove_non_ascii(json_data)
    else:
        return json_data


def process_json_file(input_file, output_file):
    """Читает JSON файл, удаляет ASCII символы и записывает обновленные данные в новый JSON файл."""
    with open(input_file, 'rb') as f:
        for encoding in ['utf-8', 'utf-16', 'latin-1']:  # Попробуйте различные кодировки
            try:
                data = f.read().decode(encoding)
                break
            except UnicodeDecodeError:
                pass
        else:
            raise UnicodeDecodeError("Не удалось прочитать файл в поддерживаемых кодировках.")

    cleaned_data = clean_json(json.loads(data))

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)


# Пример использования:
input_file = 'mydata.json'
output_file = 'newdata.json'
process_json_file(input_file, output_file)
print("ASCII символы удалены из файла и сохранены в", output_file)
