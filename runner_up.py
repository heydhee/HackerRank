#n = int(input())
#arr = list(map(int, input().split()))
#print(arr)
#newarr=arr-[max(arr)]
#print(newarr)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    narr = arr.remove(max(arr))
    runner=max(narr)
    print(runner)