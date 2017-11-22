#!/usr/bin/env python2
import string


def xor(x):
    return ''.join(chr(ord(i) ^ 10) for i in x)


def shift(x):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    for i in x:
        if i.isupper() is True:
            n.append(upper[(upper.index(i) + 3) % 26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i) + 3) % 26])
        elif i.isdigit() is True:
            n.append(digits[(digits.index(i) + 3) % 10])
        else:
            n.append(i)
    return n


def encode(x):
    return x.encode("hex")    


if __name__ == "__main__":
    code = "63656e60716c7f687d39557f3c733d7f7c667b60556c616e6565627b606277"
    print "Decode the following string to find the flag:"
    print code
    print "Enter what you got after decoding:"

    arr = raw_input()

    your_code = encode(xor(shift(arr)))

    if your_code == code:
        print "Yeah!....You are a Genius"
    else:
        print "Oops....Try again"
        print "Looking at the source code might help"

