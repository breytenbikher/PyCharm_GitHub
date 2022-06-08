a_max = 0
N = int(input(''))
for i in range(N):
    a = int(input(''))
    if not a % 5:
        if a > a_max:
            a_max = a
print(a_max)
