"""
Commands to run this script

python3 generate_submit_files.py \
  --output-submit-files-location <path to soham_lit_scripts/output_submit_files/> \
  --input-test-folder <path to ~/Workspace/tool-chain/llvm-project/llvm/test/>
"""
import time
import sys
import os
import glob
import argparse
from typing import List
from os import listdir, times
from os.path import isfile, join

def parse_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('--output-submit-files-location', type=str, required=True)
  parser.add_argument('--input-test-folder', type=str, required=True)
  parsedArgs = parser.parse_args()

  if not os.path.isdir(parsedArgs.input_test_folder):
    print("The input test folder doesn't exist")
    sys.exit(1)
  
  # We need to be sure if the user gives relative paths we should convert it to
  # absolute
  # TODO: revisit me if we need relative paths later, given that the absolute
  # paths could be different on execute nodes.
  parsedArgs.input_test_folder = os.path.abspath(parsedArgs.input_test_folder)
  parsedArgs.output_submit_files_location = os.path.abspath(parsedArgs.output_submit_files_location)
  return parsedArgs

def input_test_cases_searching(intputTestDir):
  # Exclude supurious tests which might have a keyword `RUN` in them.
  # There are a few approaches which might look similar to the ones followed in lit.cfg.py files.
  # We don't want a hard dependency on LLVM sources to change and hence we get affected.
  # Keeping it generic for now.
  #TODO: make it more better 
  excludes =  [".local.cfg", ".site.cfg", ".site.cfg.py.in", ".cfg.py", ".site.cfg.py.in", ".sh", "CMakeLists.txt"]
  # list out all the test cases.
    
  allFiles = glob.glob(join(intputTestDir, "**/*"), recursive=True)
  testCases = [f for f in allFiles if os.path.isfile(f)]
  print("Total test cases count = ", len(testCases))

  # Remove the files which are mentioned in the excludes list.
  # Such could be config files, cmake files, ...
  for eachExclude in excludes:
    testCases = remove_items(testCases, eachExclude)

  print("excluding = {}".format(excludes))
  print("Test cases after excluding = {} ".format(len(testCases)))
  return testCases

def generate_HTCondor_specific_submit_files(eachTest, parsedArgs):
  # Generate files names first
  testCaseBaseName = os.path.basename(eachTest)
  submitFileName = testCaseBaseName + ".sub"
  submitFileAbsPath = parsedArgs.output_submit_files_location + "/" + submitFileName

  submitFileData = {
    'executable' : '/home/soham/build_llvm_clang/bin/llvm-lit',
    'arguments' : '" ' + eachTest + " -v " + ' "',
    'transfer_input_files' : eachTest + ',' + ' /home/soham/build_llvm_clang/test/lit.site.cfg.py, /home/soham/llvm-project/llvm/test/lit.cfg.py, /home/soham/llvm-project/llvm/utils/lit/lit',
    'output' : submitFileAbsPath + ".output",
    'error' : submitFileAbsPath + ".error",
    'should_transfer_files' : 'IF_NEEDED',
    'when_to_transfer_output' : 'ON_EXIT',
    'log' : submitFileAbsPath + ".log"
  }
  # Open/touch file
  # add data
  # replace with specifics
  # end/close file.
  with open(submitFileAbsPath, 'w') as outfile:
    for key, value in submitFileData.items():
      outfile.write('%s = %s\n' % (key, value))
    outfile.write('queue')

  return submitFileAbsPath

def generate_generic_submit_files(testCases, parsedArgs):
  mapOfTestNameSubmitFile = {}
  for eachTest in testCases:
    submitFileName = generate_HTCondor_specific_submit_files(eachTest, parsedArgs)
    mapOfTestNameSubmitFile[eachTest] = submitFileName
  # DEBUG
  #for eachkey, val in mapOfTestNameSubmitFile.items():
  #  print(eachkey, " = ", val)
  return mapOfTestNameSubmitFile

# Removal of all occurrences of item from test_list
def remove_items(testCases, item):
    testCases = [ i for i in testCases if not os.path.basename(i).endswith(item) ]
    return testCases
    
def main():
  ##############################################
  # Argument parsing
  parsedArgs = parse_arguments()
  # Test cases folder as input.  
  intputTestDir = parsedArgs.input_test_folder
  # Submit file generation location.
  outputSubmitFilesLocation = parsedArgs.output_submit_files_location
  print("Looking for tests into = {}".format(intputTestDir))
  time.sleep(4)
  ##############################################
  # test cases crawling/searching.
  testCases = input_test_cases_searching(intputTestDir)
  ##############################################
  # We keep this routine very generic with the internal implementation being
  # handled by target specific generator(e.g HTCondor)
  print("Now generating submit files for each test case")
  time.sleep(2)
  print("...")
  time.sleep(5)
  print("...hold on tight\n")
  mapOfTestNameSubmitFile = generate_generic_submit_files(testCases, parsedArgs)
  print("Your submit files are generated at = {}".format(outputSubmitFilesLocation))
  ##############################################
  # DEBUG
  # Printing the output for debugging
  #for testName, testSubmitFileName in mapOfTestNameSubmitFile.items():
  #  print(testName)
  #  print("\t-", testSubmitFileName)


if __name__ == "__main__":
  main()