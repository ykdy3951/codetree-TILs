l=[input() for _ in range(10)];e=input();l=list(filter(lambda x: x[-1] == e, l))
print('\n'.join(l) if len(l) else 'None')