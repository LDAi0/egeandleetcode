from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * f(n - 3)


for i in range(0, 247563):
    f(i)

print((f(247563) // 519 - 477 * f(247560)) // f(247557))
