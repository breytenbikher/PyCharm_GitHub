value = 0
max_value = 0
alm_max_val = 0
while value <= 500:
    value = int(input(''))
    if value <= 500:
        if not value % 2:
            if value > max_value:
                #print(value, max_value, alm_max_val)
                alm_max_val = max_value
                max_value = value
                #print(value, max_value, alm_max_val)
            elif value > alm_max_val:
                alm_max_val = value
print(max_value)
print(alm_max_val)