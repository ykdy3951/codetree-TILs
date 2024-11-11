ans = 0

n, m = map(int,input().split())
total_t = 0
a_arr = [0] * 1000001
b_arr = [0] * 1000001

for i in range(n):
    v, t = map(int, input().split())
    for j in range(total_t + 1, total_t + t + 1):
        a_arr[j] = a_arr[j-1] + v
    total_t += t

total_t = 0
for j in range(m):
    v, t = map(int, input().split())
    for j in range(total_t + 1, total_t + t + 1):
        b_arr[j] = b_arr[j-1] + v
    total_t += t


def set_status(a, b):
    if a == b:
        return 2
    else:
        return int(a < b)

status = set_status(a_arr[0], b_arr[0])
start = 1
ans = 0
for i in range(start, total_t):
    temp_status = set_status(a_arr[i], b_arr[i])
    
    if temp_status != status:
        ans += 1
        status = temp_status
print(ans)