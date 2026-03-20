from itertools import product

cnt = 0
# Алфавит 6-ричной системы: 0, 1, 2, 3, 4, 5
# Четные цифры в этой системе: 0, 2, 4

for i in product('012345', repeat=7):
    # 1. Число не может начинаться с нуля
    if i[0] == '0':
        continue
    
    # Превращаем кортеж в строку для удобства поиска
    a = ''.join(i)
    
    # 2. Ровно одна цифра 2
    if a.count('2') == 1:
        index_2 = a.find('2')
        
        # Проверяем соседей цифры 2
        is_valid = True
        
        # Проверяем соседа слева (если он есть)
        if index_2 > 0:
            if a[index_2 - 1] in '024':
                is_valid = False
        
        # Проверяем соседа справа (если он есть)
        if index_2 < 6:
            if a[index_2 + 1] in '024':
                is_valid = False
        
        if is_valid:
            cnt += 1

print(f"Итоговое количество: {cnt}")