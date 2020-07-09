n = 3
m = 4
a = [0] * n
for idx in range(n):
    a[idx] = [0] * m
a[0][0] = 5
print(a[1][0])
