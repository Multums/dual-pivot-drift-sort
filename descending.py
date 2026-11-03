"""Dual Pivot Drift Sort - descending order.

This is the mirror image of the ascending version: the maximum goes to
the first cell, the minimum to the last cell, and elements drift toward
the pivot they are closer to.

Author: Maciej "Multum" Kuzma
"""


def dual_pivot_drift_sort_descending(numbers):
    """Sort the list in place in descending order and return it."""
    n = len(numbers)
    if n < 2:
        return numbers

    # Step 1: find the maximum and minimum (the two pivots).
    max_pos = 0
    min_pos = 0
    for i in range(1, n):
        if numbers[i] > numbers[max_pos]:
            max_pos = i
        if numbers[i] < numbers[min_pos]:
            min_pos = i

    # Step 2: put the maximum at the start and the minimum at the end.
    numbers[0], numbers[max_pos] = numbers[max_pos], numbers[0]
    if min_pos == 0:
        min_pos = max_pos
    numbers[n - 1], numbers[min_pos] = numbers[min_pos], numbers[n - 1]

    high = numbers[0]
    low = numbers[n - 1]

    # Steps 3-6: elements closer to the maximum drift left,
    # all others (also on a tie) drift right.
    changed = True
    while changed:
        changed = False
        for i in range(1, n - 1):
            left_distance = high - numbers[i]
            right_distance = numbers[i] - low
            if left_distance < right_distance:
                if numbers[i] > numbers[i - 1]:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                    changed = True
            else:
                if numbers[i] < numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    changed = True

    return numbers


if __name__ == "__main__":
    data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
    print("Before:", data)
    dual_pivot_drift_sort_descending(data)
    print("After: ", data)
