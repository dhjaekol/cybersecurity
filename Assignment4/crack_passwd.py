#!/usr/bin/env python

import collections
import argparse
import hashlib
import crypt

# crack_passwd.py [-h] -s SHADOW_FILE -d DICTIONARY_FILE
# sample_shadow.txt
# pmo455:$1$GC$t2R7Ly1RLRgoF/FcgmZHo0:15420::::::
# sample_dictionary.txt

def main():
    parser = buildParser()
    args = parser.parse_args()
    s, d = getParserArgs(args)

    with open(d, encoding='utf-8') as f:
        commonPwds = f.read().splitlines()

    with open(s, encoding='utf-8') as f:
        shadowFile = f.read().splitlines()

    # file = open("decrypt.txt", "w")
    for pwd in shadowFile:
        rec = pwd.split(":")
        pwdTuple = rec[1].split("$")

        # file.write("pwd:" + rec[1])
        if pwdTuple[1] == "1":
            for commonPwd in commonPwds:
                key_string = commonPwd
                salt = pwdTuple[2]
                saltedPwd = key_string + salt

                hash = crypt.crypt(key_string, salt)   # hashlib.md5crypt(key_string, salt)
                # file.write("cpwd: " + saltedPwd + ", hash: " + hash )
                if (hash == pwdTuple[3]):
                    print (rec[0] + ":" + commonPwd )

    # file.close()

    # print(lines)
    # print(passwords)

def buildParser():
    parser = argparse.ArgumentParser(description="crack_passwd")
    parser.add_argument('s', metavar='s', nargs='+', help='shadow_file')
    parser.add_argument('d', metavar='d', nargs='+', help='dictionary_file')
    return parser

def getParserArgs(args):
    s = args.s[0]
    d = args.d[0]
    return s, d

if __name__ == "__main__":
    main()


