#!/usr/bin/env python3
"""
tickets_helpers_lite.py — Минимальный набор для работы с билетами Avtobys.

Этот файл содержит ТОЛЬКО базовые функции:
- Загрузка CSV
- Парсинг типов
- Измерение времени

Остальные функции (group_by, count_by, find_duplicates и т.д.)
вы должны реализовать САМИ как часть домашних заданий!

Только стандартные библиотеки Python!
"""

import csv
import time
from datetime import datetime
from typing import List, Dict, Any, Callable, Optional, Iterator
from functools import wraps


# ============================================================================
# ЗАГРУЗКА ДАННЫХ
# ============================================================================

def load_tickets(filename: str) -> List[Dict[str, Any]]:
    """
    Загрузить билеты из CSV в список словарей.
    
    Пример:
        tickets = load_tickets("tickets_sample_100000.csv")
        print(f"Загружено: {len(tickets)} билетов")
        print(tickets[0])  # Первый билет
    
    Возвращает:
        Список словарей. Каждый словарь — один билет с полями:
        - created_time: datetime
        - cost: int
        - route_id: int
        - bus_id: int
        - и другие...
    """
    tickets = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticket = parse_ticket(row)
            tickets.append(ticket)
    return tickets


def load_tickets_lazy(filename: str) -> Iterator[Dict[str, Any]]:
    """
    Ленивая загрузка билетов (генератор).
    Не загружает всё в память сразу — экономит RAM.
    
    Пример:
        for ticket in load_tickets_lazy("big_file.csv"):
            if ticket['cost'] > 1000:
                print(ticket)
                break
    """
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield parse_ticket(row)


def parse_ticket(row: Dict[str, str]) -> Dict[str, Any]:
    """
    Преобразовать строку CSV в типизированный словарь.
    
    Преобразования:
    - created_time → datetime
    - cost → int
    - *_id → int или None
    """
    return {
        'created_time': _parse_datetime(row.get('created_time')),
        'cost': _parse_int(row.get('cost'), 0),
        'trip_id': _parse_int(row.get('trip_id')),
        'bus_id': _parse_int(row.get('bus_id')),
        'route_id': _parse_int(row.get('route_id')),
        'bus_stop_id': _parse_int(row.get('bus_stop_id')),
        'source_system': row.get('source_system', ''),
        'payment_type': row.get('payment_type', ''),
        'payment_channel': row.get('payment_channel', ''),
        'locality_code': row.get('locality_code', ''),
        'passenger_id': _parse_int(row.get('passenger_id')),
        'conductor_id': _parse_int(row.get('conductor_id')),
        'original_id': row.get('original_id', ''),
    }


def _parse_datetime(value: Optional[str]) -> Optional[datetime]:
    """Внутренняя: парсинг datetime из строки."""
    if not value:
        return None
    try:
        if '.' in value:
            return datetime.strptime(value[:26], '%Y-%m-%d %H:%M:%S.%f')
        else:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None


def _parse_int(value: Optional[str], default: Optional[int] = None) -> Optional[int]:
    """Внутренняя: парсинг int из строки."""
    if not value or value == '\\N' or value == 'NULL':
        return default
    try:
        return int(value)
    except ValueError:
        return default


# ============================================================================
# ИЗМЕРЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ
# ============================================================================

def measure_time(func: Callable) -> Callable:
    """
    Декоратор для измерения времени выполнения функции.
    
    Пример:
        @measure_time
        def my_sort(data):
            return sorted(data)
        
        result = my_sort(tickets)
        # Выведет: my_sort: 0.1234 сек
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.4f} сек")
        return result
    return wrapper


def benchmark(func: Callable, *args, runs: int = 5, **kwargs) -> dict:
    """
    Запустить функцию несколько раз и вернуть статистику.
    
    Пример:
        stats = benchmark(sorted, my_list, runs=10)
        print(f"Среднее: {stats['mean']:.4f} сек")
        print(f"Мин: {stats['min']:.4f} сек")
        print(f"Макс: {stats['max']:.4f} сек")
    
    Возвращает:
        dict с ключами: runs, times, mean, min, max, total, last_result
    """
    times = []
    result = None
    
    for _ in range(runs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    
    return {
        'runs': runs,
        'times': times,
        'mean': sum(times) / len(times),
        'min': min(times),
        'max': max(times),
        'total': sum(times),
        'last_result': result
    }


# ============================================================================
# ДЕМОНСТРАЦИЯ
# ============================================================================

if __name__ == "__main__":
    print("=== tickets_helpers_lite.py ===\n")
    
    print("Это МИНИМАЛЬНАЯ версия. Содержит только:")
    print("  - load_tickets(filename) — загрузка CSV")
    print("  - load_tickets_lazy(filename) — ленивая загрузка")
    print("  - measure_time — декоратор")
    print("  - benchmark(func, *args, runs=5) — статистика времени")
    print()
    
    print("Остальное вы реализуете САМИ в домашних заданиях:")
    print("  - count_by(tickets, key)")
    print("  - sum_by(tickets, key, value_key)")
    print("  - group_by(tickets, key)")
    print("  - find_duplicates(tickets, key)")
    print("  - top_n(counts, n)")
    print()
    
    print("Пример использования:")
    print("  from tickets_helpers_lite import load_tickets, benchmark")
    print("  tickets = load_tickets('tickets_sample_100000.csv')")
    print("  stats = benchmark(sorted, tickets, key=lambda t: t['cost'], runs=3)")
    print("  print(f'Среднее: {stats[\"mean\"]:.4f} сек')")
