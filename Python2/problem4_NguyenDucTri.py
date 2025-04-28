#Troy ID : 1677467 #Name : Nguyen Duc Tri 
#problem 4
import numpy as np

# Define the matrix A
A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]])

# Define the initial vector
v = np.array([1, 1, 1])

# Number of iterations
iterations = 8

# Power method
for i in range(iterations):
    # Multiply A with the vector
    Av = np.dot(A, v)
    
    # Normalize the resulting vector
    v = Av / np.linalg.norm(Av)

# Compute the eigenvalue
eigenvalue = np.dot(np.dot(A, v), v) / np.dot(v, v)

print("Largest eigenvalue after", iterations, "iterations:", eigenvalue)
print("Corresponding eigenvector:", v)

