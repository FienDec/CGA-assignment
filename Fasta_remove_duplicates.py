#!/usr/bin/python3
#script to remove duplicates from fasta file

import re
import argparse
import os

#give full path to file as an argument
parser = argparse.ArgumentParser(description='File data')
parser.add_argument('file_path', type=str, help='Full path to fasta file')
args = parser.parse_args()

#change directory to the dir containing the fasta file you want to rid of duplicates
fasta_dir = os.path.dirname(args.file_path)
os.chdir(fasta_dir)

#define the filename
file = os.path.basename(args.file_path)

#sets only contain unique values
headers_set = set()

with open(file) as f:
    #lines are placed in a list
    lines = f.readlines()
    #if line starts with >, will be added to headers_set which will contain all the unique headers
    for i in lines:
        if re.search("^\>", i):
            headers_set.add(i)
    
    #make a new file with the unique fasta's
    file_list = file.split(".")
    if len(file_list) == 1:
        file_u = file_list[0] + "_unique"
    else:
        file_u = file_list[0] + "_unique." + file_list[1]
    
    with open(file_u, "w") as f2:
        #go over headers in headers_set and write them to the new file
        for head in headers_set:
            f2.write(head)
            #search for the starting point of the sequence in the list with all the lines of the original file
            for seq in lines[lines.index(head) + 1 :]:
                #write the sequence lines to the new file until a new header is encountered in the list with all the lines of the original file
                if not re.search("^\>", seq):
                    f2.write(seq)
                else:
                    break
    f2.close()
f.close()