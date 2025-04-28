
#name : Nguyen Duc Tri 

import numpy as np

def my_within_tolerance(A, a, tol):
    indices = []
    for i, val in enumerate(A):
        if abs(val - a) < tol:
            indices.append(i)
    return indices

print(my_within_tolerance([0, 1, 2, 3], 1.5, 0.75))
# Output: [1, 2]

print(my_within_tolerance(np.arange(0, 1.01, 0.01), 0.5, 0.03))
# Output: [47, 48, 49, 50, 51, 52]
