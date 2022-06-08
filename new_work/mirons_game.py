import random
MIN_LEN = 3
MAX_LEN = 5
twenty_k_words = [i[:-1] for i in open('20k_words_dictionary.txt')]
ok = False
while not ok:
    the_word = random.choice(twenty_k_words)
    if MIN_LEN <= len(the_word) <= MAX_LEN:
        ok = True
#print(the_word)
counter = 0
victory = False
while not victory:
    counter += 1
    ok = False
    while not ok:
        word = input(f'{len(the_word)} letters:  ')
        if len(word) != len(the_word):
            print(f'We need {len(the_word)} letters')
        else:
            ok = True
    for a, b in zip(word, the_word):
        if a == b:
            print(f'[{a}]', end=' ')
        elif a in the_word:
            print(f'({a})', end=' ')
        else:
            print(a, end=' ')
    if word == the_word:
        victory = True
    print()

print('Great! You are the champion!')
print('Number of guesses: ', counter)