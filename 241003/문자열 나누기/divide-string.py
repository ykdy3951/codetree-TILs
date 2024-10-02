input();l=''.join(input().split())
print('\n'.join([l[i:min(len(l), i+5)] for i in range(0,len(l), 5)]))