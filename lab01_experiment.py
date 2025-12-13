import time
import random

# Генерация данных
n = 100000
data = [random.randint(1, n // 2) for _ in range(n)]
target = random.choice(data)

# TODO: Измерьте время поиска в списке
start = time.perf_counter()
target in data
end = time.perf_counter()
elapsed_list = end - start


# TODO: Измерьте время поиска в множестве
s = set(data)
start = time.perf_counter()
target in s
end = time.perf_counter()
elapsed_set = end - start

# TODO: Выведите результаты
print("List search:", elapsed_list)
print("Set  search:", elapsed_set)