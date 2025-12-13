import time
import random

# Генерация данных
n = 100000
data = [random.randint(1, n // 2) for _ in range(n)]
target = random.choice(data)

# TODO: Измерьте время поиска в списке
start = time.perf_counter()
target in data
print(f"Size={n}, avg_time={start} s")
# ..

# TODO: Измерьте время поиска в множестве
# ...

# TODO: Выведите результаты