a = 10
b = "ten"
print(str(a) + " is " + b)
print("%d is %s" % (a, b))
print("{} is {}".format(a, b))
print("{1} is {0}".format(a, b))
print("{a} is {b}".format(a=a, b=b))
print(f"{a} is {b}")
