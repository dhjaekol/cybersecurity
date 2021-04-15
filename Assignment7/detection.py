#!/usr/bin/env python2

# Develop a detection tool for Python viruses that uses signatures detection.py.
# You can use regular expressions for implementing the signature matching.
# Try to design accurate signatures for your own virus and the simple viruses described in python-noob.txt file

import collections
import argparse
import os
import glob
import sys

def main():
    parser = buildParser()
    args = parser.parse_args()
    dirToInfect = getParserArgs(args)
    if dirToInfect == "":
        print ("Please enter a directory to detect infected python files (.py).")
        sys.exit()

    for filename in glob.glob(os.path.join(dirToInfect, '*.py')):
        with open(filename) as f:
            program = f.readlines()
            fileIsInfected = False
            for line in program:
                if "-=::Vort3x::=-" in line:
                    fileIsInfected = True
                    # print ("file:" + filename + ", line: " + line)
                elif '-=::VortX::=-' in line:
                    fileIsInfected = True
                    # print ("file:" + filename + ", line: " + line)
                elif 'def virusAdded ():' in line:
                    fileIsInfected = True
        f.close()
        if fileIsInfected:
            print ("File:" + filename + " has been infected!")

def buildParser():
    parser = argparse.ArgumentParser(description="virus")
    parser.add_argument('-d', metavar='d', nargs='+', help='Directory of files to detect for viruses.')
    return parser

def getParserArgs(args):
    d = args.d[0]
    return d

if __name__ == "__main__":
    main()
