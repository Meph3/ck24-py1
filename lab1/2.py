# TODO Найдите количество книг, которое можно разместить на дискете

paper = 100
lines = 50
symbol = 25
kod_symbol = 4
#Размер диска
size_disk = 1024 * 1024 * 1.44
#размер 1 книги
book_size = paper * lines * symbol * kod_symbol
total_usd = 0
book = 0
#цикл считающий кол-во книг
while total_usd + book_size <= size_disk:
    total_usd += book_size
    book += 1


print("Количество книг, помещающихся на дискету:", book)
