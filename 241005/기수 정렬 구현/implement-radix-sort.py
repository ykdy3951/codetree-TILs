def radix_sort(arr, k):
    for pos in range(k):
        narr = [[] for _ in range(10)]
        for i in range(len(arr)):
            digit = 0 if len(str(arr[i])) < pos + 1 else int(str(arr[i])[-(pos+1)])
            narr[digit].append(arr[i])
        
        store_arr = []
        for i in range(10):
            for j in range(len(narr[i])):
                store_arr.append(narr[i][j])
        
        arr = store_arr
    return arr

n = int(input())
l = list(map(int, input().split()))
print(*radix_sort(l, 6))