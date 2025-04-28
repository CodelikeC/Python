#problem 9 in 217 

#Name : Nguyen Duc Tri 
import numpy as np 
import matplotlib.pyplot as plt
def my_poly_plotter(n, x_values):
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    for k in range(1, n+1):
        pk = np.power(x_values, k)
        plt.plot(x_values, pk, label=f'$p_{k}(x) = x^{k}$')
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.title(f'Polynomials $p_k(x) = x^k$ for k=1 to {n}')
    plt.legend()
    plt.grid(True)
    plt.show()
x = np.linspace(-1, 1, 200)
my_poly_plotter(5, x)
