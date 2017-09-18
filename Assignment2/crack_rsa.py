import collections


# from ShiftMethod import ShiftMethod


def main():
    # crack_rsa.py [-h] -e INT -n -INT --ciphertext INT
    #   -   Reveal plain text from cipher text using RSA algorithm. All values are integers
    #   -   -e  -   exponent
    #   -   -n  -   modulus
    #   -   --ciphertext

    # public key
    e = 211
    n = 67063

    p = 0
    q = 0

    n = p * q

    phi = (p - 1)*(q - 1)

    # m = 42
    # n = 3233
    # d = 2753
    # c = (m**e) % n
    # m = (c**d) % n

    # print ("c: " + str(c) + ", m: " + str(m))
    print ("p: " + str(p))
    print ("q: " + str(q))
    print ("n: " + str(n))

    print ("phi: " + str(phi))

    # print ("d: " + str(d))
    # print ("m: " + str(m))


if __name__ == "__main__":
    main()