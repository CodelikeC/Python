#assume that we have the folowing aray definition:m = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
# do indexing elements 7 
# do indexing elements 14 
# do slicing [6,7]
# do slicing [7,12]
# do slicing [[3,4], [8,9]] 

# Troy ID : 1677467 
# Name : Nguyen Duc Tri 

# ==Problem 1:==
print("Problem 1 is:")

# insert 2 at index 1
list_a = [1, 8, 9, 15]
list_a.insert(0, 2)
print(list_a)

# append 4
list_a.append(4)
print(list_a)
print("\n")

# ==Problem 2:==
print("Problem 2:")

import numpy as np 
m = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])

# ==3.1.
print("Ex 3.1:")
element_7 = m[1, 2] 
print(element_7)

# ==3.2.
print("Ex 3.2 is:")
element_14 = m[2, 4]
print(element_14)

# ==3.3.
print("Ex 3.3 is:")
slicing_6_7 = m[1, 1:3] 
print(slicing_6_7)

# ==3.4.
print("Ex 3.4 is :")
slicing_7_12 = m[1:3, 2] 
print(slicing_7_12)

# ==3.5.
print("Ex 3.5 is:")
slicing_3_4N8_9 = m[0:2, 3:5] 
print(slicing_3_4N8_9)