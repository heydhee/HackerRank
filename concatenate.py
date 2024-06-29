import numpy as np
n,m,p=map(int,input().split())
array1=[]
for i in range(n):
    farr=list(map(int,input().split()))
    array1+=farr
arrayNP=np.array(array1)
arrnp=arrayNP.reshape(n,p)
array2=[]
for j in range(m):
    farr=list(map(int,input().split()))
    array2+=farr
arrayMP=np.array(array2)
arrmp=arrayMP.reshape(m,p)
final_array=np.concatenate((arrnp,arrmp))
print(final_array)