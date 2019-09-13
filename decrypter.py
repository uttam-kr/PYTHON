#!/usr/bin/python
import sys

def main(argv):
    if(len(argv) < 2):
        print("please provide the encrypted file and private key both")
        print("ex:- python decrypter.py encrypted_uttam.csv private_key_file.pem")
        sys.exit(1)
    else:
        pass
    encrypted_file = argv[0]
    private_key_file = argv[1]
    file_decode(encrypted_file,private_key_file)
def file_decode(receive_file,private_key_file):
    INPUT_FILE=receive_file
    private_key=private_key_file
    OUTPUT_FILE="decrypted_file.csv"
    file_decode="openssl smine -decrypt \
        -in "+INPUT_FILE+" \
        -inform DEM -inkey "+private_key+""
    os.system(file_decode)
if __name__ == "__main__":
    main(sys.argv[1:])
              
