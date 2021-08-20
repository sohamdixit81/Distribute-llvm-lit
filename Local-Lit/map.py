import os    
import subprocess
import pathlib
from subprocess import call
import shutil

def copyinitialfiles(inputbuild, build, inputllvm_project, llvm_project):
    call(['cp', '-r', inputllvm_project + "/llvm/test/" + "", llvm_project + "/llvm"]) # cp llvm-project/llvm/test 
		#call(['cp', '-p', inputllvm_project + "/llvm/test/" + "", ]) # Linux

if __name__ == "__main__":

	# transfer code.
	destinationPath_ = "/home/soham/scripts/finaltransfer/output/"
	inputllvmprojectSourcePath_ = "/home/soham/llvm-project/"
	inputLLVMBuildPath_ = "/home/soham/build_llvm_clang"
	

	# create directories in destination
	llvm_project = destinationPath_ + "/" + "llvm-project"
	build = llvm_project + "/" + "build"

	#llvm = destinationPath_ + "/" + "llvm-project" + "/" + "llvm"
	#pathlib.Path(llvm_project).mkdir(parents=True, exist_ok=True)	# llvm-project

	## chdir and copy folders preserving the tree structure.
	os.chdir(inputllvmprojectSourcePath_ + "../")
	print("chdir to \n")
	print (os.getcwd())
	call(['cp', '--parent', 'llvm-project/llvm/test/', destinationPath_,  '-r'])
	call(['cp', '--parent', 'llvm-project/llvm/utils/lit', destinationPath_,  '-r'])
	call(['cp', '--parent', 'build_llvm_clang/bin', destinationPath_,  '-r'])
	call(['cp', '--parent', 'build_llvm_clang/lib', destinationPath_,  '-r'])
	call(['cp', '--parent', 'build_llvm_clang/test', destinationPath_,  '-r'])
	call(['cp', '--parent', 'build_llvm_clang/utils', destinationPath_,  '-r'])
	os.chdir(build)
	print("chdir to back to\n")
	print(os.getcwd())

	# Now I am running tests
	subprocess.run([build+ '/bin/llvm-lit','-s', llvm_project + '/llvm/test/Assembler'])



#	pathlib.Path(llvm_project).mkdir(parents=True, exist_ok=True)	# llvm-project
#	pathlib.Path(llvm).mkdir(parents=True, exist_ok=True)	# llvm-project/llvm
#	pathlib.Path(llvm_utils).mkdir(parents=True, exist_ok=True)	# llvm-project/build
#
#	pathlib.Path(build).mkdir(parents=True, exist_ok=True)	# llvm-project/build
