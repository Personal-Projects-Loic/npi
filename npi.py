#!/usr/bin/env python3
import sys

def helper():
    print("Usage :")
    print("\t./npi.py -e \"sentence to encode\"")
    print("\t./npi.py -d \"number to decode\"")

def letterToAscii(input_str):
    rev_str = input_str[::-1]
    res = 0
    for char in rev_str:
        res = res * 256 + ord(char)
    return res

def asciiToLetter(num):
    result = []
    num = int(num)
    while num > 0:
        result.append(chr(num % 256))
        num //= 256
    return ''.join(result[::1])

def commandAppender(ascii):
    prefix = "echo '[q]sa[ln0=aln256%Pln256/snlbx]sb"
    suffix = "snlbxq'|dc"
    res = prefix + str(ascii) + suffix

    return res

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        helper()
    elif sys.argv[1] == "-e" and len(sys.argv) == 3:
        print("The command is :", commandAppender(letterToAscii(sys.argv[2])))
    elif sys.argv[1] == "-d" and len(sys.argv) == 3:
        print(asciiToLetter(sys.argv[2]))
    else:
        print("Invalid arguments. Use -h for help.")

if __name__ == "__main__":
    main()
