import numpy as np 

#create a sample matrix 
matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])

#split the matrix into two sub_matrix 
split_matrices = np.hsplit(matrix, 2)

#print the split matrices // 
for i, sub_matrix in enumerate (split_matrices) :
    print(f"Sub-matrix {i+1} :\n{sub_matrix}\n")
