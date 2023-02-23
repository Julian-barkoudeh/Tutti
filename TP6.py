import numpy as np 

epsilon  = np.float64(0.1)
un = np.float64(1)
cpt = 0
while(un + epsilon != 1):
    epsilon = np.float64(epsilon/10)
    cpt+=1
    print(epsilon)
print(cpt)
