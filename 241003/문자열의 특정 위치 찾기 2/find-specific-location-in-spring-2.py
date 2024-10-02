a=input()
l=list(filter(lambda x: a in [x[2], x[3]], ["apple", "banana", "grape", "blueberry", "orange"]))
print('\n'.join(l+[str(len(l))]))