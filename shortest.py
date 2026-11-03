"""Dual Pivot Drift Sort - shortest version (ascending order).

Author: Maciej "Multum" Kuzma
"""


def dual_pivot_drift_sort(a):
    n = len(a)
    if n < 2:
        return a
    lo = min(range(n), key=a.__getitem__)
    a[0], a[lo] = a[lo], a[0]
    hi = max(range(n), key=a.__getitem__)
    a[-1], a[hi] = a[hi], a[-1]
    mid = a[0] + a[-1]
    changed = True
    while changed:
        changed = False
        for i in range(1, n - 1):
            j = i - 1 if 2 * a[i] < mid else i + 1
            if (a[j] - a[i]) * (j - i) < 0:
                a[i], a[j] = a[j], a[i]
                changed = True
    return a


if __name__ == "__main__":
    data = [5, -3, 0, 8, 5, -10, 2, 8, 1, -1]
    print("Before:", data)
    print("After: ", dual_pivot_drift_sort(data))
