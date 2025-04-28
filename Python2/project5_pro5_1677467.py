#Name : Nguyen Duc Tri 


#do problem 5 in page 102 

import numpy as np

def my_mat_mult(P, Q):
    m, p = P.shape
    p, n = Q.shape
    M = np.zeros((m, n))  # Initialize the result matrix M with zeros

    for i in range(m): #the for loop to check the matrix 
        for j in range(n):
            for k in range(p):
                M[i, j] += P[i, k] * Q[k, j] #matrix M = matrix P * matrixQ

    return M #return the M matrix 

# Test case 1
P = np.ones((3, 3))
result1 = my_mat_mult(P, P)
print(result1)

# Test case 2
P = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
Q = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
result2 = my_mat_mult(P, Q)
print(result2)
