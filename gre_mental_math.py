import numpy as np
from numpy.random import rand, randint, randn, choice
import math
import time
from math import sqrt
from itertools import count, islice

## divide by 5
def div5():
    ans = randint(1,200)
    num = ans*5
    txt = 'Divide '+str(num)+' by 5.'
    return txt, ans

## Doubling and Halving
def dbl_haf():
    a = randint(1, 200)*5
    b = randint(1, 500)*2
    choose = randint(0,2)
    txt = 'What is '+str(choose*a+(1-choose)*b)+'*'+str(choose*b+(1-choose)*a)+'?'
    ans = a*b
    return txt, ans

def sqr5():
    a = randint(1, 20)*5
    txt = 'What is '+str(a)+'^2?'
    return txt, a*a

def adj_sq():
    a = randint(1, 20)*5
    b = randint(1,10)*10
    choose = randint(0, 2)
    num = choose*a + (1-choose)*b
    num += randint (-1, 2)
    txt = 'What is '+str(num)+'^2?'
    return txt, num*num

def mult():
    a = randint(2, 21)
    b = randint(2, 21)
    txt = 'What is '+str(a)+'*'+str(b)+'?'
    return txt, a*b

def div():
    a = randint(1, 1000)
    b = randint(1, 21)
    txt = 'What is '+str(a*b)+'/'+str(b)+'?'
    return txt, a

def big_div():
    a = randint(1, 1000000)
    b = randint(max(1/100,2), 100000)
    txt = 'Approximate '+str(a)+'/'+str(b)+'.'
    return txt, a/b

def add_sub():
    a = randint(1, 100)
    b = randint(1, 100)
    choose = randint(0, 2)
    operation = ['+', '-'][choose]
    ans = [a+b, a-b][choose]
    txt = 'What is '+str(a)+operation+str(b)+'?'
    return txt, ans

def frac_dec():
    a = 1
    while a==1:
        a1 = randint(1,10)
        a2 = choice([1, 10, 100])
        a = a1*a2
    b = randint(1, a1)
    txt = str(b)+'/'+str(a)+' = ?'
    return txt, b/a

def dec_frac():
    a = randint(1, 10)
    txt = 'Express '+str(round(1/a, 4))+' fraction.'
    ans = '1/'+str(a)
    return txt, ans


def sort_frac():
    ls = [[randint(1,30), randint(2,30)],
        [randint(1,30), randint(2,30)],
        [randint(1,30), randint(2,30)],
        [randint(1,30), randint(2,30)]][:randint(2,5)]
    ans_vals = sorted(ls, key=lambda x: x[0]/x[1])
    txt = 'Sort: '
    for val in ls:
        txt += str(val[0])+'/'+str(val[1])+', '
    txt = txt[:-2]+'. Use benchmark values, cross-mult or x/y technique.'
    ans = ''
    for val in ans_vals:
        ans += str(val[0])+'/'+str(val[1])+', '
    return txt, ans[:-2]

def comp_frac():
    fr1 = [randint(1,10), randint(1, 10)]
    fr2 = [x+randint(1,5) for x in fr1]
    ls = [fr1, fr2]
    ans_vals = sorted(ls, key=lambda x: x[0]/x[1])
    txt = 'Sort: '
    for val in ls:
        txt += str(val[0])+'/'+str(val[1])+', '
    txt = txt[:-2]+'. Use benchmark values, cross-mult or x/y technique.'
    ans = ''
    for val in ans_vals:
        ans += str(val[0])+'/'+str(val[1])+', '
    return txt, ans[:-2]

def appx_roots():
    a = choice([2,3,5,7])
    txt = 'SQRT('+str(a)+') = ?'
    return txt, round(math.sqrt(a),2)

def divisibility():
    a = randint(1, 1000000)
    b = randint(2,12)
    q = a*b
    c = randint(2,12)
    choice = randint(0,2)
    c = c*choice + b*(1-choice)
    txt = 'Is '+str(q)+' divisible by '+str(c)+'?'
    return txt, 'YES' if q%c==0 else'NO'

def powers():
    a = randint(2,16)
    pow = randint(2,4)
    is_root = randint(0,2)
    if is_root:
        if pow==2:
            term = 'SQRT'
            val = a*a
        else:
            term = 'CUBEROOT'
            val = a*a*a

        txt = term+'('+str(val)+') = ?'
        return txt, a
    else:
        ans = a*a if pow==2 else a*a*a
        txt = 'What is '+str(a)+'^'+str(pow)+'?'
        return txt, ans

def is_prime(n=0, gen=True):
    if gen:
        ## give only odd numbers
        n = randint(1,101)
        if n%2 == 0:
            n -= 1
    ans = n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))
    txt = str(n)+' is  prime?'
    return txt, ans

def prime():
    hi = randint(2,11)
    lo = randint(1,hi)
    lo, hi = lo*10, hi*10
    txt = 'How many primes between '+str(lo)+' and '+str(hi)+'?'
    ans = sum([is_prime(x, False)[1] for x in range(lo, hi+1)])
    return txt, ans
    







def get_question():
    questions = [div, mult, adj_sq, sqr5, dbl_haf, div5, big_div, frac_dec, 
                dec_frac, sort_frac, comp_frac, appx_roots, prime, is_prime, powers, divisibility]
    func = choice(questions)
    return func()

def run():
    print('Press enter for answer.\nEnter for the next question.\nQUIT after answering.\n\n')
    while True:
        Q, A = get_question()
        print(Q)
        ptime = time.time()
        inp = input()
        print(A)
        print('You took ', round(time.time()-ptime, 2), ' secs')
        print('-'*20)
        inp = input()
        if inp=='QUIT':
            return
        

run()
