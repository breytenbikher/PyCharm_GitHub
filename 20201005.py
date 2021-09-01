import os
dictionary = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Aforizmy_i_mysli_ob_istorii.txt
alphabet = '- '
alphabet += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

texts = os.listdir('texts')

for i in texts:
    print(i)
    text = open(f'texts/{i}', encoding='utf-8')
    #text = [i for i in text]
    for i in text:
        for symbol in i:
            i = i.lower()
            if symbol not in alphabet:
                i = i.replace(symbol, '')
        i_list = i.split(' ')
        for g in i_list:
            if g:
                if g not in dictionary:
                    dictionary[g] = 1
                else:
                    dictionary[g] += 1

    unique_words = dictionary.keys()
    total_words = sum(dictionary.values())

    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


    for a in range(30):
        print(dictionary[a][0],' ', round(dictionary[a][1]/dictionary[0][1]*100, 1), f'% of {dictionary[0][0]}')


    print()
    

    
    
