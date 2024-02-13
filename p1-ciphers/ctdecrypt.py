#!/usr/bin/python3

import argparse,sys

def decrypt_text(key, ciphertext,blocksize):
    cols = {k: bytearray() for k in range(len(key))}
    decrypted_text = bytearray()

    for i, b in enumerate(ciphertext):
        cols_idx = i % len(key)
        cols[cols_idx].append(b)
    
    sorted_key = sorted(key)

    for start_idx in range(0, len(ciphertext), blocksize*len(key)):
        for k in sorted_key:           
            og_col_idx = key.index(k) 
            decrypted_text.extend(cols[og_col_idx])

    
    return decrypted_text



def main():
    parser = argparse.ArgumentParser(description="Decrypt text encrypted with a columnar transposition cipher")
    parser.add_argument("-b", "--blocksize", type=int, default=16, help="Specify the block size")
    parser.add_argument("-k", "--key", type=str, required=True, help="Specify the encryption key")
    parser.add_argument("ciphertextfile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin.buffer, help="Input ciphertext file (default: stdin)")
    args = parser.parse_args()

    try:
        with open(args.ciphertextfile.read(), 'rb') as file:
            ciphertext = file.read()
    except Exception as e:
        sys.stderr.write(f"An error occurred: {e}\n")
        exit(1)
        
    decrypted_text = decrypt_text(args.key, ciphertext, args.blocksize)
    sys.stdout.buffer.write(decrypted_text)

if __name__ == '__main__':
    main()