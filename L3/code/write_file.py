f = open("L3/text2.txt", "w")
lst = [str(i) + " " + str(i-1) for i in range(20)]
for idx in lst:
    f.write(idx + '\n')
f.close()
