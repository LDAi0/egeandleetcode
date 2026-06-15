# Читаем строку, очищая от возможных пробелов и переносов
s = open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\task 24\24-14100_14100.txt').readline().strip()

n = len(s)
# dp[i] — максимальная длина цепочки, заканчивающаяся в индексе i
dp = [0] * (n + 1)
words = ["ABA", "CB", "AC", "BB", "ABC", "BCB", "BA", "AB"]

for i in range(1, n + 1):
    for w in words:
        len_w = len(w)
        # Если слово w помещается перед текущей позицией и совпадает со срезом строки
        if i >= len_w and s[i - len_w:i] == w:
            # Пытаемся продлить цепочку, которая заканчивалась перед этим словом
            dp[i] = max(dp[i], dp[i - len_w] + len_w)

# Ответом будет самая длинная цепочка, найденная в массиве
print(max(dp))