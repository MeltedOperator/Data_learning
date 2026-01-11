import random
import time

def find_duplicates(items):
    """
    Найти все дубли за O(n).
    
    find_duplicates([1, 2, 3, 2, 4, 3]) → [2, 3]
    """
    seen = set()
    duplicates = 0
    start = time.perf_counter()

    for item in items:
        if item in seen:
            duplicates += 1
        else:
            seen.add(item)
    time_set = time.perf_counter() - start
    return duplicates, time_set

def find_dublicates_hard(items):
    """
    Найти все дубли за O(n^2)

    find_dublicates_hard([1→2→3→2(!)→4→3(!)]) 
    """
    dublicates = 0
    n = len(items)
    start = time.perf_counter()
    for i in range(n):
        for j in range(i+1, n):
            if items[i] == items[j]:
                dublicates += 1
                break
    time_set = time.perf_counter() - start
    return dublicates, time_set

# num_elements = [1_000, 10_000, 10_000]
# for n in num_elements:
#     items = [random.randint(1, 30_000) for _ in range(n)]
#     print(f"{find_dublicates_hard(items)} | {find_duplicates(items)}")


with open("report.md", "w", encoding="utf-8") as f:
    num_elements = [1_000, 10_000, 1_000]
    for n in num_elements:
        items = [random.randint(1, 30_000) for _ in range(n)]

        dublicates, velocity = find_duplicates(items)
        dublicates_h, velocity_h = find_dublicates_hard(items)

        acceleration = velocity_h - velocity

        f.write(f"""N = {n} | O(n^2): {velocity_h:.6f}с. | O(n):{velocity:.6f}с. | Ускорение:{acceleration:.6f}с.\n""")