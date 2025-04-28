# Name : Nguyen Duc Tri 
# Troy ID : 1677467 
#problem 4 : 
#Write a function my_split_matrix(m), where m is an array, the output is a list [m1, m2] where m1 is
#the left half of m, and m2 is the right half of m. In the case where there is an odd number of columns,
#the middle column should go to m1. Assume that m has at least two columns



import numpy as np

def my_split_matrix(m):
    num_cols = m.shape[1]
    split_point = num_cols // 2
    
    m1 = m[:, :split_point]
    m2 = m[:, split_point:]
    
    return m1, m2

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1, m2 = my_split_matrix(m)
print("m1 =", m1)
print("m2 =", m2)
# Output:
# m1 = array([[1, 2],
#             [4, 5],
#             [7, 8]])
# m2 = array([[3],
#             [6],
#             [9]])

m = np.ones((5, 5))
m1, m2 = my_split_matrix(m)
print("m1 =", m1)
print("m2 =", m2)
# Output:
# m1 = array([[1., 1., 1.],
#             [1., 1., 1.],
#             [1., 1., 1.],
#             [1., 1., 1.],
#             [1., 1., 1.]])
# m2 = array([[1., 1.],
#             [1., 1.],
#             [1., 1.],
#             [1., 1.],
#             [1., 1.]])










