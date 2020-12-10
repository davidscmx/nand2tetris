#! /usr/bin/env python3

import sys
import re
#class Parser():
#
#    def __init__(asm_file):
#        pass
#
#    def parse_A_instruction(self):
#        pass
#
#    def parse_C_instruction(self):
#        pass
#
#def convert_decimal_to_binary():
#    pass

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

c_inst_dic["A+1"] = "110111"
c_inst_dic["M+1"] = "110111"
c_inst_dic["D-1"] = "001110"

c_inst_dic["A-1"] = "110010"
c_inst_dic["M-1"] = "110010"
c_inst_dic["D+A"] = "000010"
c_inst_dic["D+M"] = "000010"
c_inst_dic["D-A"] = "010011"
c_inst_dic["D-M"] = "010011"
c_inst_dic["A-D"] = "000111"
c_inst_dic["M-D"] = "000111"
c_inst_dic["D&A"] = "000000"
c_inst_dic["D&M"] = "000000"
c_inst_dic["D|A"] = "010101"
c_inst_dic["D|M"] = "010101"

dest_inst_dic = {}

dest_inst_dic["null"] = "000"
dest_inst_dic["M"]    = "001"
dest_inst_dic["D"]    = "010"
dest_inst_dic["MD"]   = "011"
dest_inst_dic["A"]    = "100"
dest_inst_dic["AM"]   = "101"
dest_inst_dic["AD"]   = "110"
dest_inst_dic["AMD"]  = "111"

jump_inst_dic = {}

jump_inst_dic["null"]=  "000"
jump_inst_dic["JGT"] =  "001"
jump_inst_dic["JEQ"] =  "010"
jump_inst_dic["JGE"] =  "011"
jump_inst_dic["JLT"] =  "100"
jump_inst_dic["JNE"] =  "101"
jump_inst_dic["JLE"] =  "110"
jump_inst_dic["JMP"] =  "111"

def parse_c_inst(c_inst):    
    dest,comp,jump = "","",""
    c_inst = c_inst.rstrip()
    if "=" in c_inst:        
        c_inst_1 = c_inst.split("=")
        dest = c_inst_1[0]
        comp = c_inst_1[1]
    else:
        dest = "null"

    if ";" in c_inst:
        c_inst_2 = c_inst.split(";")
        comp = c_inst_2[0]
        jump = c_inst_2[1]
    else:
        jump = "null"
    return (dest, comp, jump)

def get_c_inst(dest, comp, jump):

    c_inst_str = "111"    

    if "M" in comp:
        a = "1"
    else:
        a = "0" 

    c_inst_str += a

    alu_inst = c_inst_dic[comp]

    c_inst_str += alu_inst
    print("dest ", dest)
    dest_inst = dest_inst_dic[dest]

    c_inst_str += dest_inst

    jump_inst = jump_inst_dic[jump]

    c_inst_str += jump_inst

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
    
    for i, line in enumerate(asm_lines):
        line = ''.join(line.split())
        if line.startswith("//"):
            continue
        
        if line.startswith("@"):
            address = int(line.strip("@"))
            address_in_bin = f'{address:016b}'
            hack_file.write(address_in_bin+"\n")
        if "=" in line or ";" in line:
            print("i, line",i, line)
            dest, comp, jump = parse_c_inst(line)
            
            c_inst = get_c_inst(dest, comp, jump)            
            hack_file.write(c_inst+"\n")
    hack_file.close()

if __name__ == "__main__":
    main()
