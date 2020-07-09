def short_story(idx=0):
    print("У попа была собака, он ее любил.")
    print("Она съела кусок мяса, он ее убил,")
    print("В землю закопал и надпись написал:")
    if idx < 100:
        short_story(idx + 1)
