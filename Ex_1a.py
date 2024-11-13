import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = arr.reshape(-2,1)
b = arr.reshape(-2,1)
sarr = np.vstack([a,b])
print(sarr)