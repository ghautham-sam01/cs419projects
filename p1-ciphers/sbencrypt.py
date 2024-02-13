#!/usr/bin/python3

import argparse,sys,sencrypt


def encrypt(password, input, output):

    seed = sencrypt.sdbm_hash(password)
    ks = sencrypt.gen_ks(seed,len(input))

    # Creating an initialization vector (IV) for applying CBC to the first block
    iv = bytearray(ks[:16])

    prev_ciphertxt_block = iv

    # Padding
    padding = 16 - (len(input) % 16)
    if padding == 0: 
        padding = 16
    
    for i in range(0, len(input), 16):
        plaintxt_block = input[i:i+16]

        if i+16 >= len(input):
            plaintxt_block += bytes([padding] * padding)
        
        temp_block = bytearray(plaintxt_block)
        for j in range(16):
            temp_block[j] ^= prev_ciphertxt_block[j]
        
        ks_block = sencrypt.gen_ks(seed, 16)

        for j in range(16):
            fir = ks_block[j] & 0xf
            sec = (ks_block[j]>>4) & 0xf
            temp_block[fir], temp_block[sec] = temp_block[sec], temp_block[fir]
        
        ciphertxt_block = bytearray(16)
        for j in range(16):
            ciphertxt_block[j] = temp_block[j] ^ ks_block[j]

        output.write(ciphertxt_block)

        prev_ciphertxt_block = ciphertxt_block 
            
def main():
    parser = argparse.ArgumentParser(description="Encrypt a file using the enhanced block cipher")
    parser.add_argument("password", help="Password for encryption")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()

    try:
        with open(args.input_file, "rb") as input_file, open(args.output_file, "wb") as output_file:
            encrypt(args.password, input_file.read(), output_file)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)

if __name__ == "__main__":
    main() 