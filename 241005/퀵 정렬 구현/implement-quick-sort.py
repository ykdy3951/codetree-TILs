def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def qsort(arr, low, high):
    if low < high:
        pos = partition(arr, low, high)

        qsort(arr, low, pos - 1)
        qsort(arr, pos + 1, high)

n = int(input())
l = list(map(int, input().split()))
qsort(l, 0, n-1)
print(*l)