# Dual Pivot Drift Sort

An original sorting algorithm by **Maciej "Multum" Kuźma**, implemented in Python.

Dual Pivot Drift Sort uses two pivots, the minimum and the maximum of the list.
After the pivots are placed at the ends, every other element "drifts" toward the
pivot it is closer to by swapping with its neighbour. Passes repeat until one
pass makes no swap. The idea combines local neighbour swaps (as in bubble sort)
with a global decision based on the pivots (as in quicksort).

## How it works

1. **Find the pivots.** Scan the list for the minimum and the maximum.
2. **Place the pivots.** Move the minimum to the first cell and the maximum to the last.
   They are now in their final positions.
3. **Measure distances.** For each inner element:
   `left distance = value - min`, `right distance = max - value`.
4. **Choose a direction.** Closer to `min` → drift left. Otherwise (also on a tie) → drift right.
5. **Swap locally.** A left-drifting element swaps with its left neighbour if that
   neighbour is bigger. A right-drifting element swaps with its right neighbour if
   that neighbour is smaller.
6. **Repeat** full passes until a pass makes no swap.

### Pseudocode

```text
ALGORITHM DualPivotDriftSort(A, n)
    find minPos and maxPos of the minimum and maximum
    swap A[0] with A[minPos]
    if maxPos = 0 then maxPos ← minPos
    swap A[n-1] with A[maxPos]
    min ← A[0];  max ← A[n-1]

    changed ← TRUE
    while changed
        changed ← FALSE
        for i ← 1 to n-2
            if A[i] - min < max - A[i]
                if A[i] < A[i-1]: swap A[i], A[i-1]; changed ← TRUE
            else
                if A[i] > A[i+1]: swap A[i], A[i+1]; changed ← TRUE
```

### Why the result is always sorted

Assume a pass made no swap but two neighbours are still in the wrong order, `a > b`.
If `a` drifts right, it would have swapped with `b`. If `a` drifts left, it is closer
to the minimum, so `b` (which is even smaller) also drifts left and would have
swapped with `a`. Both cases contradict "no swap", so the list is sorted.
The pivots never move: nothing is smaller than the first cell or bigger than the last.

## Files

| File | Order | Description |
| --- | --- | --- |
| `simplest.py` | ascending | Clean, readable reference version |
| `shortest.py` | ascending | Compact version |
| `longest.py` | ascending | Every step is a named method; counts passes and swaps |
| `educational.py` | ascending | Detailed comments and a step-by-step printout |
| `descending.py` | descending | Mirror version: maximum first, minimum last |
| `optimized.py` | both | Faster bidirectional version, `descending=True` for descending order |
| `test_sorting.py` | | Tests for every version |
| `benchmark.py` | | Speed comparison |

## Usage

Requires Python 3.8+. No third-party dependencies.

```sh
python simplest.py
python educational.py
python descending.py
```

In your own code:

```python
from optimized import dual_pivot_drift_sort

data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
dual_pivot_drift_sort(data)                   # [-10, -3, -1, 0, 1, 2, 5, 5, 8, 8]
dual_pivot_drift_sort(data, descending=True)  # [8, 8, 5, 5, 2, 1, 0, -1, -3, -10]
```

Every function sorts the list **in place** and also returns it.
The algorithm works on numbers (integers and floats), because it computes distances.

## Optimized version

`optimized.py` keeps the same idea and gives the same result, with two changes:

- **Alternating passes.** In the original version a left-drifting element moves only
  one cell per pass. Forward and backward passes now alternate, so elements drifting
  in either direction can travel all the way in a single pass.
- **One comparison instead of two distances.** `value - min < max - value` is the
  same as `2 * value < min + max`.

## Complexity

| | Value |
| --- | --- |
| Time, worst case | O(n²) |
| Time, best case (already sorted) | O(n) |
| Extra memory | O(1), in place |
| Stable | No (placing the pivots can reorder equal values) |

## Benchmark

`python benchmark.py`, list of 1000 numbers, best of 3 runs, milliseconds.
Measured on one Windows PC with Python 3.13; your numbers will differ.

| Algorithm | random | nearly sorted | reversed | few distinct |
| --- | ---: | ---: | ---: | ---: |
| Drift Sort (original) | 102.19 | 77.43 | 119.98 | 75.01 |
| Drift Sort (optimized) | 44.17 | 2.11 | 90.81 | 39.74 |
| Bubble sort | 34.47 | 20.60 | 47.12 | 30.88 |
| Python `list.sort()` | 0.03 | 0.01 | 0.00 | 0.02 |

The optimized version is about 2× faster than the original on random data and
about 10× faster than bubble sort on nearly sorted data. Like every O(n²) algorithm,
it is far slower than Python's built-in O(n log n) sort on large lists. Its strengths
are simplicity, in-place work and data that is already almost sorted.

## Tests

```sh
python test_sorting.py
```

The tests cover empty and one-element lists, negative numbers, floats, duplicates,
already sorted and reversed input, every permutation of lists up to 6 elements, and
about a thousand random lists. They also check that sorting happens in place.

## Author

**Maciej "Multum" Kuźma**. Original algorithm design and documentation.

## License

[MIT](LICENSE). You may use, copy and modify this code if you keep the copyright notice.
