# import time
# import random

# # Генерация данных
# n = 100000
# data = [random.randint(1, n // 2) for _ in range(n)]
# target = random.choice(data)

# # TODO: Измерьте время поиска в списке
# start = time.perf_counter()
# target in data
# end = time.perf_counter()
# elapsed_list = end - start


# # TODO: Измерьте время поиска в множестве
# data_set = set(data)
# start = time.perf_counter()
# found = target in data_set
# time_set = time.perf_counter() - start

# # TODO: Выведите результаты
# print("List search:", elapsed_list)
# print("Set  search:", time_set)

import time
import random

sizes = [1000, 10000, 100000, 10000000]
#при n == 10_000_000 разница становится критичной для списка
#наибольшая разница возникает между 1000 и 10_000, а также 100_000 и 10_000_000
results = []

for n in sizes:
    # Генерация данных
    data = [random.randint(1, n // 2) for _ in range(n)]
    target = random.choice(data)
    
    # Измерение поиска в списке
    start = time.perf_counter()
    found = target in data
    time_list = time.perf_counter() - start
    
    # Измерение поиска в множестве
    data_set = set(data)
    start = time.perf_counter()
    found = target in data_set
    time_set = time.perf_counter() - start
    #почему размер списка не сильно сказывается на множестве.
    #происходит это потому, что все числа записываются в хеш таблицу
    #имеют свой индекс и во множестве нет дубликатов. Это значительно
    #облегчает поиск target числа
    
    results.append((n, time_list, time_set))
    
    print(f"n={n:7d} | Список: {time_list:.6f}с | Множество: {time_set:.6f}с")

with open('lab01_results.txt', 'w', encoding='utf-8') as f:
    f.write("Размер | Список (сек) | Множество (сек) | Ускорение\n")
    f.write("-" * 60 + "\n")
    for n, t_list, t_set in results:
        speedup = t_list / t_set if t_set > 0 else float('inf')
        f.write(f"{n:7d} | {t_list:12.6f} | {t_set:15.6f} | {speedup:9.1f}x\n")

print("Результаты сохранены в lab01_results.txt")