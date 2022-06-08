import datetime
start = datetime.datetime.now()
N = 2
x = 1
number_of_variants = 2**N
counter = 0
for i in range(number_of_variants):
    if '1' * x in bin(i):
        counter += 1
answer = (counter / number_of_variants) * 100
print(counter)
print(answer, '%')
finish = datetime.datetime.now()
print(finish-start)