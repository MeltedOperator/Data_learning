import time
import random

# n = 100

# step = 0
# middle_step = 0
# last_step = 0
# start = time.perf_counter()

# for i in range(5):
#     for j in range(n):
#         for o in range(n):
#             step += 1

# end = time.perf_counter()
# dominant = end - start

# start = time.perf_counter()
# for i in range(100):
#     for j in range(n):
#         middle_step = middle_step + 1

# end = time.perf_counter()
# middle = end - start

# start = time.perf_counter()
# for i in range(1000):
#     last_step += 1
# end = time.perf_counter()
# freed = end - start 

# sum = step + middle_step + last_step
# sum_t = dominant + middle + freed
# print(f"Доминатное слагаемое 5n^2. При {n} элементов время: {dominant:.6f}с | шагов: {step} (Конт. вопрос 2) |\n")
# print(f"Среднее слагаемое 100n. При {n} элементов время: {middle:.6f}с | шагов: {middle_step} (Конт. вопрос 2) |\n")
# print(f"Cвободное слагаемое 1000. При {n} элементов время: {freed:.6f}с | шагов: {last_step} (Конт. вопрос 2) |\n")
# print(f"РЕЗУЛЬТАТЫ всего шагов: {sum} | всего времени затрачено: {sum_t}")

# # Сохранение результатов в файл

# # with open('answers.txt', 'a', encoding='utf-8') as f:
# #     f.write("\n")
#     # f.write("="*50 + "\n")
# #     f.write(f"Доминатное слагаемое 5n^2. При {n} элементов время: {dominant:.6f}с | шагов: {step} (Конт. вопрос 2) |\n")
# #     f.write(f"Среднее слагаемое 100n. При {n} элементов время: {middle:.6f}с | шагов: {middle_step} (Конт. вопрос 2) |\n")
# #     f.write(f"Cвободное слагаемое 1000. При {n} элементов время: {freed:.6f}с | шагов: {last_step} (Конт. вопрос 2) |\n")
# #     f.write(f"\nРЕЗУЛЬТАТЫ. Функция вида 5n^2 + 100n + 1000 | всего шагов: {sum} | всего времени затрачено: {sum_t:.6f}с \n")
# #     f.write("="*50 + "\n")

# n = 10_000_000
# def listn(n):
#     start = time.perf_counter()
#     fn = [random.randint(1, n) for _ in range(n)]
#     target = random.choice(fn)

#     start = time.perf_counter()
#     found = target in fn
#     time_fn = time.perf_counter() - start
#     return time_fn

# def logn(n):
#     start = time.perf_counter()
#     lgn = [random.randint(1, n) for _ in range(n)]
#     lgn.sort()
#     target = random.choice(lgn)
#     middle = n // 2
#     r_end = lgn[-1]
#     l_end = lgn[0]

#     start = time.perf_counter()
#     if target < middle:
#         r_end = middle
#         middle = (middle + l_end) // 2
#     elif target > middle:
#         l_end = middle
#         middle = (middle + r_end) // 2
#     found = target in lgn
#     time_lgn = time.perf_counter() - start
#     return time_lgn
    
# def nsquared(n):
#     start = time.perf_counter()
#     n_n = [random.randint(1, n) for _ in range(n)]
#     for i in range(n):
#         for j in range(i + 1, n):
#             if n_n[i] == n_n[j]:
#                 time_n_squared = time.perf_counter() - start
#                 return time_n_squared


# listn_result = listn(n)
# logn_result = logn(n)
# n_squared = nsquared(n)
# result1 = f"Результат f(n) = n, при n = {n}: {listn_result:.6f}c|\n"
# result2 = f"Результат f(n) = log(n), при n = {n}: {logn_result:.6f}c|\n"
# result3 = f"Результат f(n) = n^2, при n = {n}: {n_squared:.6f}c|\n"
# print(result1, result2, result3)

# with open('answers.txt', 'a', encoding='utf-8') as f:
#     f.write("\n")
#     f.write("="*50 + "\n")
#     f.write(result1)
#     f.write("Алгоритм находит выбранный элемент из списка со случайными числами ЛИНЕЙНО \n")
#     f.write(result2)
#     f.write("Алгоритм находит выбранный элемент из списка со случайными числами БИНАРНЫМ способом \n")
#     f.write(result3)
#     f.write("Алгоритм определяет есть ли в списке дубликаты НАИВНЫМ способом \n")
#     f.write("="*50 + "\n")
#     f.write("РЕЗУЛЬТАТЫ: из трех алгоритмов самым быстрым можно назвать n, а самым ")
#     f.write("медленным n^2")

n = 50_000
max_random_number = 30_000
array1 = [random.randint(1, max_random_number) for _ in range(n)]
array2 = [random.randint(1, max_random_number) for _ in range(n)]

def find_common_naive(arr1, arr2):
    """
    Наивный подход: O(n * m)
    Для каждого элемента arr1 проверяем, есть ли он в arr2
    """
    common = []
    start = time.perf_counter()
    for item in arr1:
        if item in arr2 and item not in common:
            common.append(item)
    end = time.perf_counter()
    time_spent1 = end - start
    return common, time_spent1

def find_common_set(arr1, arr2):
    """
    Подход с множествами: O(n + m)
    Используем встроенную операцию пересечения множеств
    """
    start = time.perf_counter()
    set1 = set(arr1)
    set2 = set(arr2)
    end = time.perf_counter()
    time_spent2 = end - start
    return list(set1 & set2), time_spent2
border1 = "="*50
border2 = "-"*50
explanation = f"""В случае с наивным подходом мы сравниваем два массива
                в каждом из которых по {n} случайных чисел, причем среди них со 100%
                вероятностью будут дубликаты, потому что у нас число возможных 
                комбинаций чисел {max_random_number} меньше чем длина массива. Алгоритм
                пройдется по КАЖДОМУ элементу в ДВУХ массивах, ПОСМОТРИТ
                есть ли этот элемент в списке common и только потом решит добавлять
                его или нет. Это пример On^2 алгоритма. В случае же со 
                множествами у нас только уникальные числа из двух массивов,
                из которых мы уже собираем список. Нам не приходится постоянно возвращаться
                чтобы проверить есть ли элемент уже в списке или его нет, не приходится
                перепроверять дубликаты"""

common, time_spent1 = find_common_naive(array1, array2)
common_smart, time_spent2 = find_common_set(array1, array2)
with open('results.txt', 'w', encoding='utf-8') as f:

    f.write("\n"+border1+"\n")
    f.write("ДОМАШНЕЕ ЗАДАНИЕ 1 - РЕЗУЛЬТАТЫ \n")
    f.write(border1+"\n")

    f.write(f"\nРазмер array1: {len(array1)} \n")
    f.write(f"Размер array2: {len(array2)} \n")
    f.write(f"Диапазон значений: 1-{max_random_number}"+"\n"*2)

    f.write("ПОДХОД 1: НАИВНЫЙ (вложенные циклы)\n")
    f.write(border2+"\n")
    f.write(f"Время Выполнения: {time_spent1:.6f} секунд \n")
    f.write(f"Найдено Общих элементов: {len(common)}"+"\n"*2)

    f.write("ПОДХОД 2: МНОЖЕСТВА (сет интерсекшин)\n")
    f.write(border2+"\n")
    f.write(f"Время Выполнения: {time_spent2:.6f} секунд \n")
    f.write(f"Найдено Общих элементов: {len(common_smart)}"+"\n"*2)    

    f.write("СРАВНЕНИЕ \n")
    f.write(border2/5+"\n")
    f.write(f"Ускорение: {time_spent1 / time_spent2}"+"\n"*2)
    f.write("ОБЪЯСНЕНИЕ РАЗНИЦЫ В ПРОИЗВОДИТЕЛЬНОСТИ:\n")
    f.write(explanation)

