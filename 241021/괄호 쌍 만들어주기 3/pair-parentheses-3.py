s=input();n=len(s)
b=[0] * (n + 1)

for i in range(n):
    b[i+1] = b[i]
    if s[i] == ')':
        b[i+1] += 1

ans = 0
for i in range(n):
    if s[i] == '(':
        ans += b[-1] - b[i+1]
print(ans)