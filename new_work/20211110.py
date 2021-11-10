file = open('input.txt')
file = [i.replace('\n','') for i in file][1:]
the_dict = {}
for i in range(len(file)):
    if not i % 2:
        name = file[i]
        score = file[i+1]
        score = score.split(' ')
        score = sum([int(i) for i in score])
        the_dict[name] = score
for name in the_dict:
    if the_dict[name] == min(the_dict.values()):
        answer = name
output = open('output.txt','w')
output.write(answer)


