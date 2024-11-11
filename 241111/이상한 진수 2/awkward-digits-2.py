a=input()
idx=a.find(
    '0'
)
if idx == -1:
    print(int(a[:-1]+'0',2))
else:
    print(int(a[:idx]+'1'+a[idx+1:],2))