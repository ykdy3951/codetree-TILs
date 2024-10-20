n=int(input())
l=list(map(int,input().split()))

arr=[0, 0]
for i in l:
    arr[i%2] += 1

while not (arr[0] == arr[1] or arr[0] == arr[1] + 1):
    if arr[0] > arr[1] + 1:
        arr[0] -= 1
    else:
        arr[1] -= 2
        arr[0] += 1

print(arr[0] + arr[1])