import numpy as np 
vector_row = np.array([[1, -5, 3,2,4]])
vector_column = np.array([[1], [2], [3],[4]])
print (vector_column.shape)
print (vector_row.shape)

from numpy.linalg import norm
new_vector = vector_row.T
print (new_vector)
norm_1 = norm(new_vector, 1)

norm_2 = norm(new_vector,2)
norm_inf = norm(new_vector, np.inf)
print("l1 is : %.lf" %norm_1)
print ("l2 is : %.lf"%norm_2)
print ("l_lnf is : %.lf "%norm_inf)

from numpy import arccos,dot 
v = np.array([[10,9,3]])
w = np.array([[2,5,12]])
theta = arccos (dot(v,w.T) / (norm(v) * norm(w)))
print (theta)
#cross product 
v = np.array([[0,2,0]])
w = np.array([[1,2,1]])
print(np.cross(v,w))

