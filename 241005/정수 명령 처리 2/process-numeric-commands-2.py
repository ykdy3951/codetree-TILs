from collections import deque

class Queue:
    def __init__(self):
        self.arr = deque()

    def push(self, num):
        self.arr.append(num)
    
    def front(self):
        return self.arr[0]

    def size(self):
        return len(self.arr)

    def empty(self):
        return int(len(self.arr) == False)

    def pop(self):
        return self.arr.popleft()

q = Queue()

for _ in range(int(input())):
    x = input().split()

    if x[0] == 'push':
        q.push(int(x[1]))

    else:
        print(getattr(q, x[0])())