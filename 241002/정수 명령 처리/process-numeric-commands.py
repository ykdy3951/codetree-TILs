class Stack:
    def __init__(self):
        self.items = []
                
    def push(self, item):
        self.items.append(item)
                
    def empty(self):
        return not self.items
                
    def size(self):
        return len(self.items)
        
    def pop(self):    
        return self.items.pop()
                
    def top(self):      
        return self.items[-1]

n = int(input())
s = Stack()
for i in range(n):
    x=list(input().split())
    if x[0] == 'push':
        s.push(int(x[1]))
    elif x[0] == 'pop':
        print(s.pop())
    elif x[0] == 'size':
        print(s.size())
    elif x[0] == 'empty':
        print(int(s.empty()))
    else:
        print(s.top())