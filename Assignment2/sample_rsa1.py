import collections
import argparse
# from ShiftMethod import ShiftMethod


def main():

    m = 42
    p = 61
    q = 53
    e = 17
    n = 3233
    d = 2753

    phi = (p - 1) * (q - 1)

    c = (m**e) % n
    m = (c**d) % n

    # print ("c: " + str(c) + ", m: " + str(m))
    print ("p: " + str(p))
    print ("q: " + str(q))
    print ("phi: " + str(phi))
    print ("d: " + str(d))
    print ("m: " + str(m))


if __name__ == "__main__":
    main()
