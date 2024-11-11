ans = 0

n, m = map(int,input().split())
a_arr = [0] * 1000001
b_arr = [0] * 1000001

D = {
    'L' : -1,
    'R' : 1
}

total_t = 0
for i in range(n):
    t, d = map(int, input().split())
    for j in range(total_t + 1, total_t + t + 1):
        a_arr[j] = a_arr[j-1] + D[d]
    total_t += t

total_t = 0
for j in range(m):
    t, d = map(int, input().split())
    for j in range(total_t + 1, total_t + t + 1):
        b_arr[j] = b_arr[j-1] + D[d]
    total_t += t

ans = 0
for i in range(1, total_t):
    if a_arr[i-1] != b_arr[i-1] and a_arr[i] == b_arr[i]:
        ans += 1
print(ans)