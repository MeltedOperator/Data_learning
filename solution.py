#эксперименты с алгоритмами
import random
import time

def measure_list_search(n, trials=5):
    arr = [random.randint(1, 1_000_000) for _ in range(n)]
    target = arr[-1]
    total = 0
    for _ in range(trials):
        start = time.perf_counter()
        target in arr
        end = time.perf_counter()
        total += (end - start)
    return total / trials

for size in [1_000, 10_000, 100_000, 300_000]:
    avg = measure_list_search(size)
    print(f"Size={size:7d}, avg_time={avg:.6f} s")