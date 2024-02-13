#!/usr/bin/python3

import argparse, sys, sencrypt

def decrypt(password, input, output):
    seed = sencrypt.sdbm_hash(password)
    ks = sencrypt.gen_ks(seed,len(input))

    # Creating an initialization vector (IV) for applying CBC to the first block
    iv = bytearray(ks[:16])

    prev_ciphertxt_block = iv

    padding = 0

    for i in range(0, len(input), 16):
        ciphertxt_block = input[i:i+16]
        
        # Decrypt ciphertext block
        temp_block = bytearray(16)
        for j in range(16):
            temp_block[j] = ciphertxt_block[j] ^ ks[j]
        
        ks_block = sencrypt.gen_ks(seed,16)

        for j in range(15, -1, -1):
            fir = ks_block[j] & 0xf
            sec = (ks_block[j] >> 4) & 0xf
            temp_block[fir], temp_block[sec] = temp_block[sec], temp_block[fir]
        
        # Apply CBC
        plaintxt_block = bytearray(16)
        for j in range(16):
            plaintxt_block[j] = temp_block[j] ^ prev_ciphertxt_block[j]
        
        # Write plaintext block
        if i + 16 >= len(input):
            padding = plaintxt_block[-1]
            output.write(plaintxt_block[:-padding])
        else:
            output.write(plaintxt_block)
        
        # Update previous ciphertext block for CBC
        prev_ciphertxt_block = ciphertxt_block    

def main():
    parser = argparse.ArgumentParser(description="Decrypt a file using the enhanced block cipher")
    parser.add_argument("password", help="Password for decryption")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()

    try:
        with open(args.input_file, "rb") as input_file, open(args.output_file, "wb") as output_file:
            decrypt(args.password, input_file.read(), output_file)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)

if __name__ == '__main__':
    main()