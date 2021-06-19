import numpy as np
s=1

for i in range(1,20):
    s=np.lcm(i,s)
print(s)