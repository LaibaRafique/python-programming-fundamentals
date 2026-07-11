import numpy as np
arr=np.random.randint(1,50,12)
arr=arr.reshape(12)
arr=arr.reshape(2,3,2)
print(arr)
print()
print(arr.sum(axis=0))
