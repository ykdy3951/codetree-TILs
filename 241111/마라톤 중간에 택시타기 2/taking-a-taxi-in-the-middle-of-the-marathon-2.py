n=int(input())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

l = [Point(*map(int,input().split()))]
total_dist = 0
for i in range(n-1):
    l.append(Point(*map(int,input().split())))
    total_dist += l[-1] - l[i]

sub = 0
for j in range(1, n-1):
    sub = min(sub, (l[j-1] - l[j+1]) - (l[j]-l[j+1]) - (l[j-1] - l[j]))
print(total_dist + sub)