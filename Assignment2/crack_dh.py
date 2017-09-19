#!/usr/bin/env python

import collections
import argparse

def main():
    # Usage: crack_dh.py [-h] -g INT -n INT --alice INT --bob INT
    # -g = generator
    # -n = modulus
    # --alice (A)
    # --bob (B)

    parser = argparse.ArgumentParser(description="Diffie-Hellman")
    parser.add_argument('g', metavar='g', type=int, nargs='+', help='generator')
    parser.add_argument('n', metavar='n', type=int, nargs='+', help='modulus')
    parser.add_argument('A', metavar='alice', type=int, nargs='+', help='alice')
    parser.add_argument('B', metavar='bob', type=int, nargs='+', help='bob')
    args = parser.parse_args()
    g = args.g[0]
    n = args.n[0]
    A = args.A[0]
    B = args.B[0]
    print ("g: " + str(g) + ", n: " + str(n) + ", A: " + str(A) + ", B: " + str(B))

    # Alice sends A to Bob and Bob sends B to Alice
    # Alice computes shared key k = Ba mod p
    # Bob computes shared Key k = Ab mod p

    # 1. Alice and Bob agree on a prime number, p, and a base, g, in the open
    # p = 23

    # 2. Alice chooses a secret integer a whose value is 6 and computes
    # A = g**a mod p =  5**6 mod 23 = 8
    # a = 6
    # A = (g**a) % p
    # print("A: " + str(A))

    ecgdA = egcd(A, B)
    print(ecgdA)

    modInv()

    # 3. Bob chooses a secret integer b whose value is 15 and computes
    # B = g**b % p = 5**15 % 23 = 19
    # b = 15
    # B = (g**b) % p
    # print("B: " + str(B))

    # 4. Alice sends A to Bob and Bob sends B to Alice

    # 5. To obtain the shared secret, Alice computes k = B**a % p
    # ak = B**a % p
    # print("ak: " + str(ak))

    # 6. To object the shared secret, Bob computes k = A**b % p
    # bk = A**b % p
    # print("bk: " + str(bk))

    print ("Secret key of Alice (a): ")
    print ("Secret key of Bob (b): ")
    print ("Shared secret computed by Alice (B^a mod n): ")
    print ("Shared secret computed by Bob (A^b mod n):  ")

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = a
    return gcd, x, y

# http://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInv (a, b):
    a = a%m
    x = 1
    while (x < m):
        if (a*x) % m == 1:
            return x
        i = i + 1

if __name__ == "__main__":
    main()