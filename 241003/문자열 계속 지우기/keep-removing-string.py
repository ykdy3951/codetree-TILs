a,b=list(input()),list(input())
while True:
    flag=True
    for i in range(0,len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            del a[i:i+len(b)]
            flag=False
    if flag:
        break
print(''.join(a))