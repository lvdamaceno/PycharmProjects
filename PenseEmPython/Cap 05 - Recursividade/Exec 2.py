from random import randint

def fermat(a ,b ,c ,n):
    if (a**n + b**n) == c**n:
        print('a: ' + str(a) + ', ' + 'b: ' + str(b) + ', ' + 'c: ' + str(c) + ', ')
        print('Holy smokes, Fermat was wrong'+str((a**n + b**n))+'is equal from'+str(c**n))
    else:
        print('a: '+str(a)+', '+'b: '+str(b)+', '+'c: '+str(c)+', ')
        print('No, that does not works '+str((a**n + b**n))+' is diferent from '+str(c**n))


fermat(randint(0,99), randint(0,99), randint(0,99), 2)

trials=1

for t in range(trials):
    fermat(randint(1, 9), randint(1, 9), randint(1, 9), 2)

