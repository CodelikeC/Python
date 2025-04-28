#name : Nguyen Duc Tri #Troy ID: 1677467 #problem 8 #277
import numpy as np 
A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]])
eigenvalues , eigenvectors = np.linalg.eig(A)
idx = np.argmax (eigenvalues)
largest_eigenvalue = eigenvalues[idx]
corresponding_eigenvector = eigenvectors[:, idx]
print("eigenvalues:", eigenvalues)
print("eigenvectors:",eigenvectors)
print("largest value:", largest_eigenvalue)
print("corresponding_eigenvector:", corresponding_eigenvector)
