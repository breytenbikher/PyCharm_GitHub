file = [int(i) for i in open('INPUT.TXT')]
x, y = file
answer = None
finish = False
if x == y:
    answer = 0
    finish = True
elif x > y:
    mirror = 'H'
else:
    mirror = 'V'
if not finish:
    b = y + x
    if b % 2:
        answer = -1
        finish = True
    else:
        x_ans = int(b/2)
        y_ans = b - x_ans
        answer = 1
output = open('OUTPUT.TXT', 'w')
output.write(str(answer))
output.close()
if not finish:
    output = open('OUTPUT.TXT', 'a')
    output.write(f'\n{x_ans} {y_ans} {mirror}')



