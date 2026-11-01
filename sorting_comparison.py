
import random
import time
import tracemalloc
import statistics
import csv


# Merge Sort: divide the list and merge the sorted halves.
def merge_sort(data):
    if len(data) <= 1:
        return data[:]

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quicksort: partition values around a pivot.
def quick_sort(data):
    if len(data) <= 1:
        return data[:]

    pivot = data[len(data) // 2]

    smaller = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    larger = [x for x in data if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


# Create simulated student assignment scores.
def create_data(size, order):
    rng = random.Random(2026 + size)
    scores = [rng.randint(0, 100) for _ in range(size)]

    if order == "sorted":
        return sorted(scores)
    elif order == "reverse sorted":
        return sorted(scores, reverse=True)

    return scores


# Measure runtime and peak memory separately.
def test_algorithm(algorithm, data):
    times = []

    for _ in range(7):
        start = time.perf_counter()
        result = algorithm(data)
        elapsed = (time.perf_counter() - start) * 1000

        assert result == sorted(data)
        times.append(elapsed)

    tracemalloc.start()
    algorithm(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return (
        round(statistics.median(times), 3),
        round(peak / 1024, 1)
    )


# Compare both algorithms on different datasets.
results = []

for size in [100, 1000, 5000]:
    for order in ["sorted", "reverse sorted", "random"]:
        data = create_data(size, order)

        for name, algorithm in [
            ("Merge Sort", merge_sort),
            ("Quicksort", quick_sort)
        ]:
            runtime, memory = test_algorithm(algorithm, data)

            results.append([
                name, order, size, runtime, memory
            ])

            print(
                f"{name}: {size} records, {order}, "
                f"{runtime} ms, {memory} KiB"
            )


# Save the results as a CSV file.
with open("performance_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Algorithm", "Input Order", "Records",
        "Execution Time (ms)", "Peak Memory (KiB)"
    ])

    writer.writerows(results)

print("Performance results saved successfully.")
