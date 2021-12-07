file = open('INPUT.TXT')
file = [i for i in file]
#denominator = [i for i in file][1]
numerator, denominator = file[0], file[1]
def recurs(numerator,denominator,n):
