import os
import argparse

parser=argparse.ArgumentParser(description='Creating Classes folders')
parser.add_argument('-filepath',type=str,help="Classes names txt file path:")
parser.add_argument('-dstpath', type=str,help="Path to create folder:")
args=parser.parse_args()
file_path=args.filepath
file_dst=args.dstpath
## opeing txt file.....
f=open(file_path,"r")
for i in f:
 filename=i.strip().split()[0]
 os.mkdir(str(filename))
