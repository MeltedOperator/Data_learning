import time
import random
#Теоретический вопрос 1:
#Почему же датасеты меняют инженерные решения? Почему алгоритм со 100
#элементами может оказаться совершенно неэффективным со 100 000 элементов?
#Это связано с тем, как сколько шагов приходится на проверку даты.

#Представим у нас есть большой список из случайных элементов, нам нужен
#один конкретный элемент. Даже если в этом списке есть дубликаты, программа бездумно
#пройдет через весь список и проверит каждый элемент, прежде найти(или не найти)
#нужный элемент. 

#Хеш функция не только распределит элементы по порядку, но и исключит
#из них дубликаты, так что поиск и заполнение множества придется гораздо быстрее чем 
#со списком. Но и этот алгоритм станет ненужным, если нам вдруг понадобятся все дубликаты,
#нам нужен будет алгоритм который будет сортировать элементы по их признакам
#Именно поэтому здесь важно подобрать свой механизм, который будет более эффективен
#чем предыдущий


#Теоретический вопрос 2:

#Что такое доминантный член, почему он так важен?
#Доминантный член показывает насколько быстро меняется функция
#в зависимости от числа элементов n, причем доминантный член
#будет расти гораздо быстрее чем все остальные, поэтому в первую очередь
#мы будем обращать внимание на него.

#Возьмем функцию 5n^2 + 100n + 1000. Здесь первый член будет доминантным,
#Потому что он мало того что умножается на 5, так еще и возводится во вторую
#степень. Поэтому при росте n он будет значительно больше чем 100n и особенно 1000
#давайте проверим на практике: 

# n = 100

# step = 0
# start = time.perf_counter()

# for i in range(5):
#     for j in range(n):
#         for o in range(n):
#             step += 1

# for i in range(100):
#     for j in range(n):
#         step += 1

# step += 1000

# end = time.perf_counter()
# t_data = end - start
# print(f"при {n} элементов: {t_data:.6f}с | шагов: {step} |")

# # Сохранение результатов в файл

# with open('answers.txt', 'a', encoding='utf-8') as f:
#     f.write("="*50 + "\n")
#     f.write(f"при {n} элементов: {t_data:.6f}с | шагов: {step} (Конт. вопрос 2) |\n")


#Теоретический вопрос 3:

#Сравнение функций роста.
#Даны функции f(n) = n, g(n) = n^2 и h(n) = log(n)
#При n = 1_000_000 нужно вычислить приблизительное значение
#и расположить в порядке возрастания

n = 1_000_000
def listn(n):
    start = time.perf_counter()
    fn = [random.randint(1, n) for _ in range(n)]
    target = random.choice(fn)

    start = time.perf_counter()
    found = target in fn
    time_fn = time.perf_counter() - start
    return time_fn

def logn(n):
    start = time.perf_counter()
    lgn = [random.randint(1, n) for _ in range(n)]
    lgn.sort()
    target = random.choice(lgn)
    middle = n // 2
    r_end = lgn[-1]
    l_end = lgn[0]

    start = time.perf_counter()
    if target < middle:
        r_end = middle
        middle = (middle + l_end) // 2
    elif target > middle:
        l_end = middle
        middle = (middle + r_end) // 2
    found = target in lgn
    time_lgn = time.perf_counter() - start
    return time_lgn
    
def nsquared(n):
    start = time.perf_counter()
    n_n = [random.randint(1, n) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if n_n[i] == n_n[j]:
                time_n_squared = time.perf_counter() - start
                return time_n_squared


listn_result = listn(n)
logn_result = logn(n)
n_squared = nsquared(n)
ramka = "="*50 + "\n"
result1 = f"результат f(n) = n, при n = {n}: {listn_result:.6f}c|\n"
result2 = f"результат f(n) = log(n), при n = {n}: {logn_result:.6f}c|\n"
result3 = f"результат f(n) = n^2, при n = {n}: {n_squared:.6f}c|\n"
print(result1, result2, result3)

with open('answers.txt', 'a', encoding='utf-8') as f:
    f.write(result1)
    f.write(result2)
    f.write(result3)