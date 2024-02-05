#!/usr/bin/python3

import argparse,sys

def encrypt_text(key, plaintext):
    pass

def main():
    parser = argparse.ArgumentParser(description="Encrypt text using a columnar transposition cipher")
    parser.add_argument("-b", "--blocksize", type=int, default=16, help="Specify the block size")
    parser.add_argument("-k", "--key", type=str, required=True, help="Specify the encryption key")
    parser.add_argument("plaintextfile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin, help="Input plaintext file (default: stdin)")
    args = parser.parse_args()

    plaintext = args.plaintextfile.read()
    encrypted_text = encrypt_text(args.key, plaintext)
    sys.stdout.buffer.write(encrypted_text)

if __name__ == '__main__':
    main()