import numpy
n,m=map(int,input().split())
array=list()
for i in range(n):
    a=list(map(int, input().split()))
    array.append(a)
arr=numpy.array(array)
summ=numpy.sum(arr, axis=0)
prod=numpy.prod(summ)
print(prod)
