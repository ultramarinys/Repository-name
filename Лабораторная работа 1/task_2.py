# TODO Найдите количество книг, которое можно разместить на дискете
symbols = 25*50*100 #количество символов
count_b = 1.44*1024*1024 #размер в байтах
count_sum = count_b/4
count = int(count_sum/symbols)
print("Количество книг, помещающихся на дискету:", count)

