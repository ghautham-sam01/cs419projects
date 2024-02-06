#!/usr/bin/python3

import argparse,sys

def encrypt_text(key, plaintext,blocksize):
    
    cols = {k: bytearray() for k in range(len(key))}
    
    encrypted_text = bytearray()
    
    for i, b in enumerate(plaintext):
        cols_idx = i % len(key)
        cols[cols_idx].append(b)

    sorted_key = sorted(key)
    
    for start_idx in range(0,len(plaintext), blocksize):
        for k in sorted_key:
            cols_idx = key.index(k)
            encrypted_text.extend(cols[cols_idx])


    return encrypted_text



def main():
    parser = argparse.ArgumentParser(description="Encrypt text using a columnar transposition cipher")
    parser.add_argument("-b", "--blocksize", type=int, default=16, help="Specify the block size")
    parser.add_argument("-k", "--key", type=str, required=True, help="Specify the encryption key")
    parser.add_argument("plaintextfile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin.buffer, help="Input plaintext file (default: stdin)")
    args = parser.parse_args()

    plaintext = args.plaintextfile.read()
    encrypted_text = encrypt_text(args.key, plaintext, args.blocksize)
    sys.stdout.buffer.write(encrypted_text)

if __name__ == '__main__':
    main()