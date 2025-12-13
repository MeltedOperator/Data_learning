import time
import random

# Генерация данных
n = 10000000
data = [random.randint(1, n // 2) for _ in range(n)]
target = random.choice(data)

# TODO: Измерьте время поиска в списке
start = time.perf_counter()
target in data
t_list = time.perf_counter() - start


# TODO: Измерьте время поиска в множестве
s = set(data)
start = time.perf_counter()
target in s
t_set = time.perf_counter() - start

# TODO: Выведите результаты
print("List search:", t_list)
print("Set  search:", t_set)