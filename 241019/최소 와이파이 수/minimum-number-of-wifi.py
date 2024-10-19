n,m=map(int,input().split())
l=list(map(int,input().split()))
x=0
st, val = 0, -1

while st < n:
    if l[st] == 1:
        val=st
    
    if val != -1:
        x += 1
        st += 2 * m
        val = -1

    st += 1

print(x)