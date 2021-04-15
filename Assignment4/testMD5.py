#!/usr/bin/env python

import collections
import argparse
import hashlib
import codecs

# crack_passwd.py [-h] -s SHADOW_FILE -d DICTIONARY_FILE
# sample_shadow.txt
# pmo455:$1$GC$t2R7Ly1RLRgoF/FcgmZHo0:15420::::::
# sample_dictionary.txt

def main():
    hash = hashlib.md5(("password").encode("utf-8")).hexdigest()
    hash2 = hashlib.md5(("password").encode("ascii")).hexdigest()
    print(hash)
    print(hash2)

if __name__ == "__main__":
    main()


