import collections
import argparse


# from ShiftMethod import ShiftMethod


def main():
    # crack_rsa.py [-h] -e INT -n -INT --ciphertext INT
    #   -   Reveal plain text from cipher text using RSA algorithm. All values are integers
    #   -   -e  -   exponent
    #   -   -n  -   modulus
    #   -   --ciphertext

    parser = argparse.ArgumentParser(description="RSA algorithm.")
    parser.add_argument('e', metavar='e', type=int, nargs='+', help='exponent')
    parser.add_argument('m', metavar='n', type=int, nargs='+', help='modulus')
    parser.add_argument('c', metavar='ciphertext', type=int, nargs='+', help='ciphertext')

    args = parser.parse_args()
    e = args.e
    m = args.m
    c = args.c

    print("e = " + str(e))
    print("m = " + str(m))
    print("c = " + str(c))

    # Encrypt	m**e mod n = c
    # (c / m**e)

    # Decrypt	c**d mod n = m


def xgcd(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1

    print("prevx:" + prevx)
    print("x:" + x)
    print("prevy:" + prevy)
    print("y:" + y)

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


# def gcd(a, b):
#     if a == 0:
#         return b
#     return gcd(b%a, a)


# def power(x, y, m):
#     if y == 0:
#         return 1
#     p = power(x , y/2, m) % m
#     p = (p * p) % m
#     return (y%2 == 0)? p: (x * p) % ,


if __name__ == "__main__":
    main()


