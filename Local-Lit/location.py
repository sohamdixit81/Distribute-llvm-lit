#!/usr/bin/env python3.8

import os    
import subprocess

getdir=os.listdir('/var/lib/condor/execute/')
input_path='/var/lib/condor/execute/'+getdir[0]+'/input'
output_path='/var/lib/condor/execute/'+getdir[0]+'/output'

subprocess.run([output_path+'/build_llvm_clang/bin/llvm-lit','-v',output_path+'/llvm-project/llvm/test/Bindings'])
