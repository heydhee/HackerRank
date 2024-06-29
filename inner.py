import numpy as np
a=list(map(int,input().split()))
b=list(map(int,input().split()))
arr1=np.array(a)
arr2=np.array(b)
inn=np.inner(arr1, arr2)
out=np.outer(arr1, arr2)
print(inn)
print(out)