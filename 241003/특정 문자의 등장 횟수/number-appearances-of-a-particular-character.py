s=input()
a=[0,0]
for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        a[0]+=1
    elif s[i:i+2] == 'eb':
        a[1]+=1
print(*a)