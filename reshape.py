import numpy
arr =list(map (int, input().split()))
L=numpy.array(arr)
#arr = numpy.array(L)
#print(arr)
newarr = L.reshape((3,3))
print(newarr)