import numpy as np
n=int(input())
arr=list()
for i in range(n):
    arr+=map(float,input().split())
array=np.array(arr)
farr=np.reshape(array,(n,n))
print(np.linalg.det(farr))