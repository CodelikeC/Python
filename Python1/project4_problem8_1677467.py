
#name : Nguyễn Đức Trí 
# Do problem 8 in page 88 
print ("===problem 8===")

import cmath #like include <cmath> or #include <algorithm> in C++

def my_n_roots(a, b, c):
    discriminant = b**2 - 4*a*c  # Calculate the discriminant
    
    if discriminant > 0: #like if () {} in C++
        n_roots = 2
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        roots = [root1, root2]
    elif discriminant < 0: #like else if(){} in C++
        n_roots = -2
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        roots = [root1, root2]
    else:
        n_roots = 1
        root = -b / (2*a)
        roots = [root]
    
    return n_roots, roots

n_roots, r = my_n_roots(1, 0, -9)
print(n_roots, r)  # Output: n_roots = 2, r = [3, -3]

n_roots, r = my_n_roots(3, 4, 5)
print(n_roots, r)  # Output: n_roots = -2, r = [(-0.6667+1.1055j), (-0.6667-1.1055j)]

n_roots, r = my_n_roots(2, 4, 2)
print(n_roots, r)  # Output: n_roots = 1, r = [1]

    
