"""Dual Pivot Drift Sort - educational version (ascending order).

Run this file to watch the algorithm work step by step.

Author: Maciej "Multum" Kuzma
"""


def dual_pivot_drift_sort(numbers, show_steps=False):
    """Sort the list in place in ascending order and return it.

    With show_steps=True every important step is printed.
    """
    n = len(numbers)

    # A list with 0 or 1 elements is already sorted.
    if n < 2:
        return numbers

    # ------------------------------------------------------------------
    # Step 1 - find the pivots.
    # The two pivots are the smallest and the largest value in the list.
    # We remember where they are, because we will move them.
    # ------------------------------------------------------------------
    min_pos = 0
    max_pos = 0
    for i in range(1, n):
        if numbers[i] < numbers[min_pos]:
            min_pos = i
        if numbers[i] > numbers[max_pos]:
            max_pos = i
    if show_steps:
        print(f"Step 1: minimum {numbers[min_pos]} at index {min_pos}, "
              f"maximum {numbers[max_pos]} at index {max_pos}")

    # ------------------------------------------------------------------
    # Step 2 - place the pivots.
    # The minimum goes to the first cell and the maximum to the last cell.
    # They are already in their final places and will never move again.
    # ------------------------------------------------------------------
    numbers[0], numbers[min_pos] = numbers[min_pos], numbers[0]
    # Special case: if the maximum was in cell 0, the swap above has just
    # moved it to min_pos, so we must look for it there.
    if max_pos == 0:
        max_pos = min_pos
    numbers[n - 1], numbers[max_pos] = numbers[max_pos], numbers[n - 1]

    low = numbers[0]
    high = numbers[n - 1]
    if show_steps:
        print(f"Step 2: pivots placed -> {numbers}")

    # ------------------------------------------------------------------
    # Steps 3-6 - drift.
    # For every inner element we measure how far it is from each pivot:
    #   left distance  = value - minimum
    #   right distance = maximum - value
    # An element closer to the minimum "drifts" left: it swaps with its
    # left neighbour if that neighbour is bigger.
    # Any other element (also on a tie) drifts right: it swaps with its
    # right neighbour if that neighbour is smaller.
    # We repeat full passes until a pass makes no swap at all.
    # ------------------------------------------------------------------
    pass_number = 0
    changed = True
    while changed:
        changed = False
        pass_number += 1
        for i in range(1, n - 1):
            left_distance = numbers[i] - low
            right_distance = high - numbers[i]

            if left_distance < right_distance:
                # Closer to the minimum -> look left.
                if numbers[i] < numbers[i - 1]:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                    changed = True
            else:
                # Closer to the maximum (or a tie) -> look right.
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    changed = True

        if show_steps:
            state = "swaps made" if changed else "no swaps - done"
            print(f"Pass {pass_number}: {numbers} ({state})")

    # Why is the list sorted now?
    # Suppose two neighbours were still in the wrong order: a > b.
    # If a drifts right, it would have swapped with b.
    # If a drifts left, then b (which is even smaller) also drifts left,
    # so b would have swapped with a.
    # Either way the last pass would have made a swap - a contradiction.
    return numbers


if __name__ == "__main__":
    data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
    print("Start:", data)
    dual_pivot_drift_sort(data, show_steps=True)
    print("Result:", data)
