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
data_set = set(data)
start = time.perf_counter()
found = target in data_set
time_set = time.perf_counter() - start

# TODO: Выведите результаты
print("List search:", elapsed_list)
print("Set  search:", time_set)

# import time
# import random

# sizes = [1000, 10000, 100000, 300000]
# results = []

# for n in sizes:
#     # Генерация данных
#     data = [random.randint(1, n // 2) for _ in range(n)]
#     target = random.choice(data)
    
#     # Измерение поиска в списке
#     start = time.perf_counter()
#     found = target in data
#     time_list = time.perf_counter() - start
    
#     # Измерение поиска в множестве
#     data_set = set(data)
#     start = time.perf_counter()
#     found = target in data_set
#     time_set = time.perf_counter() - start
    
#     results.append((n, time_list, time_set))
    
#     print(f"n={n:7d} | Список: {time_list:.6f}с | Множество: {time_set:.6f}с")