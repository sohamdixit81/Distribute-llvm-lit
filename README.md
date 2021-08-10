# Distribute-llvm-lit
generate_submit_files.py

- What does the project do - It takes the test files and covert it into .sub files(submit script) Which we need to submit to HTCondor.

- Commands to run this script -
python3 generate_submit_files.py \
  --output-submit-files-location <path to soham_lit_scripts/output_submit_files/> \
  --input-test-folder <path to ~/Workspace/tool-chain/llvm-project/llvm/test/>

- The python_scripts folder contains as follows
    - output_submit_files - *submit files will be stored in this which are converted.*
    - python_scripts      - *generate_submit_files.py, generate_submit_files.py, ht_condor_specific_library.py 
                      (generate_submit_files.py and ht_condor_specific_library.py will be include soon)*
    - tests               - *a.test b.test (sample test cases)*
