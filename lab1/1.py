numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]




# Нахождение суммы и количества всех значений, отличных от None
valid_numbers = [num for num in numbers if num is not None]
# общее количество включает None
average_value = sum(valid_numbers) / len(numbers)

# Замените None на среднее значение.
numbers[numbers.index(None)] = average_value
print("Измененный список:", numbers)