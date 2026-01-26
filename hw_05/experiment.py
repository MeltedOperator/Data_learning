# # from tickets_helpers import load_tickets, benchmark

# tickets = load_tickets("tickets_sample_1000000.csv")
# timestamps = [t['created_time'] for t in tickets]

# # Сравните
# # stats_heap = benchmark(lambda: heap_sort(timestamps.copy()), runs=3)
# stats_sorted = benchmark(lambda: sorted(timestamps.copy()), runs=3)

# print(f"heap_sort: {stats_heap['mean']:.3f} сек")
# print(f"sorted():  {stats_sorted['mean']:.3f} сек")