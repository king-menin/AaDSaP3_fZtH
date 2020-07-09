# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for j in range(len(row)):
        row[j] = int(row[i])
    a.append(row)
