import numpy as np
n,m=map(int, input().split())
for i in range(n):
    arr1=list(map(int, input().split()))
array1=np.array(arr1)
a=np.reshape(array1,(n,m))
for j in range(n):
    arr2=list(map(int, input().split()))
array2=np.array(arr2)
b=np.reshape(array2,(n,m))
# print(a)
# print(b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))