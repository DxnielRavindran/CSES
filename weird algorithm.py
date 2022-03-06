def weirdAlgo(inty):
    print(int(inty))
    while (inty != 1):           
        if inty % 2 == 0:
                inty  = inty / 2                  
        else:
            inty  = (inty * 3)  + 1  
        print(int(inty))


           
weirdAlgo(7)



