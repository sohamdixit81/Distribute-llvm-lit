#!/usr/bin/env python3.8
import os    
#from transfer import transfer
import shutil
import subprocess
getdir=os.listdir('/var/lib/condor/execute/')
input_path='/var/lib/condor/execute/'+getdir[0]+'/input'
output_path='/var/lib/condor/execute/'+getdir[0]+'/output'
def llvmLit():
	a_file = open(output_path+'/llvm-lit', "r")  #open the file in read mode
	list_of_lines = a_file.readlines()      #read all the lines from that file
	for x in range(len(list_of_lines)):
		if "sys.path.insert(0" in list_of_lines[x]:
			list_of_lines[x] = "sys.path.insert(0,"+"'"+str(os.getcwd())+"/output/lit')"+"\n"    # add the currect location to specified line in file like i gave 37
	a_file = open(output_path+"/llvm-lit", "w")   #again open same file for write
	a_file.writelines(list_of_lines)            #write all the lines again as it is
	a_file.close()      #close the file 

def litsite():
	a_file = open(output_path+"/lit.site.cfg.py", "r")  #open the file in read mode
	list_of_lines = a_file.readlines()      #read all the lines from that file
	#print(list_of_lines[81])
	crtpath=str(os.getcwd())
	print(crtpath)
	for x in range(len(list_of_lines)):
		if "os.path.join(config.llvm_src_root," in list_of_lines[x]:
			list_of_lines[x] = "    config, os.path.join(config.llvm_src_root, "+'"' + str(os.getcwd())+'/output/lit.cfg.py"))'+'\n'
	#print(list_of_lines[81])
	a_file = open(output_path+"/lit.site.cfg.py", "w")   #again open same file for write
	a_file.writelines(list_of_lines)            #write all the lines again as it is
	a_file.close()      #close the file 


# path
def transfer():
	#path ='/home/soham/scripts/input'

	# List files and directories
	#print("Before copying file:")
	#print(os.listdir(path))

	
	# Source path
	#src ='/home/soham/scripts/input'

	# Destination path
	#dest ='/home/soham/scripts/output'

	# Copy the content of
	# source to destination
	destination = shutil.copytree(input_path,output_path)

	# List files and directories
	#print("After copying file:")
	#print(os.listdir(path))

	# Print path of newly
	# created file
	print("Destination path:", destination)


transfer()
llvmLit()
litsite()

subprocess.run([output_path+'/llvm-lit','-v',output_path+'/empty.test'])



#path ='/var/lib/condor/execute/'



