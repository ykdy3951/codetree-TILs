n=int(input())
x = [1, 2, 3]
score = [0, 0, 0]
for i in range(n):
    a, b, c = map(int, input().split())
    for i in range(3):
        if a == x[i]:
            x[i] = b
        elif b == x[i]:
            x[i] = a

        if x[i] == c:
            score[i] += 1

print(max(score))