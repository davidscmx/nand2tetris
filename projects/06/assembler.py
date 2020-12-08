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



def parse_c_inst(c_inst):
    pass
def return_c_inst(dest, comp, jump):

    c_inst_str = "111"    

    if "M" in comp:
        a = "1"
    else:
        a = "0" 

    c_inst_str +=a

    c_inst_dic = {}
    c_inst_dic["0"]  = "101010"
    c_inst_dic["1"]  = "111111"
    c_inst_dic["-1"] = "111010"
    c_inst_dic["D"]  = "001100"
    
    c_inst_dic["A"]  = "110000"
    c_inst_dic["M"]  = "110000"

    c_inst_dic["!A"]  = "110001"
    c_inst_dic["!M"]  = "110001"

    c_inst_dic["-D"]  = "001111"

    c_inst_dic["-A"]  = "110011"
    c_inst_dic["-M"]  = "001111"

    c_inst_dic["D+1"] = "011111"
    return c_inst_str


def main():    
    if len(sys.argv) != 2:
        print("use: ./assembler.py myfile.asm")
        exit(1)
    
    if not sys.argv[1].endswith(".asm"):
        print("Please input an .asm file")
        exit(2)

    asm_file_str = sys.argv[1]
    with open(asm_file_str, "r") as asm_file:
        asm_lines = asm_file.readlines()
    
    hack_file_str = asm_file_str.replace(".asm", ".hack")
    hack_file = open(hack_file_str, "w") 
    
    for line in asm_lines:
        if line.startswith("//"):
            continue
        
        if line.startswith("@"):
            address = int(line.strip("@"))
            address_in_bin = f'{address:016b}'
            hack_file.write(address_in_bin+"\n")
        if "=" in line or ";" in line:
            pass
        
    hack_file.close()

if __name__ == "__main__":
    main()
