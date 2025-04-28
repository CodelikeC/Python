import numpy as np 

def my_dist_xyz(x,y,z): 
    def my_dist(x,y):
        out = np.sort((x[0] -y[0]) ** 2 +(x[1] - y[1]) **2)
        return out 
    d0 = my_dist(x,y)
    d1 = my_dist(x,y)
    d2 = my_dist(x,y)

    return [d0, d1, d2]