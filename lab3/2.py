def find_common_participants(group1, group2, separator=","):
    # Разделяем строки участников на списки, используя указанный разделитель
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим пересечение множеств и сортируем результат
    common_participants = sorted(participants1 & participants2)
    return common_participants


# Пример использования
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызываем функцию с указанием разделителя
common = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common)
