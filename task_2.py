information = 1.44 * (1024**2)
pages = 100
lines = 50
symbols = 25
for_one_symbol = 4
for_one_line = symbols * for_one_symbol
for_one_page = lines * for_one_line
for_one_book = pages * for_one_page
on_disk = information // for_one_book
print("Количество книг, помещающихся на дискету:", round (on_disk))
