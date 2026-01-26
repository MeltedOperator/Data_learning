import timeit
import random

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1; right = 2 * i + 2
    if left < n and arr[left] > arr[largest]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)  # build heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return arr 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]; j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]; j -= 1
        arr[j + 1] = key
    return arr 

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []; i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result 

def sorted1(arr):
    sorted(arr)
     

sizes = [1000,5000,10000,50000,100000,500000,1000000]
for n in sizes:
    # Генерация данных
    arr = [random.randint(1, 10) for _ in range(n)]
    time_taken_heap = timeit.timeit(
    stmt="heap_sort(arr.copy())",
    globals={"heap_sort": heap_sort, "arr":arr},
    number=5)
    print(f"средняя время heap_sort: {time_taken_heap}с")

    if n < 10000:
        time_taken_insert = timeit.timeit(
        stmt="insertion_sort(arr.copy())",
        globals={"insertion_sort": insertion_sort, "arr":arr},
        number=5)
        print(f"средняя время insertion_sort: {time_taken_insert}с")

        time_taken_bubble = timeit.timeit(
        stmt="bubble_sort(arr.copy())",
        globals={"bubble_sort": bubble_sort, "arr":arr},
        number=5)
        print(f"средняя время bubble_sort: {time_taken_bubble}с")

    time_taken_merge = timeit.timeit(
    stmt="merge_sort(arr.copy())",
    globals={"merge_sort": merge_sort, "arr":arr},
    number=5)
    print(f"средняя время merge_sort: {time_taken_merge}с")

    time_taken_sorted = timeit.timeit(
    stmt="sorted1(arr.copy())",
    globals={"sorted1": sorted1, "arr":arr},
    number=5)
    print(f"средняя время sorted1: {time_taken_sorted}с")

