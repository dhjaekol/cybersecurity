#!/usr/bin/env python

import collections
import argparse
import hashlib
from md5crypt import md5crypt
import multiprocessing

# crack_passwd.py [-h] -s SHADOW_FILE -d DICTIONARY_FILE
# sample_shadow.txt
# pmo455:$1$GC$t2R7Ly1RLRgoF/FcgmZHo0:15420::::::
# sample_dictionary.txt

def main():
    parser = buildParser()
    args = parser.parse_args()
    s, d = getParserArgs(args)

    with open(d,"r") as f:
        commonPwds = f.read().split('|')

    with open(s,"r") as f:
        shadowFile = f.read().splitlines()

    data = ( commonPwds, shadowFile )

    # coreCount = multiprocessing.cpu_count()
    # p = multiprocessing.Pool(coreCount)
    # p.map(crackPassword, data)

    crackPassword(data)

def crackPassword ((commonPwds, shadowFileChunk)):
    hashDict = {"dhjaekol":[("1","2")]}

    for pwd in shadowFileChunk:
        rec = pwd.split(":")
        pwdTuple = rec[1].split("$")

        hashList = []
        if pwdTuple[1] == "1":
            salt = pwdTuple[2]
            if salt in hashDict:
                hashList = hashDict[salt]
            else:
                for commonPwd in commonPwds:
                    key_string = commonPwd
                    saltedPwd = key_string + salt
                    hash = md5crypt(key_string, salt)
                    hashSplit = hash.split("$")
                    hashList.append((key_string, hashSplit[3]))
                hashDict[salt] = hashList

        for hash in hashList:
            if (hash[1] == pwdTuple[3]):
                print (rec[0] + ":" + hash[0] )

def buildParser():
    parser = argparse.ArgumentParser(description="crack_passwd")
    parser.add_argument('-s', metavar='s', nargs='+', help='shadow_file')
    parser.add_argument('-d', metavar='d', nargs='+', help='dictionary_file')
    return parser

def getParserArgs(args):
    s = args.s[0]
    d = args.d[0]
    return s, d

if __name__ == "__main__":
    main()


