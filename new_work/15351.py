A = [int(i) for i in open('INPUT.TXT')][1:]
counter = 0
for i in A:
    if not i%7:
        if i%4:
            counter += 1
output = open('OUTPUT.TXT', 'w')
output.write(str(counter))