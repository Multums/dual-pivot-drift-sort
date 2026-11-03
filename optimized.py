"""Dual Pivot Drift Sort - optimized (bidirectional) version.

Same idea as the original algorithm, with two improvements:

1. Passes alternate direction. A forward pass carries elements that
   drift right all the way to their place; a backward pass does the same
   for elements that drift left. In the original version an element that
   drifts left could move only one cell per pass.
2. The drift direction is decided with one comparison against the sum of
   the pivots (2 * value < low + high) instead of computing two distances.

The result is identical to the original version, only reached faster.

Author: Maciej "Multum" Kuzma
"""


def dual_pivot_drift_sort(numbers, descending=False):
    """Sort the list in place and return it.

    With descending=True the list is sorted in descending order.
    """
    n = len(numbers)
    if n < 2:
        return numbers

    min_pos = 0
    max_pos = 0
    for i in range(1, n):
        value = numbers[i]
        if value < numbers[min_pos]:
            min_pos = i
        elif value > numbers[max_pos]:
            max_pos = i

    numbers[0], numbers[min_pos] = numbers[min_pos], numbers[0]
    if max_pos == 0:
        max_pos = min_pos
    last = n - 1
    numbers[last], numbers[max_pos] = numbers[max_pos], numbers[last]

    pivot_sum = numbers[0] + numbers[last]
    forward = range(1, last)
    backward = range(last - 1, 0, -1)

    changed = True
    while changed:
        changed = False
        for i in forward:
            value = numbers[i]
            if 2 * value < pivot_sum:
                if value < numbers[i - 1]:
                    numbers[i] = numbers[i - 1]
                    numbers[i - 1] = value
                    changed = True
            elif value > numbers[i + 1]:
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = value
                changed = True
        if not changed:
            break

        changed = False
        for i in backward:
            value = numbers[i]
            if 2 * value < pivot_sum:
                if value < numbers[i - 1]:
                    numbers[i] = numbers[i - 1]
                    numbers[i - 1] = value
                    changed = True
            elif value > numbers[i + 1]:
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = value
                changed = True

    if descending:
        numbers.reverse()
    return numbers


if __name__ == "__main__":
    data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
    print("Before:     ", data)
    print("Ascending:  ", dual_pivot_drift_sort(data[:]))
    print("Descending: ", dual_pivot_drift_sort(data[:], descending=True))
