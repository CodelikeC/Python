#Name : Nguyễn Đức Trí 
#Troy ID : 1677467 
#Do problem 3 in page 188

import numpy as np 

array_2d = ([[1, 3, 5],
            [7, 8, 9],
            [11, 13, 15]])
file_name = "array_data.csv"

np.savetxt(file_name,array_2d, delimiter=",")

print ("array save to", file_name)
read_array = np.genfromtxt(file_name, delimiter=",")
print ("array read from", file_name,":\n", read_array)
