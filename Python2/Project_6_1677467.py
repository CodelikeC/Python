#Do problem 4 in page 116 
#name : Nguyen Duc Tri 

 
print ("Problem 4")
print ("page 116")
def my_n_choose_k(n, k):
    if n == k or k == 0:
        return 1
    else:
        return my_n_choose_k(n-1, k) + my_n_choose_k(n-1, k-1)

print(my_n_choose_k(10, 1))  # Output: 10
print(my_n_choose_k(10, 10))  # Output: 1
print(my_n_choose_k(10, 3))  # Output: 120 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
