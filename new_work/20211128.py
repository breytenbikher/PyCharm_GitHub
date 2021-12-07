file = open('INPUT.TXT')
user_input = [int(i) for i in file][0]
answer = 0
for i in range(1, user_input+1):
    if user_input % i == 0:
        answer += i
answer = str(answer)
output = open('OUTPUT.TXT', 'w')
output.write(answer)
