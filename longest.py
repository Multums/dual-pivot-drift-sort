"""Dual Pivot Drift Sort - longest version (ascending order).

Every step of the algorithm is a separate, named method.

Author: Maciej "Multum" Kuzma
"""


class DualPivotDriftSort:
    """Ascending Dual Pivot Drift Sort that works in place."""

    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)
        self.left_pivot = None
        self.right_pivot = None
        self.passes = 0
        self.swaps = 0

    def find_pivot_positions(self):
        """Return the positions of the minimum and the maximum value."""
        minimum_position = 0
        maximum_position = 0
        for position in range(1, self.size):
            value = self.numbers[position]
            if value < self.numbers[minimum_position]:
                minimum_position = position
            if value > self.numbers[maximum_position]:
                maximum_position = position
        return minimum_position, maximum_position

    def place_pivots(self, minimum_position, maximum_position):
        """Move the minimum to the first cell and the maximum to the last."""
        last_position = self.size - 1
        self.swap(0, minimum_position)
        if maximum_position == 0:
            # The maximum was in the first cell and has just been moved
            # to the place where the minimum used to be.
            maximum_position = minimum_position
        self.swap(last_position, maximum_position)
        self.left_pivot = self.numbers[0]
        self.right_pivot = self.numbers[last_position]

    def distance_to_left_pivot(self, value):
        return value - self.left_pivot

    def distance_to_right_pivot(self, value):
        return self.right_pivot - value

    def drifts_left(self, value):
        """True when the value is closer to the minimum than to the maximum.

        Equal distances drift right.
        """
        return self.distance_to_left_pivot(value) < self.distance_to_right_pivot(value)

    def swap(self, first_position, second_position):
        self.numbers[first_position], self.numbers[second_position] = (
            self.numbers[second_position],
            self.numbers[first_position],
        )

    def drift_pass(self):
        """Run one pass over the inner cells. Return True if anything moved."""
        something_moved = False
        for position in range(1, self.size - 1):
            current_value = self.numbers[position]
            if self.drifts_left(current_value):
                neighbour_position = position - 1
                out_of_order = current_value < self.numbers[neighbour_position]
            else:
                neighbour_position = position + 1
                out_of_order = current_value > self.numbers[neighbour_position]
            if out_of_order:
                self.swap(position, neighbour_position)
                self.swaps += 1
                something_moved = True
        self.passes += 1
        return something_moved

    def sort(self):
        """Sort the list in place and return it."""
        if self.size < 2:
            return self.numbers
        minimum_position, maximum_position = self.find_pivot_positions()
        self.place_pivots(minimum_position, maximum_position)
        keep_going = True
        while keep_going:
            keep_going = self.drift_pass()
        return self.numbers


def dual_pivot_drift_sort(numbers):
    """Sort the list in place in ascending order and return it."""
    return DualPivotDriftSort(numbers).sort()


if __name__ == "__main__":
    data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
    print("Before:", data)
    sorter = DualPivotDriftSort(data)
    sorter.sort()
    print("After: ", data)
    print("Passes:", sorter.passes, "Swaps:", sorter.swaps)
