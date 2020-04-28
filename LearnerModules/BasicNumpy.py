import numpy as np;
import pandas as pd
arr1 = [25, 56, 12, 85, 34, 75]
arr2 = [42, 3, 86, 32, 856, 46]
arr1=np.array(arr1)
arr2=np.array(arr2)
si=arr1.shape
narr=np.random.rand(1,6)
arr1=arr1.astype(dtype=np.complex64)
arr1_mat=arr1.reshape(2,3)
arr2_mat=arr2.reshape(2,3)
arr3=arr1_mat+arr2_mat
