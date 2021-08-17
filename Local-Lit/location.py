import os    
from transfer import transfer
import subprocess
def llvmLit():
	a_file = open("/home/soham/scripts/output/llvm-lit", "r")  #open the file in read mode
	list_of_lines = a_file.readlines()      #read all the lines from that file
	for x in range(len(list_of_lines)):
		if "sys.path.insert(0" in list_of_lines[x]:
			list_of_lines[x] = "sys.path.insert(0,"+"'"+str(os.getcwd())+"/output/lit')"+"\n"    # add the currect location to specified line in file like i gave 37
	a_file = open("/home/soham/scripts/output/llvm-lit", "w")   #again open same file for write
	a_file.writelines(list_of_lines)            #write all the lines again as it is
	a_file.close()      #close the file 

def litsite():
	a_file = open("/home/soham/scripts/output/lit.site.cfg.py", "r")  #open the file in read mode
	list_of_lines = a_file.readlines()      #read all the lines from that file
	#print(list_of_lines[81])
	crtpath=str(os.getcwd())
	print(crtpath)
	for x in range(len(list_of_lines)):
		if "os.path.join(config.llvm_src_root," in list_of_lines[x]:
			list_of_lines[x] = "    config, os.path.join(config.llvm_src_root, "+'"' + str(os.getcwd())+'/output/lit.cfg.py"))'+'\n'
	#print(list_of_lines[81])
	a_file = open("/home/soham/scripts/output/lit.site.cfg.py", "w")   #again open same file for write
	a_file.writelines(list_of_lines)            #write all the lines again as it is
	a_file.close()      #close the file 



transfer()
llvmLit()
litsite()

subprocess.run(['./output/llvm-lit','-v','/home/soham/scripts/output/empty.test'])
