from tickets_helpers import load_tickets, benchmark # pyright: ignore[reportMissingImports]

tickets = load_tickets("tickets_sample_1000000.csv")
timestamps = [t['created_time'] for t in tickets]

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1; right = 2 * i + 2 
    if left < n and arr[left] > arr[largest]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Сортировка кучей (in-place, возвращает arr)."""
    # Ваша реализация
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)  # build heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
# Сравните
stats_heap = benchmark(lambda: heap_sort(timestamps.copy()), runs=3)
stats_sorted = benchmark(lambda: sorted(timestamps.copy()), runs=3)

print(f"heap_sort: {stats_heap['mean']:.3f} сек")
print(f"sorted():  {stats_sorted['mean']:.3f} сек")