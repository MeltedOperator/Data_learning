import random

def heapify(arr, n, i):

    """строит heap благодаря определению большей и меньшей части,
    после чего "просеивает" элементы. Сам по себе heap это бинарное дерево,
    где сверху минимальные числа и снизу самые большие. Родитель важнее детей"""

    largest = i

    left = 2 * i + 1; right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right

    if largest != i: 

        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):

    """Сортировка кучей (in-place, возвращает arr)."""

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)  # build heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def test_heap_sort():
    
    """Тесты для heap"""

    # Пустой массив
    assert heap_sort([]) == []
    
    # Один элемент
    assert heap_sort([42]) == [42]
    
    # Уже отсортирован
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Обратный порядок
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Случайные данные
    data = [random.randint(0, 10000) for _ in range(1000)]
    assert heap_sort(data.copy()) == sorted(data)
    
    print("✓ Все тесты пройдены!")

test_heap_sort()