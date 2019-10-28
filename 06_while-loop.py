while True:
    x=int(input("Enter a number to count to: "))
    if x=="q" or x=="salir":
        break
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
