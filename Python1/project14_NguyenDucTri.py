#Nguyen Duc Tri, problem 3 in page 261.  
import numpy as np 

def my_is_orthogonal(v1, v2, tol):
    angle = np.arccos(np.dot(v1.T, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    if np.abs(np.pi/2 - angle) < tol:
        return 1
    else:
        return 0
a = np.array([[1], [0.001]])
b = np.array([[0.001], [1]])
print(my_is_orthogonal(a, b, 0.01))   # Output: 1
print(my_is_orthogonal(a, b, 0.001))  # Output: 0
a = np.array([[1], [0.001]])
b = np.array([[1], [1]])
print(my_is_orthogonal(a, b, 0.01))   # Output: 1
a = np.array([[1], [1]])
b = np.array([[-1], [1]])
print(my_is_orthogonal(a, b, 1e-10))  # Output: 1 


