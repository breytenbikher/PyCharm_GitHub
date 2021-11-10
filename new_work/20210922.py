def what_day(date):
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    st_date = '2021-10-10'
    day = 'Sa'
    f_date = date
    months_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    f_date = '-'.join([str(int(i)) for i in f_date.split('-')])

    def is_leap(year):
        if year % 400 == 0:
            leap = True
        else:
            if year % 100 == 0:
                leap = False
            else:
                if year % 4 == 0:
                    leap = True
                else:
                    leap = False
        return leap


    def det_day(s_day, n_days):
        '''Tu, 10 returns Fr'''
        remainder = n_days % 7
        for n, i in enumerate(days):
            if i == s_day:
                s_day_n = n + 1
        f_day_n = s_day_n + remainder
        if f_day_n > 7:
            f_day_n = f_day_n % 7
        #print(s_day_n,remainder,f_day_n)
        f_day = days[f_day_n - 1]
        return f_day



    #f_year, f_month, f_day = [int(i) for i in f_date.split('-')]

    def plus_day(date):
        '''retuns next date'''
        st_year, st_month, st_day = [int(i) for i in date.split('-')]
        new_year = st_year
        if not is_leap(st_year):
            if st_day < months_dict[st_month]:
                new_day = st_day + 1
                new_month = st_month
                new_year = st_year
            else:
                new_day = 1
                if st_month < 12:
                    new_month = st_month + 1
                    new_year = st_year
                else:#it's December
                    new_month = 1
                    new_year = st_year + 1
        else:
            days_in_month = months_dict[st_month]
            if st_month == 2:
                days_in_month += 1
            if st_day < days_in_month:
                new_day = st_day + 1
                new_month = st_month
                new_year = st_year
            else:
                new_day = 1
                if st_month < 12:
                    new_month = st_month + 1
                else:#it's December
                    new_month = 1
                    new_year = st_year + 1

        return f'{new_year}-{new_month}-{new_day}'
    date = st_date
    counter = 0
    while date != f_date:
        date = plus_day(date)
        counter += 1
    #print(counter)
    answer = det_day(day, counter)
    #print(counter)
    return answer

print(what_day('1921-01-01'))














