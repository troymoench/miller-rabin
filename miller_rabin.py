# Miller-Rabin Primality Test

from random import randint

def isodd(n):
    return n % 2 == 1

def miller_rabin_test(n, a):

    # write n - 1 = r*2^s
    s = 0
    r = (n - 1)
    while not isodd(r):
        r = r // 2 # integer division
        s += 1

    # let b = a^r mod n
    b = pow(a, r, n)

    prev = -1 % n
    next = b
    # print("prev =", prev)
    # print("next =", next)
    if (prev == (-1 % n)) and (next == 1):
        return True
    i = 0
    while i <= s:
        prev = next
        next = pow(b,2**i,n)
        # print("prev =", prev)
        # print("next =", next)
        if (prev == (-1 % n)) and (next == 1):
            return True
        i += 1
    return False


print("Miller-Rabin Primality Test")
n = int(input("n = "))
a_vals = int(input("values of a = "))

primes = 0
for i in range(a_vals):
    a = randint(1,n-1)
    # print("a =", a)
    if miller_rabin_test(n, a):
        primes += 1


if primes == a_vals:
    print("prime")
else:
    print("composite")
