
from tickets_helpers_lite import load_tickets, benchmark 

tickets_file = r"c:\Users\tata2\Desktop\hw_05\hw_05\tickets_sample_1000000.csv"
tickets = load_tickets(tickets_file)
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

    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)  # build 
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def sorted_sort(arr):
    sorted(arr)
# Сравните
stats_heap = benchmark(lambda: heap_sort(timestamps.copy()), runs=3)
stats_sorted = benchmark(lambda: sorted_sort(timestamps.copy()), runs=3)

with open("report.md", "a", encoding="utf-8") as f:

    f.write("Для миллиона билетов!")

    f.write(f"heap_sort: {stats_heap['mean']:.3f} сек \n")

    f.write(f"sorted():  {stats_sorted['mean']:.3f} сек \n")

    acceleration = stats_heap["mean"] / stats_sorted["mean"]
    f.write(f"{acceleration} во сколько раз sorted быстрее") 
