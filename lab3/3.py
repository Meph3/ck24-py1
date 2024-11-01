def count_letters(text):
    letter_count = {}
    for char in text.lower():  # Преобразуем текст в нижний регистр
        if char.isalpha():     # Проверяем, является ли символ буквой
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())  # Общее количество букв
    frequency = {letter: round(count / total_letters, 2) for letter, count in letter_count.items()}
    return frequency

# Тестовые данные
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# Подсчёт букв и вычисление частот
letter_counts = count_letters(main_str)
letter_frequencies = calculate_frequency(letter_counts)

# Вывод частот букв
for letter, freq in letter_frequencies.items():
    formatted_freq = "{:.2f}".format(freq).replace(".", ".")
    print(f"{letter}: {formatted_freq}")
