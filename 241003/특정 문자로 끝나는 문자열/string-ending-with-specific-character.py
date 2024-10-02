l=[input() for _ in range(10)];e=input()
print('\n'.join(filter(lambda x: x[-1] == e, l)))