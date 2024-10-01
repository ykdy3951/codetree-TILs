m1, d1, m2, d2 = map(int,input().split())
dotk = input()

t = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

l = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    l[i+1] += l[i]

days = l[m2 - 1] + d2 - (l[m1 - 1] + d1 - 1 + t.index(dotk))
print(days // 7 + 1 if days > 0 else 0)