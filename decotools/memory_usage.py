import tracemalloc

def trace_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        snapshot_before = tracemalloc.take_snapshot()

        result = func(*args, **kwargs)

        snapshot_after = tracemalloc.take_snapshot()
        tracemalloc.stop()

        top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')
        total = sum(stat.size_diff for stat in top_stats)
        print(f"{func.__name__} memory usage: {total / 1024:.2f} KiB")

        return result
    return wrapper