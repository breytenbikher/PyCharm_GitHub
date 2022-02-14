answer = 0
text = 'NO'
list_1 = []
ok = False
while not ok:
    a = int(input(''))
    if a >= 0:
        list_1.append(a)
    else:
        ok = True
        for i in list_1:
            if i%10 == 3:
                answer += i
        for i in list_1:
            if 100<=i<1000:
                text = 'YES'
print(answer, text)