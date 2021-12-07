file = open('INPUT.TXT')
output = open('OUTPUT.TXT', 'a')
user_input = [i for i in file][1:]
user_input = [[int(j) for j in i.split(' ')] for i in user_input]
for i in user_input:
    a, b, x, y = i
    A = b * x
    B = b * (a - 1 - x)
    C = a * y
    D = a * (b - 1 - y)
    ans = max([A, B, C, D])
    output.write(f'{ans}\n')
