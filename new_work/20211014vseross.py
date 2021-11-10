def a(A,B):
    # A = int(input(''))
    # B = int(input(''))
    n_1 = 0
    n_2 = 0
    A = int(A)
    B = int(B)
    counter = 0
    while A != 0 and B != 0:
        counter += 1
        if A >= B:
            n_1 += 1
            A -= 2
            B -= 1
        else:
            n_2 += 1
            A -= 1
            B -= 2
    ok = A + B == 0
    if not ok:
        print('-1')
    else:
        print(n_1, n_2)
a(4,5)