A = dict(zip('abcdef', list(range(6))))
for key in A:
    print(key, A[key])

A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print(key, val)

print(A.keys())
print(A.values())
