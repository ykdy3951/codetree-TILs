a, o, c = input().split()

if o not in '+-/*':
    print('False')
else:
    t = o*2 if o == '/' else o
    print(a, o, c, '=', eval(a+t+c))