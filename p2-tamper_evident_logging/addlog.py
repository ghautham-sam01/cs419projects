import os,sys,argparse, hashlib, base64
from datetime import datetime

def get_prev_hash():
    if os.path.exists('loghead.txt'):
        with open('loghead.txt', 'r') as file:
            return file.read().strip()
    else:
        return 'begin'

def write_to_file(hash_value):
    with open('loghead.txt', 'w') as file:
        file.write(hash_value)

def create_log_file():
    with open('log.txt', 'w'):
        pass

def main():
    if not os.path.exists('log.txt'):
        create_log_file()
        write_to_file("begin")
    elif not os.path.exists('loghead.txt'):
        print("Error: loghead.txt is missing.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Log entry")
    parser.add_argument("log",type=str, help="Log entry to add to the log text")
    
    args = parser.parse_args()

    last_hash = get_prev_hash()

    log_text = args.log.replace('\n',' ')

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    log_entry = f'{timestamp} - {last_hash} {log_text}'

    with open('log.txt', 'a') as f:
        f.write(log_entry + "\n")

    hash_value = hashlib.sha256(log_entry.encode()).digest()
    hash_base64 = base64.b64encode(hash_value).decode()

    write_to_file(hash_base64)

    print("Log entry added successfully.")

if __name__ == "__main__":
    main()    