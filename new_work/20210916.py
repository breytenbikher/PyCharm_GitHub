user_input = open('INPUT.TXT')
user_input = [i for i in user_input][0]
user_input = user_input.split(' ')
max_i = 0
min_i = int(user_input[1])
for i in user_input:
    i = int(i)
    if i > max_i:
        max_i = i
for i in user_input:
    i = int(i)
    if i < min_i:
        min_i = i
answer = str(max_i - min_i)
output = open('OUTPUT.TXT', 'w')
output.write(answer)