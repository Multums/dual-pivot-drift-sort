"""Compare running times. Run: python benchmark.py

Results depend on the computer, so treat them as a rough comparison.
"""
import random
import time

import optimized
import simplest


def bubble_sort(numbers):
    """Classic bubble sort with early exit, used as a reference point."""
    end = len(numbers) - 1
    changed = True
    while changed:
        changed = False
        for i in range(end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                changed = True
        end -= 1
    return numbers


ALGORITHMS = {
    "Drift Sort (original)": simplest.dual_pivot_drift_sort,
    "Drift Sort (optimized)": optimized.dual_pivot_drift_sort,
    "Bubble sort": bubble_sort,
    "Python list.sort()": lambda numbers: numbers.sort(),
}


def make_inputs(size, rng):
    random_data = [rng.randint(-10_000, 10_000) for _ in range(size)]
    nearly_sorted = sorted(random_data)
    for _ in range(size // 50 or 1):
        i, j = rng.randrange(size), rng.randrange(size)
        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
    return {
        "random": random_data,
        "nearly sorted": nearly_sorted,
        "reversed": sorted(random_data, reverse=True),
        "few distinct": [rng.randint(0, 4) for _ in range(size)],
    }


def measure(sort, data, repeats=3):
    best = float("inf")
    for _ in range(repeats):
        copy = data[:]
        start = time.perf_counter()
        sort(copy)
        best = min(best, time.perf_counter() - start)
        assert copy == sorted(data)
    return best


def main(size=1000):
    rng = random.Random(42)
    print(f"List size: {size} (best of 3 runs, milliseconds)\n")
    header = f"{'Algorithm':<24}" + "".join(f"{name:>15}" for name in make_inputs(10, rng))
    print(header)
    print("-" * len(header))
    inputs = make_inputs(size, rng)
    for name, sort in ALGORITHMS.items():
        row = f"{name:<24}"
        for data in inputs.values():
            row += f"{measure(sort, data) * 1000:>15.2f}"
        print(row)


if __name__ == "__main__":
    main()
