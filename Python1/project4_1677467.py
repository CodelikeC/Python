# do problem 4 in page 88 

#Write a function my_make_size10(x) where x is an array, and output is the first 10 elements of x if
#x has more than 10 elements, and output is the array x padded with enough zeros to make it length
#10 if x has less than 10 elements.

def my_make_size10(x):
    size10 = list(x)[:10] + [0] * (10 - len(x))
    return size10

# Output: [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
print(my_make_size10(range(1, 2)))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_make_size10(range(1, 15)))

# Output: [3, 6, 13, 4, 0, 0, 0, 0, 0, 0]
print(my_make_size10([3, 6, 13, 4, 0, 0, 0, 0, 0, 0]))
