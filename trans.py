import numpy
n,m=map(int,input().split())
array=list()
for i in range(n):
    a=list(map(int, input().split()))
    array.append(a)
arr=numpy.array(array)
trans=numpy.transpose(array)
flat=arr.flatten()
print(trans)
print(flat)