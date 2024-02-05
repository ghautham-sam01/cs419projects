#!/usr/bin/python3

import argparse,sys

def decrypt_text(key, ciphertext):
    pass

def main():
    parser = argparse.ArgumentParser(description="Decrypt text encrypted with a columnar transposition cipher")
    parser.add_argument("-b", "--blocksize", type=int, default=16, help="Specify the block size")
    parser.add_argument("-k", "--key", type=str, required=True, help="Specify the encryption key")
    parser.add_argument("ciphertextfile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin, help="Input ciphertext file (default: stdin)")
    args = parser.parse_args()

    ciphertext = args.ciphertextfile.read()
    decrypted_text = decrypt_text(args.key, ciphertext)
    sys.stdout.buffer.write(decrypted_text)

if __name__ == '__main__':
    main()