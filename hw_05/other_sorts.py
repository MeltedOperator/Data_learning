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

def sorted_sort(arr):
    sorted(arr)
     

sizes = [1000,5000,10000,50000,100000,500000,1000000]
sorts = [(heap_sort, None),(bubble_sort,5000), 
         (insertion_sort,5000), (merge_sort,None), (sorted_sort,None)]
header = "Метод Сортировки | N" + " | ".join(map(str,sizes)) + "|\n"
with open('report.md', 'w', encoding='utf-8') as f:
    f.write(header)
    for sort, limit in sorts:
        results = []
        for n in sizes:
            if limit is not None and n > limit:
                results.append(" ------ ")
            else:
                arr = [random.randint(1, 10) for _ in range(n)] 
                time_taken_heap = timeit.timeit(
                stmt="sort(arr.copy())",
                globals={"sort": sort, "arr":arr},
                number=5)
                results.append(f"{time_taken_heap:.3f}с. ")
        line = f"{sort.__name__} | " + " | ".join(results) + "|\n"
        f.write(line)



