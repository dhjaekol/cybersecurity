#!/usr/bin/env python

import collections
import argparse

def main():
    # 5 23 8 19
    parser = buildParser()
    args = parser.parse_args()
    g, n, A, B = getParserArgs(args)
    p = n

    # 1. Alice and Bob agree on a prime number, p, and a base, g, in the open
    # p = 23

    # 2. Alice chooses a secret integer a whose value is 6 and computes
    # A = g^a mod p
    # A = 5^6 mod 23

    a = 0
    a = naive_mod_inverse(A, a, g, p)

    # 3. Bob chooses a secret integer b whose value is 15 and computes
    # B = g**b % p

    b = 0
    b = naive_mod_inverse(B, b, g, p)

    # 4. Alice sends A to Bob and Bob sends B to Alice

    # 5. To obtain the shared secret, Alice computes k = B**a % p
    aliceSharedSecret = B**a % p

    # 6. To object the shared secret, Bob computes k = A**b % p
    bobSharedSecret = A**b % p

    print ("Secret key of Alice (a): " + str(a))
    print ("Secret key of Bob (b): " + str(b))
    print ("Shared secret computed by Alice (B^a mod n): " + str(aliceSharedSecret))
    print ("Shared secret computed by Bob (A^b mod n):  " + str(bobSharedSecret))


def naive_mod_inverse(A, a, g, p):
    for a in range(p):
        x = g ** a % p
        if x == A:
            break
    return a


# http://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInv(a, b):
    a = a % m
    x = 1
    while (x < m):
        if (a * x) % m == 1:
            return x
        i = i + 1


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = a
    return gcd, x, y


def getParserArgs(args):
    g = args.g[0]
    n = args.n[0]
    A = args.alice[0]
    B = args.bob[0]
    # print ("g: " + str(g) + ", n: " + str(n) + ", A: " + str(A) + ", B: " + str(B))
    return g, n, A, B


def buildParser():
    parser = argparse.ArgumentParser(description="Diffie-Hellman")
    parser.add_argument('-g', metavar='g', type=int, nargs='+', help='generator')
    parser.add_argument('-n', metavar='n', type=int, nargs='+', help='modulus')
    parser.add_argument('--alice', metavar='alice', type=int, nargs='+', help='alice')
    parser.add_argument('--bob', metavar='bob', type=int, nargs='+', help='bob')
    return parser




if __name__ == "__main__":
    main()