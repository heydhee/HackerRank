import numpy as np
n=int(input())
a=[]
b=[]
for i in range(n):
    a+=(map(int,input().split()))

for j in range(n):
     b+=map(int,input().split())
#
mat1 = np.array(a).reshape(n,n)
mat2 = np.array(b).reshape(n, n)
#
print(np.dot(mat1,mat2))