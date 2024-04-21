import numpy
arr = list(map(int, input().split()))
# rev = arr.reverse()
rarr = numpy.array(arr, float)
rev = numpy.flip(rarr)
print(rev)

# def arrays(arr):
#     rev = arr.reverse()
#     rarr = numpy.array(rev, float)
#     return print(rarr)
#
# arr = input().strip().split(' ')