#Name : Nguyen Duc Tri 


#Do problem 3 in page 102 

print ("Problem 3 ")
print ("Page 102")


import numpy as np 
def my_n_max (x,n): 
    #write a function in here 

    # Sort the list in descending order
    sorted_x = sorted(x, reverse=True)
    
    # Return the first n elements
    return sorted_x[:n]

x = [7, 9, 10, 5, 8, 3, 4, 6, 2, 1]
n = 3

out = my_n_max(x, n)
print(out)  # Output: [10, 9, 8]
  
    
     
    
