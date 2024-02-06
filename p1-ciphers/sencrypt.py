#!/usr/bin/python3

import argparse,os


def rand_generator(xO,m,a,c):
    return a*xO + c % m

def encrypt():
    # Generating a rand number
    rand = rand_generator()
    

def decrypt():
    pass

def main():
    parser = argparse.ArgumentParser(description="Encrypt text using a stream cipher")
    parser.add_argument("password", type=str, required=True, help="Specify password")
    parser.add_argument("plaintextfile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin.buffer, help="Input plaintext file (default: stdin)")
    parser.add_argument("ciphertextfile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin.buffer, help="Input ciphertext file (default: stdin)")
    args = parser.parse_args()


if __name__ == '__main__':
    main()