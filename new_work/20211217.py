a = int(input(''))
b = int(input())
n = int(input())
m = int(input())
min_time_n = n + a * (n - 1)
max_time_n = n + a * (n + 1)
min_time_m = m + b * (m - 1)
max_time_m = m + b * (m + 1)
#print(min_time, max_time)
if max_time_m < min_time_n or max_time_n < min_time_m:
    answer = -1
else:
    if n >= m:
        answer = f'{min_time_n} {max_time_n}'
    else:
        answer = f'{min_time_m} {max_time_m}'
print(answer)


