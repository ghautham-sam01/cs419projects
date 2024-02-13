#!/usr/bin/python3

import argparse,sys

m = 256  # modulus
a = 1103515245  # multiplier
c = 12345  # increment

def rand_gen(xO):
    return (a*xO + c) % m

def sdbm_hash(password):
    hash_val = 0
    for b in password:
        hash_val = b + (hash_val<<6) + (hash_val<<16) - hash_val
    return hash_val

def gen_ks(seed,len):
    ks = bytearray()
    curr_val = seed
    for _ in range(len):
        curr_val = rand_gen(curr_val)
        ks.append(curr_val)
    return ks

def apply_stream_cipher(password,input,output):
    seed = sdbm_hash(password)
    ks = gen_ks(seed,len(input))
    ciphertext = bytearray()
    for i in range(len(input)):
        ciphertext.append(input[i] ^ ks[i])
    output.write(ciphertext)


def main():
    '''
    parser = argparse.ArgumentParser(description="Encrypt or decrypt file using a stream cipher")
    parser.add_argument("password", help="Specify password")
    parser.add_argument("input_file", help="Input plaintext file (default: stdin)")
    parser.add_argument("output_file",help="Input ciphertext file (default: stdin)")
    args = parser.parse_args()
    try:
        with open(args.input_file, "rb") as input_file, open(args.output_file, "wb") as output_file:
            apply_stream_cipher(args.password.encode(), input_file.read(), output_file)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    '''
    test1 = []
    seed = 85
    for i in range(5):
       test1.append(rand_gen(seed) if len(test1)==0 else rand_gen(test1[i-1]))
    print(f' Test 1: using seed 85 {test1}')
    
    test2 = 'monkey01'
    print(f'Test 2: checking hashing function with monkey01 : {sdbm_hash(test2.encode())}')  

if __name__ == '__main__':
    main()