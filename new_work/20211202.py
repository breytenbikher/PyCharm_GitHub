file = open('INPUT.TXT')
output = open('OUTPUT.TXT', 'w')
output.write('')
output = open('OUTPUT.TXT', 'a')
user_input = [[int(j) for j in i.split(' ')] for i in file][1:]
for i in user_input:
    b, a, x, y = i
    R = b * (a - 1 - y)
    O = a * x
    M = a * (b - 1 - x)
    A = b * y
    ans = max([R, O, M, A])
    output.write(f'{ans}\n')
