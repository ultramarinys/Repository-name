pages = 100
lines_in_page = 50
symbols_in_line = 25
symbols = pages*lines_in_page*symbols_in_line  # количество символов
count_bytes = 1.44*1024*1024 # размер в байтах
bytes_in_symbols = 4 # количество байт в одном символе
count_sum = count_bytes/bytes_in_symbols
count = int(count_sum/symbols)
print("Количество книг, помещающихся на дискету:", count)
