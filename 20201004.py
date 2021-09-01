import random
mylist = [i for i in range(-10,10)]
ok = False
while not ok:
    mylist2 = mylist[:]
    a = mylist2.pop(random.randint(0,len(mylist2)-1))
    b = mylist2.pop(random.randint(0,len(mylist2)-1))
    c = mylist2.pop(random.randint(0,len(mylist2)-1))
    d = mylist2.pop(random.randint(0,len(mylist2)-1))
    l1,l2,r1,r2 = 0,0,0,0
    try:
        l1 = a**b
        l2 = c**d
        r1 = b**a
        r2 = d**c
    except:
        pass
    if all([l1,l2,r1,r2]):
        if l1 == l2 and r1 == r2:
            ok = True
            print(a,b,c,d)
