#Name : Nguyễn Đức Trí 
#Troy ID : 1677467 

#assignment. 

#problem 1 in page 153 

def my_bin_2_dec(b):
    d = 0
    for i, bit in enumerate(reversed(b)):
        d += bit * (2 ** i)
    return d

# Test cases
print ("Print the output")
print(my_bin_2_dec([1, 1, 1]))           # Output: 7
print(my_bin_2_dec([1, 0, 1, 0, 1, 0, 1]))# Output: 85
print(my_bin_2_dec([1]*25)) #output : 33554431 
    

