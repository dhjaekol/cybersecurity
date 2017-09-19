import collections
import argparse

def main():
    # crack_rsa.py [-h] -e INT -n -INT --ciphertext INT
    #   -   Reveal plain text from cipher text using RSA algorithm. All values are integers
    #   -   -e  -   exponent
    #   -   -n  -   modulus
    #   -   --ciphertext

    # Key generation
    #  1. Choose random primes p and q and compute n =  p * q
    #  2. Compute Euler function phi(n) = (p - 1) (q - 1)
    #  3. Choose random encryption key e with gcd(e,  phi(n)) = 1
    #  4. Compute decryption key d, such that d.e = 1 (mod phi(n))
    #          that is   d.e = 1+ k phi(n), for some k

    # Public Key = (e,n)                Private Key: (d,n)
    # Encryption: c = me mod  n        Decryption: m = cd mod  n

    # Given c, (e, n) find m, d

    parser = argparse.ArgumentParser(description="RSA algorithm.")
    parser.add_argument('e', metavar='e', type=int, nargs='+', help='exponent')
    parser.add_argument('n', metavar='n', type=int, nargs='+', help='modulus')
    parser.add_argument('c', metavar='ciphertext', type=int, nargs='+', help='ciphertext')

    args = parser.parse_args()
    e = args.e
    n = args.n
    c = args.c

    e = e[0]
    n = n[0]
    c = c[0]

    print("e = " + str(e))
    print("n = " + str(n))
    print("c = " + str(c))

    #  1. Choose random primes p and q and compute n =  p * q - Example: n = 4711 - p1 = 7, q1 = 673
    primeFactors = primes(n)
    p = primeFactors[0]
    q = primeFactors[1]
    # print(p)
    # print(q)

    #  2. Compute Euler function phi(n) = (p - 1) (q - 1)
    n = p * q
    phi = (p - 1)*(q - 1)
    print(n)
    print(phi)

    #  3. Choose random encryption key e with gcd(e,  phi(n)) = 1
    #   We are given e

    #  4. Compute decryption key d, such that d.e = 1 (mod phi(n))
    #       that is   d.e = 1+ k phi(n), for some k

    # egcd(e,phi)
    d = egcd(3,20)[1]
    # print(d)

    # 5. Decrypt -> c**d mod n = m
    m = c**d % n

    # Output
    print ("p: " + str(p))
    print ("q: " + str(q))
    print ("phi: " + str(phi))
    print ("d: " + str(d))
    print ("m: " + str(m))

def gcd(a, b):
	while b:
 		a, b = b, a%b
	return a

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = a
    return gcd, x, y

def xgcd(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1

    print("prevx:" + str(prevx))
    print("x:" + str(x))
    print("prevy:" + str(prevy))
    print("y:" + str(y))

    print ("begin loop")
    while b:
        q = a/b

        print ("q = a/b, q = " + str(q) + ", a=" + str(a) + ", b=" + str(b))

        x, prevx = prevx - q*x, x

        print("x, prevx = prevx - q*x, prevx=", str(prevx) +
              ", q=" + str(q)
              + ", x=" + str(x))

        y, prevy = prevy - q*y, y

        print("y, prevy = prevy - q*y, prevy", str(prevy) +
              ", q=" + str(q) +
              ", y=" + str(y))

        a, b = b, a % b

        print ("a, b = b, a % b -> a, " + str(a) +
               ", b = " + str(b) +
               ", y = " + str(y))

    print ("end loop")

    print ("return a, prevx, prevy - " +
           "a = " + str(a) +
           "prevx = " + str(prevx) +
           "prevy = " + str(prevy))

    return a, prevx, prevy

# https://stackoverflow.com/questions/16996217/prime-factorization-list
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

if __name__ == "__main__":
    main()


