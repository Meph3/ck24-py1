import json


def calculate_sum_of_products(json_file_path):
    try:
        # Чтение JSON файла
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверка, что данные являются списком словарей
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Файл должен содержать список словарей.")

        # Вычисление суммы произведений "score" и "weight"
        total = sum(item["score"] * item["weight"] for item in data if "score" in item and "weight" in item)

        # Округляем результат до 3 знаков после запятой
        return round(total, 3)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении или парсинге файла: {e}")
    except ValueError as e:
        print(f"Ошибка в данных: {e}")


# Пример использования
result = calculate_sum_of_products("input.json")
if result is not None:
    print(result)
