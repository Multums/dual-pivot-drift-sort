"""Dual Pivot Drift Sort - simplest version (ascending order).

Author: Maciej "Multum" Kuzma
"""


def dual_pivot_drift_sort(numbers):
    """Sort the list in place in ascending order and return it."""
    n = len(numbers)
    if n < 2:
        return numbers

    # Step 1: find the minimum and maximum (the two pivots).
    min_pos = 0
    max_pos = 0
    for i in range(1, n):
        if numbers[i] < numbers[min_pos]:
            min_pos = i
        if numbers[i] > numbers[max_pos]:
            max_pos = i

    # Step 2: put the minimum at the start and the maximum at the end.
    numbers[0], numbers[min_pos] = numbers[min_pos], numbers[0]
    if max_pos == 0:
        max_pos = min_pos
    numbers[n - 1], numbers[max_pos] = numbers[max_pos], numbers[n - 1]

    low = numbers[0]
    high = numbers[n - 1]

    # Steps 3-6: let every element drift toward the closer pivot
    # until a whole pass makes no swap.
    changed = True
    while changed:
        changed = False
        for i in range(1, n - 1):
            left_distance = numbers[i] - low
            right_distance = high - numbers[i]
            if left_distance < right_distance:
                if numbers[i] < numbers[i - 1]:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                    changed = True
            else:
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    changed = True

    return numbers


if __name__ == "__main__":
    data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
    print("Before:", data)
    dual_pivot_drift_sort(data)
    print("After: ", data)
