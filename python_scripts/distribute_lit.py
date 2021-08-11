"""Commands to run this script
    python3 distribute_lit.py
"""
from os import listdir
import subprocess
#to collect te file from given  path/location
files=listdir("../output_submit_files/")
#print(files)

#to iterate file list
for x in files:
	subprocess.run(["condor_submit","../output_submit_files/"+x])
	#print('done' + x)
	
	
