#! /usr/bin/env python3

import sys

class Parser():

    def __init__(asm_file):
        pass

    def parse_A_instruction(self):
        pass

    def parse_C_instruction(self):
        pass


def convert_decimal_to_binary():
    pass

def main():
    
    if len(sys.argv) != 2:
        print("use: ./assembler.py myfile.asm")

    asm_file = open(sys.argv[1], "r")
    asm_lines = asm_file.readlines()
    
    for line in asm_lines:
        if line.startswith("//"):
            continue
        
        if line.startswith("@"):
            address = int(line.strip("@"))
            address_in_bin = f'{address:08b}'
            print(address_in_bin)
        if "=" in line:
            pass
        
        print(line)

if __name__ == "__main__":
    main()
