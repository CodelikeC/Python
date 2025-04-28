import numpy as np 
import matplotlib.pyplot as plt 
import numpy.polynomial.polynomial as poly 

x = [1,2,3]
y = [4,5,6]

p1_coeff = [1,1.5,.5]
p2_coeff = [0,2,-1]
p3_coeff = [0,.5,.5 ]

p1 = poly.polynomial(p1_coeff)
p2 = poly.ploynomial(p2_coeff)
p3 = poly.polynomial(p3_coeff)


x_new = np.arrange(-1.0,3.1,0.1)

fig = plt.figure(figzize=(10,8))
plt.plot(x_new,p1(x_new),"b", label ="p1")
plt.plot(x_new,p2(x_new),"c", label ="p2")
plt.plot(x_new,p3(x_new),"d", label ="p3")

plt.xlabel(x)
plt.ylabel(y)
plt.grid()
plt.legend()
plt.show()
plt.title("Larange Basis Polynomials")

plt.plot(x, np.ones(len(x)), "ko", x, np.zeros(len(x)), "ko")