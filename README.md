<img width="700" alt="Gsoc" src="https://user-images.githubusercontent.com/84951816/130228946-b6d7c953-161d-409d-b6f6-ab92b653fd82.png" align="center" >

| **Student** | Soham Sanjay Dixit |
| --- | --- |
| **Github** | [@sohamdixit81](http://github.com/sohamdixit81)  |
| **Organisation**  | [LLVM](https://llvm.org/)  |
| **Project** | [Distributed lit testing](https://summerofcode.withgoogle.com/projects/#5185044001325056) | 

# What is done
- #### The [python_scripts](https://github.com/sohamdixit81/Distribute-llvm-lit/tree/master/python_scripts) folder contains
      
    
   - #### [ generate_submit_files.py](https://github.com/sohamdixit81/Distribute-llvm-lit/blob/master/python_scripts/generate_submit_files.py)
            It takes the test files and covert it into .sub files(submit script) Which we need to submit to HTCondor.
            Commands to run this script -
                                 python3 generate_submit_files.py \
                                 --output-submit-files-location <path to soham_lit_scripts/output_submit_files/> \
                                 --input-test-folder <path to ~/Workspace/tool-chain/llvm-project/llvm/test/>
  
  - ### The [test](https://github.com/sohamdixit81/Distribute-llvm-lit/tree/master/tests) folder contains                   
       a.test & b.test (sample test cases)    
  
  - ### The [Local-Lit](https://github.com/sohamdixit81/Distribute-llvm-lit/tree/master/Local-Lit) folder contains
   - #### [ locatio.py](https://github.com/sohamdixit81/Distribute-llvm-lit/blob/master/Local-Lit/location.py)
        Its is the script that we provide to transfer.sub to run the test cases on HTCondor.
            
   - #### [map.py](https://github.com/sohamdixit81/Distribute-llvm-lit/blob/master/Local-Lit/map.py)
       Its maintains the tree structure and copies the dependencies to the output folder which is created by it. 
       This output folder is given to HTCondor as transfer_input_files
                  
   - #### [transfer.sub](https://github.com/sohamdixit81/Distribute-llvm-lit/blob/master/Local-Lit/transfer.sub)
        Its is a sub script file which is given to HTCondor
                   
                   
# TODO

  - To run the test, the test requires specific executables. The script is pending that to identify the specific executables (dependencies).
  - And Finally Integrate each and every script So we will satisfy the Goal of this project.

