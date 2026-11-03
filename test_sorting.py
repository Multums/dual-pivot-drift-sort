"""Tests for every version. Run: python test_sorting.py"""
import random
import unittest

import descending
import educational
import longest
import optimized
import shortest
import simplest

ASCENDING = {
    "simplest": simplest.dual_pivot_drift_sort,
    "shortest": shortest.dual_pivot_drift_sort,
    "longest": longest.dual_pivot_drift_sort,
    "educational": educational.dual_pivot_drift_sort,
    "optimized": optimized.dual_pivot_drift_sort,
}
DESCENDING = {
    "descending": descending.dual_pivot_drift_sort_descending,
    "optimized": lambda numbers: optimized.dual_pivot_drift_sort(numbers, descending=True),
}

FIXED_CASES = [
    [],
    [7],
    [2, 1],
    [1, 2],
    [5, -3, 0, 8, 5, -10, 2, 8, 1, -1],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [4, 4, 4, 4, 4],
    [10, 1, 10, 1, 10, 1],
    [3, 1, 2],
    [1, 3, 2],
    [-5, -1, -3, -2, -4],
    [2.5, -1.25, 0.0, 3.75, 2.5],
    [10**12, -(10**12), 0, 1, -1],
]


def random_cases():
    rng = random.Random(2026)
    cases = []
    for size in range(2, 40):
        for _ in range(25):
            cases.append([rng.randint(-20, 20) for _ in range(size)])
    for size in (100, 250):
        cases.append([rng.randint(-1000, 1000) for _ in range(size)])
        cases.append([rng.randint(0, 3) for _ in range(size)])
    return cases


ALL_CASES = FIXED_CASES + random_cases()


class TestDualPivotDriftSort(unittest.TestCase):
    def check(self, sort, expected_for):
        for case in ALL_CASES:
            data = case[:]
            result = sort(data)
            expected = expected_for(case)
            self.assertEqual(data, expected, case)
            self.assertIs(result, data, "the list must be sorted in place")
            self.assertEqual(sort(data), expected, "sorting twice must not change the result")

    def test_ascending_versions(self):
        for name, sort in ASCENDING.items():
            with self.subTest(version=name):
                self.check(sort, sorted)

    def test_descending_versions(self):
        for name, sort in DESCENDING.items():
            with self.subTest(version=name):
                self.check(sort, lambda case: sorted(case, reverse=True))

    def test_all_permutations_of_small_lists(self):
        from itertools import permutations

        for size in range(1, 7):
            for permutation in permutations(range(size)):
                for name, sort in ASCENDING.items():
                    with self.subTest(version=name, data=permutation):
                        self.assertEqual(sort(list(permutation)), sorted(permutation))

    def test_longest_counts_passes_and_swaps(self):
        sorter = longest.DualPivotDriftSort([3, 2, 1])
        sorter.sort()
        self.assertEqual(sorter.numbers, [1, 2, 3])
        self.assertGreaterEqual(sorter.passes, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
