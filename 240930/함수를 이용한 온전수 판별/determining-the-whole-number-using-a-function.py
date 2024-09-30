def chk(num : int):
    if num % 2 == 0 or num % 10 == 5 or (num % 3 == 0 and num % 9 != 0):
        return 0
    return 1
cnt = 0
a, b = map(int, input().split())
for i in range(a, b + 1):
    cnt += chk(i)
print(cnt)