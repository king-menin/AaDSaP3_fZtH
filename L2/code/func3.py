def some_func(arg1, arg2, *args, kv_arg1=1, kv_arg2=2, **kwargs):
    print(arg1, arg2, end=" ")
    print("kv_arg1=", kv_arg1, " kv_arg2=", kv_arg2, sep="")
    for arg in args:
        print(arg, end=" ")
    print()
    for key, val in kwargs.items():
        print(key, "=", val, end=" ", sep="")
    print()


some_func(-1, -2, 0, 1, kv_arg1=2, kv_arg2=3, kv_arg3=4)
