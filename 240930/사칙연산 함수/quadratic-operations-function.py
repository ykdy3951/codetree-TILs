a, o, c = input().split()

if o not in '+-/*':
    print('False')
else:
    o = o*2 if o == '/' else o
    print(a, o, c, '=', eval(a+o+c))