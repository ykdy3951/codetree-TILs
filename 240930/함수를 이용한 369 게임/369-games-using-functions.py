a,b=map(int,input().split());cnt=0
for i in range(a, b+1):
    flag = False
    str_i = str(i)
    for j in '369':
        if j in str_i:
            flag = True
            break
    if i % 3 == 0:
        flag = True
    
    if flag:
        cnt += 1
print(cnt)